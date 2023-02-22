# sqlmap 数据库注入检测

- 创建时间: 2022年08月03日12:08:35
- github: <https://github.com/sqlmapproject/sqlmap>
- 原文: <https://github.com/sqlmapproject/sqlmap/blob/master/README.md>
- 中文翻译: <https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-zh-CN.md>

## 简介

sqlmap 是一个开源的渗透测试工具，可以用来自动化的检测，利用SQL注入漏洞，获取数据库服务器的权限。它具有功能强大的检测引擎,针对各种不同类型数据库的渗透测试的功能选项，包括获取数据库中存储的数据，访问操作系统文件甚至可以通过带外数据连接的方式执行操作系统命令。

## 演示截图

![sqlmap](https://camo.githubusercontent.com/e3bc69b980bc05011eaa4f570476a51f10d3d24ec39df0b19920170d44b40bcc/68747470733a2f2f7261772e6769746875622e636f6d2f77696b692f73716c6d617070726f6a6563742f73716c6d61702f696d616765732f73716c6d61705f73637265656e73686f742e706e67)

你可以访问 wiki上的 [截图](https://github.com/sqlmapproject/sqlmap/wiki/Screenshots) 查看各种用法的演示

## 安装方法

你可以点击 [这里](https://github.com/sqlmapproject/sqlmap/tarball/master) 下载最新的 tar 打包的源代码 或者点击[这里](https://github.com/sqlmapproject/sqlmap/zipball/master)下载最新的 zip 打包的源代码.

推荐你从 [Git](https://github.com/sqlmapproject/sqlmap) 仓库获取最新的源代码:

```shell
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
```

sqlmap 可以运行在 [Python](https://www.python.org/download/) 2.6, 2.7 和 3.x 版本的任何平台上

## 使用方法

通过如下命令可以查看基本的用法及命令行参数:

```shell
python sqlmap.py -h
```

通过如下的命令可以查看所有的用法及命令行参数:

```shell
python sqlmap.py -hh
```

你可以从 [这里](https://asciinema.org/a/46601) 看到一个sqlmap 的使用样例。除此以外，你还可以查看 [使用手册](https://github.com/sqlmapproject/sqlmap/wiki/Usage)。获取sqlmap所有支持的特性、参数、命令行选项开关及说明的使用帮助。

## 链接

- 项目主页: <https://sqlmap.org>
- 源代码下载: [.tar.gz](https://github.com/sqlmapproject/sqlmap/tarball/master) or [.zip](https://github.com/sqlmapproject/sqlmap/zipball/master)
- RSS 订阅: <https://github.com/sqlmapproject/sqlmap/commits/master.atom>
- Issue tracker: <https://github.com/sqlmapproject/sqlmap/issues>
- 使用手册: <https://github.com/sqlmapproject/sqlmap/wiki>
- 常见问题 (FAQ): <https://github.com/sqlmapproject/sqlmap/wiki/FAQ>
- Twitter: [@sqlmap](https://twitter.com/sqlmap)
- 教程: [https://www.youtube.com/user/inquisb/videos](https://www.youtube.com/user/inquisb/videos)
- 截图: <https://github.com/sqlmapproject/sqlmap/wiki/Screenshots>

## rest API

参考: <https://github.com/sqlmapproject/sqlmap/wiki/Usage#api-rest-json>

中文文档: <https://sqlmap.kvko.live/usage/api>

以及源码: <https://github.com/sqlmapproject/sqlmap/blob/master/sqlmapapi.py>

以及APIyaml: <https://github.com/sqlmapproject/sqlmap/blob/master/sqlmapapi.yaml>

yaml源文件地址: <https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/sqlmapapi.yaml>

使用swagger UI 查看api文档，打开: <https://petstore.swagger.io/> 然后在地址栏中输入 yaml 源文件地址即可查看文档的UI详情

可使用 <https://www.convertjson.com/yaml-to-json.htm> yaml 转 json, 将yaml格式的api转化为Json格式。
