# 无头浏览器环境搭建

## CentOS 7 上安装 Chromium

1、 首先让确保您的系统是最新的。

```shell
yum clean all
yum install -y epel-release
yum -y update
```

2、在 CentOS 7 上安装 Chromium。

要在 CentOS 7 上安装 Chromium，只需使用 yum install 命令即可：

```shell
yum install -y chromium
```

3、访问 Google Chrome 网络浏览器。

Chromium 浏览器安装完成后，您可以从 GNU 应用程序菜单或命令行终端执行以下命令来启动 Chromium：

```shell
chromium
# chromium-browser
```

更多信息参考[chromium 官方网站](https://www.chromium.org/)。

* [Testing in Chromium](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/testing/web_tests.md)
* [Running in headless mode with --ozone-platform or xvfb](https://www.chromium.org/developers/testing/running-tests/#running-in-headless-mode-with-ozone-platform-or-xvfb)

## 安装chromedriver

```shell
yum install chromedriver
```
