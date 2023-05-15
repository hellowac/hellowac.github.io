# nameko 的使用及注意事项

参考自: <https://zhuanlan.zhihu.com/p/82924225>

nameko 是python语言的一个微服务框架，支持通过 rabbitmq 消息队列传递的 rpc 调用，也支持 http 调用。本文主要介绍 nameko 的 rpc 调用以及一些注意事项。

## 创建项目

本文采用项目结构如下：

```text
- project
    - services
        - service1
            - __init__.py
            - service1.py
        - service2
            - __init__.py
            - service2.py
    - utils
        - __init__.py
        - dependencies.py
    - __init__.py
    - config.yaml
```

python 需使用pip安装 `nameko` 库，同时需要安装 `rabbitmq` 。 `rabbitmq` 安装推荐使用 `docker` `，docker` 命令如下：

```shell
docker pull rabbitmq：3.7-management
docker run --hostname my-rabbit --name rabbitmq-borg -p 15672:15672 -p 25672:25672 -p 5672:5672 -d rabbitmq:3.7-management
```

docker 管理页面为 `localhost:15672`，默认用户名密码 `guest`、`guest`。

## 微服务定义

在 service1.py 下定义一个微服务。`nameko` 中每个微服务被定义为一个类，类变量 `name` 即为微服务的名称，由 `rpc` 装饰器装饰的方法即为对外提供的`rpc`调用方法。

```python
from nameko.rpc import rpc


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)
```

## 微服务启动

微服务启动时需要指定配置文件，在 `config.yaml` 中写入配置如下：

```buildoutcfg
AMQP_URI: 'pyamqp://guest:guest@localhost'
WEB_SERVER_ADDRESS: '0.0.0.0:8000'
rpc_exchange: 'nameko-rpc'
max_workers: 10
parent_calls_tracked: 10

LOGGING:
    version: 1
    handlers:
        console:
            class: logging.StreamHandler
    root:
        level: DEBUG
        handlers: [console]
```

启动时需要制定微服务类，将上面定义的 GreetingService 类提至 services 模块，在 services/__init__.py 中导入如下：

```buildoutcfg
from .service1.service1 import GreetingService
```

此时就可以启动微服务了，启动命令：

```buildoutcfg
nameko run --config config.yaml services:GreetingService
```

其中 services 为项目路径下的 services 模块，GreetingService 为模块内的微服务类。可在一条启动的命令上同时添加多个微服务类。

