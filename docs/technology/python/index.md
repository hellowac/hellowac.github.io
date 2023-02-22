# 简介

这是我整理的与`python`相关的知识和笔记

## centos 安装 Python3

原文: <https://phoenixnap.com/kb/how-to-install-python-3-centos-7>

### 从包管理器安装

包管理器中可用的最新 Python 3 版本是 `Python 3.6.8`。 对于最新的主要版本，您需要从源代码安装包。 有关如何执行此操作的说明，请参阅下一节。 如果您更喜欢安装 3.6.8 版，请按照下列步骤操作。

1、首先更新存储库：

```shell
sudo yum update -y
```

2、在继续在 CentOS 系统上安装 Python 3 之前，请确保它在包存储库中可用。 如果您有 CentOS 7.7 或更高版本，请跳至下一步。 如果您使用的是 7.7 之前的 CentOS 版本，则需要添加 IUS，这是一个 yum 存储库，提供更新的软件版本并包括 Python 3。

要添加 IUS 存储库，请使用以下命令：

```shell
sudo yum install https://repo.ius.io/ius-release-el$(rpm -E '%{rhel}').rpm
```

等待安装完成。 然后，更新存储库：

```shell
sudo yum update -y
```

> 注意: 不确定您正在运行哪个 CentOS 版本？ 有许多不同的方法可以[检查 CentOS 版本](https://phoenixnap.com/kb/how-to-check-centos-version)。

3、 通过在终端窗口中运行以下命令来安装 Python 3：

```shell
sudo yum install -y python3
```

等待安装完成。 输出应显示它已安装 python3 和所需的依赖项。

4、 验证您是否已成功安装 Python 3：

```shell
python3 --version
```

您应该会在您的 CentOS 系统上看到现在可用的 Python 3 版本。

```shell
$python3 --version

Python 3.6.8
```

### 源码编译安装

要安装 Python 的最新主要版本 3.9.6（在撰写本文时），您需要下载源代码副本并在设置时采取一些额外步骤。

1、 首先，安装所需的包和依赖项：

```shell
sudo yum groupinstall "Development Tools" -y
```

```shell
sudo yum install gcc open-ssl-devel bzip2-devel libffi-devel sqlite-devel -y
sudo yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel -y
```

2、 接下来，使用 `wget` 命令下载所需的 Python 版本。 如果您没有 wget，只需运行以下命令即可安装它：

```shell
sudo yum install wget -y
```

要下载 Python 3.9.6，请使用以下命令：

```shell
wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
```

3、解压包：

```shell
sudo tar xzf Python-3.9.6.tgz
```

4、 然后，移动到目录：

```shell
cd Python 3.9.6
```

5、 进入 Python 目录后，使用以下两个命令将源代码编译成安装包：

```shell
./configure --enable-optimizations
```

```shell
make altinstall
```

make 命令构建安装程序包。 `altinstall` 命令指示系统创建此 Python 版本的第二个安装。 没有它，系统将替换 Python 的默认版本。

6、检查 Python 版本以验证安装：

```shell
python3.9
```

系统应显示：

```shell
aaaa
```

### 总结

本指南提供了两种在 CentOS 7 上安装 Python 3 的不同方法。对于较新版本的 CentOS，请查看我们关于如何[在 CentOS 8 上安装 Python](https://phoenixnap.com/kb/install-python-on-centos-8) 的文章。

一切就绪后，您可以从一些基本脚本开始，例如在 Python 中[获取当前时间和日期](https://phoenixnap.com/kb/get-current-date-time-python)，或者使用内置方法（包括创建、打开和关闭文件）在 Python 中学习[文件处理](https://phoenixnap.com/kb/file-handling-in-python)。
