# pip

- 创建时间: 2022年08月15日14:46:21
- 官网: <https://pypi.org/project/pip/>

## 常用命令

### 安装

在`Python 3.4`版本之后以及`Python 2.7.9`版本之后，官网的安装包当中就已经自带了`pip`，用户直接在安装完Python之后就可以直接使用，要是使用由`virtualenv`或者`pyvenv`创建的虚拟环境，那么`pip`也是被默认安装的

如果是需要自己另外安装`pip`包的，在已经配置好Python的环境当中运行下面这个命令行

```shell
py -m ensurepip --upgrade
```

> 另外一种方式是从官网上(<https://bootstrap.pypa.io/get-pip.py>)直接下载`get-pip.py`脚本，然后直接运行`python get-pip.py`脚本即可

### 如何使用

安装后，在命令行中输入pip，然后按下回车，就会出现下图所示的使用说明：

```shell
~ > pip

Usage:   
  pip <command> [options]

Commands:
  install                     Install packages.
                              (安装包)
  download                    Download packages.
                              (下载包)
  uninstall                   Uninstall packages.
                              (卸载包)
  freeze                      Output installed packages in requirements format.
                              (以`requirements`格式输出已安装的软件包。)
  list                        List installed packages.
                              (列出已安装的软件包。)
  show                        Show information about installed packages.
                              (显示有关已安装软件包的信息。)
  check                       Verify installed packages have compatible dependencies.
                              (验证已安装的软件包是否具有兼容的依赖项。)
  config                      Manage local and global configuration.
                              (管理本地和全局配置。)
  search                      Search PyPI for packages.
                              (在 PyPI 中搜索包。[已不可用])
  cache                       Inspect and manage pip's wheel cache.
                              (检查和管理 pip 的wheel缓存。)
  index                       Inspect information available from package indexes.
                              (检查包索引中的可用信息。)
  wheel                       Build wheels from your requirements.
                              (根据您的要求构建 wheel)
  hash                        Compute hashes of package archives.
                              (计算包的哈希值。)
  completion                  A helper command used for command completion.
                              (用于命令完成的辅助命令。)
  debug                       Show information useful for debugging.
                              (显示对调试有用的信息。)
  help                        Show help for commands.
                              (显示命令帮助。)

General Options:
  -h, --help                  Show help.
                              (显示帮助。)
  --debug                     Let unhandled exceptions propagate outside the main subroutine, instead of logging them to stderr.
                              (让未处理的异常传播到主子例程之外，而不是将它们记录到 stderr。)
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
                              (以隔离模式运行 pip，忽略环境变量和用户配置。)
  --require-virtualenv        Allow pip to only run in a virtual environment; exit with an error otherwise.
                              (允许 pip 只在虚拟环境中运行； 否则退出错误。)
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
                              (给更多的输出。 选项是附加的，最多可使用 3 次。)
  -V, --version               Show version and exit.
                              (显示版本并退出。)
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging levels).
                              (减少输出。 选项是附加的，最多可以使用 3 次（对应于 WARNING、ERROR 和 CRITICAL 日志记录级别）。)
  --log <path>                Path to a verbose appending log.
                              (详细附加日志的路径。)
  --no-input                  Disable prompting for input.
                              (禁用输入提示。)
  --proxy <proxy>             Specify a proxy in the form scheme://[user:passwd@]proxy.server:port.
                              (以 scheme://[user:passwd@]proxy.server:port 形式指定代理。)
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
                              (每个连接应尝试的最大重试次数（默认 5 次）。)
  --timeout <sec>             Set the socket timeout (default 15 seconds).
                              (设置套接字超时（默认 15 秒）。)
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
                              (路径已存在时的默认操作：(s)witch、(i)gnore、(w)ipe、(b)ackup、(a)bort。)
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
                              (将此主机或主机：端口对标记为受信任，即使它没有有效或任何 HTTPS。)
  --cert <path>               Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL Certificate Verification' in pip documentation for more information.
                              (PEM 编码的 CA 证书包的路径。 如果提供，覆盖默认值。 有关更多信息，请参阅 pip 文档中的“SSL 证书验证”。)
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
                              (SSL 客户端证书的路径，包含私钥和 PEM 格式证书的单个文件。)
  --cache-dir <dir>           Store the cache data in <dir>.
                              (将缓存数据存储在 <dir> 中。)
  --no-cache-dir              Disable the cache.
                              (禁用缓存。)
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index.
                              (不要定期检查 PyPI 以确定是否有新版本的 pip 可供下载。 用 --no-index 指定。)
  --no-color                  Suppress colored output.
                              (抑制彩色输出。)
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.
                              (对即将推出的不受支持的 Python 发出无声弃用警告。)
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
                              (启用可能向后不兼容的新功能。)
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.
                              (启用已弃用的功能，该功能将在未来被删除。)
```

## 升级

要是你觉得自己的pip版本有点低，想要升级一下的话，在命令行中输入以下命令

```shell
pip install --upgrade pip
```

或者是

```shell
pip install -U pip
```

## 安装某个版本的包

如果打算用pip来安装第三方的包，用的是以下的命令行

```shell
pip install package-name
```

例如我们想要安装指定版本的第三方的包，例如安装3.4.1版本的matplotlib，

```shell
pip install matplotlib==3.4.1
```

## 卸载或者是更新包

要是你打算想要卸载某个包，该要输入的命令行是

```shell
pip uninstall package_name
```

而如果打算更新某个包，对应的命令行是

```shell
pip install --upgrade package_name

# 或者是
pip install -U package_name
```

## 查看某个包的信息

可以通过以下的这个命令行来查看指定包的信息，

```shell
> pip show -f requests

Name: requests
Version: 2.24.0
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache 2.0
Location: c:\users\pc120\pycharmprojects\pythonproject1\venv\lib\site-packages
Requires: certifi, chardet, idna, urllib3
Required-by: etelemetry, gTTS, pandas-datareader, pandas-profiling, pyler, pywhatkit, pyxnat, streamlit, tushare, wikipedia, yfinance
Files:
  requests-2.24.0.dist-info\DESCRIPTION.rst
  requests-2.24.0.dist-info\INSTALLER
  .......
```

## 查看需要被升级的包

我们需要查看一下现有的这些包中，哪些是需要是被升级的，可以用下面这行命令行来查看，

```shell
> pip list -o

Package    Version Latest Type
---------- ------- ------ -----
docutils   0.15.2  0.18.1 wheel
PyYAML     5.4.1   6.0    wheel
rsa        4.7.2   4.8    wheel
setuptools 56.0.0  62.1.0 wheel
```

## 查看兼容问题

在下载安装一些标准库的时候，需要考虑到兼容问题，一些标准库的安装可能需要依赖其他的标准库，会存在版本相冲突等问题，我们先用下面这条命令行来检查一下是否会有冲突的问题存在

```shell
> pip check package_name
```

当然要是我们不指定是哪个标准库的话，会检查现在已经安装的所有包中的是否存在版本冲突等问题

```shell
> pip check

yfinance 0.1.70 has requirement requests>=2.26, but you have requests 2.24.0.
selenium 4.1.0 has requirement urllib3[secure]~=1.26, but you have urllib3 1.25.11.
```

## 指定国内源来安装

我们要是感觉到安装的速度有点慢，可以指定国内的源来安装某个包，例如

```shell
> pip install -i https://pypi.douban.com/simple/ package_name
```

国内源有

```text
清华：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/ 
豆瓣：http://pypi.douban.com/simple/
```

## 下载包但是不安装

要是我们想要下载某个包到指定的路径下，命令行如下

```shell
> pip download package_name -d "某个路径"
```

例如

```shell
> pip download requests -d "."
```

就是在当前的目录下下载requests模块以及其他所要依赖的模块

## 批量安装软件包

我们一般在看到别人的项目时，都会包含一个`requirements.txt`文件，里面包含了一些Python项目当中需要用到的第三方库

```text
antlr4-python3-runtime==4.7.2
click==8.1.3
ghp-import==2.1.0
...
```

要生成这种txt文件，需要这么来做

```shell
> pip freeze > requirements.txt
```

而如果我们需要来批量安装第三方库，在命令行中输入以下这个命令

```shell
> pip install -r requirements.txt
```
