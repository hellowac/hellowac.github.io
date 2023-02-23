# alembic教程(转)

[sqlalchemy]: https://docs.sqlalchemy.org/en/14/ "SQLAlchemy"
[alembic]: https://alembic.zzzcomputing.com/en/latest/index.html "Alembic"
[alembic.ini]: https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file "alembic.ini"
[target_metadata]: https://alembic.sqlalchemy.org/en/latest/ops.html?highlight=target_metadata#alembic.operations.Operations.f "target_metadata"

官方文档: <https://alembic.sqlalchemy.org/en/latest/index.html>{target="_blank"}

相关项目: <https://github.com/python-gino/gino>{target="_blank"} - [文档](https://www.bookstack.cn/read/gino-1.0-zh/3d56d5fe80ab5932.md){target="_blank"}

翻译的alembic文档: <https://hellowac.github.io/alembic_doc/>{target="_blank"}

[alembic]{target="_blank"}是[sqlalchemy]{target="_blank"}的作者开发的。用来做OMR模型与数据库的迁移与映射。`alembic`使用方式跟`git`有点了类似，表现在两个方面，第一个，`alembic`的所有命令都是以`alembic`开头；第二，`alembic`的迁移文件也是通过版本进行控制的。首先，通过`pip install alembic`进行安装。以下将解释`alembic`的用法：

## 初始化[alembic]{target="_blank"}仓库

在终端中，`cd` 到你的项目目录中，然后执行命令`alembic init alembic`，创建一个名叫`alembic`的仓库。

## 创建模型类

创建一个`models.py`模块，然后在里面定义你的模型类，示例代码如下：

```python
from sqlalchemy import Column,Integer,String,create_engine,Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    username = Column(String(20),nullable=False)
    password = Column(String(100),nullable=False)

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer,primary_key=True)
    title = Column(String(100),nullable=False)
    content = Column(Text, nullable=False)
```

### 设置数据库连接

在[alembic.ini]{target="_blank"}中设置数据库的连接，`sqlalchemy.url = driver://user:pass@localhost/dbname`，比如以mysql数据库为例，则配置后的代码为：

```python
sqlalchemy.url = mysql+mysqldb://root:root@localhost/alembic_demo?charset=utf8
```

### 设置[target_metadata]{target="_blank"}

为了使用模型类更新数据库，需要在`env.py`文件中设置[target_metadata]{target="_blank"}，默认为`target_metadata=None`。使用`sys`模块把当前项目的路径导入到`path`中：

```python
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from models import Base
... #省略代码
target_metadata = Base.metadata # 设置创建模型的元类
... #省略代码
```

## 自动生成迁移文件

使用`alembic revision --autogenerate -m "message"`将当前模型中的状态生成迁移文件。

## 更新数据库

使用`alembic upgrade head`将刚刚生成的迁移文件，真正映射到数据库中。同理，如果要降级，那么使用`alembic downgrade head`。

## 修改代码后

重复4~5的步骤。

## 命令和参数解释

1. `init`：创建一个alembic仓库。
2. `revision`：创建一个新的版本文件。
3. `–autogenerate`：自动将当前模型的修改，生成迁移脚本。
4. `-m`：本次迁移做了哪些修改，用户可以指定这个参数，方便回顾。
5. `upgrade`：将指定版本的迁移文件映射到数据库中，会执行版本文件中的upgrade函数。如果有多个迁移脚本没有被映射到数据库中，那么会执行多个迁移脚本。
6. `[head]`：代表最新的迁移脚本的版本号。
7. `downgrade`：会执行指定版本的迁移文件中的downgrade函数。
8. `heads`：展示head指向的脚本文件版本号。
9. `history`：列出所有的迁移版本及其信息。
10. `current`：展示当前数据库中的版本号。

另外，在你第一次执行`upgrade`的时候，就会在数据库中创建一个名叫`alembic_version`表，这个表只会有一条数据，记录当前数据库映射的是哪个版本的迁移文件。

## 经典错误

| 错误描述                                                     | 原因                                                         | 解决办法                                                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------------------------------------------- |
| `FAILED: Target database is not up to date.`                 | 主要是`heads`和`current`不相同。`current`落后于heads的版本。 | 将`current`移动到`head`上。`alembic upgrade head`                       |
| `FAILED: Can't locate revision identified by '77525ee61b5b'` | 数据库中存的版本号不在迁移脚本文件中                         | 删除数据库的`alembic_version`表中的数据，重新执行`alembic upgrade head` |