以上为 nameko run 的方式启动，官方文档中还提及 ServiceRunner 的启动方式，如果微服务较多，各服务配置有所区别可以使用。参考：[文档](https://nameko.readthedocs.io/en/stable/key_concepts.html#running-services)

## 微服务远程调用

### 一般脚本调用微服务如下

```python
config = {'AMQP_URI': "amqp://guest:guest@localhost"}
from nameko.standalone.rpc import ClusterRpcProxy
with ClusterRpcProxy(config) as rpc:
    result = rpc.greeting_service.hello("world")
    result_async = rpc.greeting_service.hello.call_async("world async")
    print(result)
    print(result_async.result())
```

rpc后紧跟的是微服务定义时的类变量 name 的值即为微服务名称，接着紧跟rpc方法，使用 call_async 为异步调用，而调用 result_async.result() 时会等待异步任务返回结果。需要注意的是， 运行 ClusterRpcProxy(config) 时会创建与队列的连接，该操作比较耗时，如果有大量的微服务调用，不应该重复创建连接，应在语句块内完成所有调用。异步调用的结果只能在语句块内获取，即调用 .result() 等待结果。语句块之外连接断开就无法获取了。

### flask 内异步调用微服务

flask 内应该使用 flask_nameko，尤其注意不要在视图函数里实例化 ClusterRpcProxy(config)，否则每个用户的每次请求都会重新创建销毁与队列的连接，比较耗时。
flask_nameko 的使用见官方 [github](https://github.com/jessepollak/flask-nameko) 。

### 微服务间相互调用

如果我们需要在 service2.py 中定义的微服务里调用 service1.py 的 GreetingService 微服务，可通过以下代码实现：

```python
from nameko.rpc import rpc, RpcProxy
from utils.dependencies import LoggingDependency


class Service2:
    name = "service2"
    log = LoggingDependency()
    other_rpc = RpcProxy("greeting_service")

    @rpc
    def hello_service2(self, name):
        return self.other_rpc.hello(name)

```

## nameko 框架使用的一些注意事项（坑）

### 微服务监控

nameko微服务出错不会自动打印错误日志，需要加上监控相关的依赖，参考 [github issue](https://github.com/nameko/nameko/issues/243)。
该依赖并未打印相应的调用栈，我们可以加上，在 utils/dependencies.py 定义监控依赖如下：

```python
import datetime
import traceback
import logging
from weakref import WeakKeyDictionary
from nameko.dependency_providers import DependencyProvider

log = logging.getLogger(__name__)


class LoggingDependency(DependencyProvider):

    def __init__(self):
        self.timestamps = WeakKeyDictionary()

    def worker_setup(self, worker_ctx):

        self.timestamps[worker_ctx] = datetime.datetime.now()

        service_name = worker_ctx.service_name
        method_name = worker_ctx.entrypoint.method_name

        log.info("Worker %s.%s starting", service_name, method_name)

    def worker_result(self, worker_ctx, result=None, exc_info=None):

        service_name = worker_ctx.service_name
        method_name = worker_ctx.entrypoint.method_name

        if exc_info is None:
            status = "completed"
        else:
            status = "errored"
            log.error(traceback.print_tb(exc_info[2]))

        now = datetime.datetime.now()
        worker_started = self.timestamps.pop(worker_ctx)
        elapsed = (now - worker_started).seconds

        log.info("Worker %s.%s %s after %ss",
                 service_name, method_name, status, elapsed)

```

在 services/service1/service1.py 的 GreetingService 使用该监控依赖如下：

```python
from nameko.rpc import rpc
from utils.dependencies import LoggingDependency


class GreetingService:
    name = "greeting_service"
    log = LoggingDependency()

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)

    @rpc
    def raise_exception(self):
        raise Exception()

```

这样如果微服务出错就会打印相应的调用栈了，可以远程调用 raise_exception 测试。

### 耗时资源的初始化

对于每次微服务调用，nameko会找到相应的微服务类，将其实例化成对象，该对象再去处理具体的业务逻辑。这就意味着耗时资源的初始化如果放在 __init__ 方法里就会每次微服务调用都重新初始化一次，该类资源应当初始化为类变量，在多个实例建共用。比如导入一个机器学习的模型用于预测，如果将导入模型这个操作放在 init 方法里就会有性能问题，应当放在类变量里。如以下伪码：

```python
from nameko.rpc import rpc
from utils.dependencies import LoggingDependency


class GreetingService:
    name = "greeting_service"
    log = LoggingDependency()
    model = load_model(model_path)  # 耗时资源应初始化为类变量

    @rpc
    def predict(self, x):
        return GreetingService.model.predict(x)

```

### 　线程安全问题  

如果资源初始化在微服务方法之外完成，即资源可能同时被多个微服务实例共用，如上面伪代码中的机器学习模型，那么该资源应当是线程安全的。尤其是使用数据库的时候，如 pymysql，一般数据库连接的初始化是在微服务类外完成的，同时被多个微服务共用，那就应当使用连接池（如使用　DbUtils）进行封装，使相应数据库操作实现线程安全。redis, pymongo 内部实现连接池，不需要进一步封装。

### 　计算密集型任务导致任务重试

nameko 框架基于协程实现，对于 IO 操作能够自动切换控制流，但是如果是计算密集型的任务则会一直占用资源。如果是把 nameko 用来做计算密集型耗时任务的异步调用，耗时大于２分钟（如处理一批数据），那么可能会导致任务不断重试。出现这种情况的原因是 nameko 框架需要每隔 60　秒给 rabbitmq 发送心跳信息，而计算密集型任务无法切换控制流，导致框架无法发送心跳。两分钟后，rabbitmq 认为微服务下线，就把之前的任务重新放入队列重试。对于这种任务，可以间隔一段时间使用一次 time.sleep(0.1)　交出控制流。如果计算是由第三方库引入的，无法直接控制，可以使用 tpool 转换为系统级的线程去处理。具体代码如下：

```python
import time
from eventlet import tpool
from nameko.rpc import rpc
from utils.dependencies import LoggingDependency


def some_fun_you_can_not_control():
    start = time.time()
    while True:
        if time.time() - start > 300:
            break


class GreetingService:
    name = "greeting_service"
    log = LoggingDependency()

    @rpc
    def computation_bound(self):
        # 该任务一经发起会被不停重试，消耗计算资源
        start = time.time()
        while True:
            if time.time() - start > 300:
                break

    @rpc
    def computation_bound_sleep(self):
        # 使用 sleep 交出控制流让框架能够发送心跳
        start = time.time()
        while True:
            if int(time.time() - start) % 5 == 0:
                time.sleep(0.1)

            if time.time() - start > 300:
                break

    @rpc
    def computation_bound_tpool(self):
        # 使用 tpool 切换为线程运行
        return tpool.execute(some_fun_you_can_not_control)

    @rpc
    def raise_exception(self):
        raise Exception()

```
