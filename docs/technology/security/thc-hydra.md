# Hydra 九头蛇

- 创建时间: 2022年08月03日12:08:35
- github: <https://github.com/vanhauser-thc/thc-hydra>
- 原文: <https://github.com/vanhauser-thc/thc-hydra/blob/master/README>

```text
                                H Y D R A

                      (c) 2001-2022 by van Hauser / THC
             <vh@thc.org> https://github.com/vanhauser-thc/thc-hydra
       many modules were written by David (dot) Maciejak @ gmail (dot) com
                 BFG code by Jan Dlabal <dlabaljan@gmail.com>

        Licensed under AGPLv3 (see LICENSE file)

           Please do not use in military or secret service organizations,
                          or for illegal purposes.
      (This is the wish of the author and non-binding. Many people working
       in these organizations do not care for laws and ethics anyways.
            You are not one of the "good" ones if you ignore this.)

           note: no this is not meant to be a markdown doc! old school!
```

可以通过docker直接下载最新github状态的Hydra：

```shell
docker pull vanhauser/hydra
```

## 简介

正如每项密码安全研究所显示的那样，最大的安全漏洞之一是密码。

这个工具是一个概念验证代码，让研究人员和安全顾问有可能展示从远程系统获得未经授权的访问是多么容易。

**此工具仅用于法律目的！**

已经有几种登录黑客工具可用，但是，没有一种工具既不支持一种以上的攻击协议，也不支持并行连接。

它经过测试可以在 Linux、Windows/Cygwin、Solaris、FreeBSD/OpenBSD、QNX (Blackberry 10) 和 MacOS 上进行本地编译。

目前该工具支持以下协议：

Asterisk, AFP, Cisco AAA, Cisco auth, Cisco enable, CVS, Firebird, FTP,
HTTP-FORM-GET, HTTP-FORM-POST, HTTP-GET, HTTP-HEAD, HTTP-POST, HTTP-PROXY,
HTTPS-FORM-GET, HTTPS-FORM-POST, HTTPS-GET, HTTPS-HEAD, HTTPS-POST,
HTTP-Proxy, ICQ, IMAP, IRC, LDAP, MEMCACHED, MONGODB, MS-SQL, MYSQL, NCP, NNTP, Oracle Listener,
Oracle SID, Oracle, PC-Anywhere, PCNFS, POP3, POSTGRES, Radmin, RDP, Rexec, Rlogin,
Rsh, RTSP, SAP/R3, SIP, SMB, SMTP, SMTP Enum, SNMP v1+v2+v3, SOCKS5,
SSH (v1 and v2), SSHKEY, Subversion, Teamspeak (TS2), Telnet, VMware-Auth,
VNC and XMPP.

但是，新服务的模块引擎非常简单，因此在支持更多服务之前不会花费很长时间。 非常感谢您在编写、增强或修复模块方面的帮助！！ :-)

## 从哪儿获取

您始终可以在<https://github.com/vanhauser-thc/thc-hydra/releases>的项目页面上找到 hydra 的最新发布/生产版本

如果您对当前的开发状态感兴趣，公共开发存储库位于 Github：

`svn co https://github.com/vanhauser-thc/thc-hydra`

或者

`git clone https://github.com/vanhauser-thc/thc-hydra`

使用开发版本需要您自担风险。 它包含新功能和新错误。 事情可能行不通！

或者（也更容易）可以将其作为 docker 容器拉取：

```shell
docker pull vanhauser/hydra
```

## 如何编译

要配置、编译和安装 hydra，只需输入：

```shell
./configure
make
make install
```

如果你想要 ssh 模块，你必须在你的系统上设置 libssh（不是 libssh2！），从 <https://www.libssh.org> 获取它，对于 ssh v1 支持，你还需要在 cmake 命令行中的选项中添加“-DWITH_SSH1=On " 。

> **重要**: 如果你在 MacOS 上编译，那么你必须这样做——不要通过 brew 安装 libssh！

如果您使用 Ubuntu/Debian，这将安装一些可选模块所需的补充库（请注意，有些可能在您的发行版中不可用）：

```shell
apt-get install libssl-dev libssh-dev libidn11-dev libpcre3-dev \
                 libgtk2.0-dev libmysqlclient-dev libpq-dev libsvn-dev \
                 firebird-dev libmemcached-dev libgpg-error-dev \
                 libgcrypt11-dev libgcrypt20-dev
```

这将启用除 Oracle、SAP R/3、NCP 和苹果归档协议之外的所有可选模块和功能 - 您需要从供应商的网站下载和安装它们。

对于所有其他 Linux 衍生产品和基于 BSD 的系统，请使用系统软件安装程序并查找与上述命令类似的名称库。 在所有其他情况下，您必须下载所有源库并手动编译它们。

## 支持的平台

- 所有 UNIX 平台 (Linux, *BSD, Solaris, etc.)
- MacOS (基本上是一个 BSD 克隆)
- 带有 Cygwin 的 Windows（IPv4 和 IPv6）
- 基于 Linux、MacOS 或 QNX 的移动系统（例如 Android、iPhone、Blackberry 10、Zaurus、iPaq）

## 如何使用

如果您只输入 `hydra`，您将看到可用重要选项的简短摘要。

键入 `./hydra -h` 以查看所有可用的命令行选项。

请注意，不包含登录名/密码文件。 工具会自己生成它们。

但是存在默认密码列表，请使用“dpl4hydra.sh”生成列表。

对于 Linux 用户，可以使用 GTK GUI，试试 `./xhydra`

对于命令行用法，语法如下：

    对于攻击一个目标或网络，您可以使用新的 "://" 样式：

    `hydra [some command line options] PROTOCOL://TARGET:PORT/MODULE-OPTIONS`

    旧模式也可以用于这些，此外，如果您想从文本文件中指定目标，您 *必须* 使用这个：

    `hydra [some command line options] [-s PORT] TARGET PROTOCOL [MODULE-OPTIONS]`

通过命令行选项，您可以指定要尝试的登录名、密码、是否应使用 SSL、用于攻击的并行任务数量等。

PROTOCOL 是您要用于攻击的协议，例如 ftp、smtp、http-get 或许多其他可用 TARGET 是您要攻击的目标 MODULE-OPTIONS 是可选值，每个 PROTOCOL 模块都是特殊的

***第一步*** - 选择你的目标你有三个选项来指定你想要攻击的目标：

1. 命令行上的单个目标：只需将 IP 或 DNS 地址输入
2. 命令行上的网络范围：CIDR 规范，如“192.168.0.0/24”
3. 文本文件中的主机列表：每个条目一行（见下文）

***第二步*** - 选择您的协议

尽量避免使用 telnet，因为检测正确或错误的登录尝试是不可靠的。

使用端口扫描器查看目标上启用了哪些协议。

***第三步*** - 检查模块是否有可选参数

`hydra -U PROTOCOL`

例如: `hydra -U smtp`

***第四步*** - 目标端口

这是可选的，如果没有提供端口，则使用协议的默认公共端口。

如果您指定使用 SSL（“-S”选项），则默认使用 SSL 公共端口。

如果使用 “://” 表示法，如果要提供 IPv6 地址或 CIDR（“192.168.0.0/24”）表示法进行攻击，则必须使用“[” 和 “]”括号：

```text
  hydra [some command line options] <ftp://[192.168.0.0/24>]/
  hydra [some command line options] -6 smtps://[2001:db8::1]/NTLM
```

请注意，hydra 所做的一切都只是 IPv4！

如果要攻击 IPv6 地址，必须添加“-6”命令行选项。

那么所有的攻击都只是 IPv6！

如果您想通过文本文件提供目标，则不能使用 :// 符号，而是使用旧样式并仅提供协议（和模块选项）：

  `hydra [some command line options] -M targets.txt ftp`

您还可以通过在文件中的目标条目后添加 `:<port>` 来为每个目标条目提供端口，例如：

```text
foo.bar.com
target.com:21
unusual.port.com:2121
default.used.here.com
127.0.0.1
127.0.0.1:2121
```

请注意，如果要附加 IPv6 目标，则必须提供 -6 选项并且 *必须* 将 IPv6 地址放在文件中的中括号中！如下所示：

```text
foo.bar.com
target.com:21
[fe80::1%eth0]
[2001::1]
[2002::2]:8080
[2a01:24a:133:0:00:123:ff:1a]
```

## 登录和密码

对于如何使用登录名和密码进行攻击，您有很多选择使用 -l 登录名和 -p 密码，您告诉 hydra 这是唯一可以尝试的登录名和/或密码。

使用 -L 登录名 和 -P 密码，您可以为文本文件提供条目。 例如。：

``` shell
hydra -l admin -p password ftp://localhost/
hydra -L default_logins.txt -p test ftp://localhost/
hydra -l admin -P common_passwords.txt ftp://localhost/
hydra -L logins.txt -P passwords.txt ftp://localhost/
```

此外，您可以通过 “-e” 选项尝试基于登录的密码。

“-e” 选项有三个参数：

```text
s - 尝试使用密码登录
n - 尝试空密码
r - 反转登录并尝试将其作为密码
```

如果你想，例如 尝试“尝试使用密码登录”和“空密码”，在命令行中指定“-e sn”。

但除了 -p/-P 之外，还有两种尝试密码的模式：

您可以使用文本文件，其中登录名和密码对由冒号分隔，例如：

```text
admin:password
test:test
foo:bar
```

这是一个常见的默认帐户样式列表，它也是由 hydra 提供的 dpl4hydra.sh 默认帐户文件生成器生成的。

您可以使用带有 -C 选项的文本文件 - 请注意，在此模式下，您不能使用 -l/-L/-p/-P 选项（但可以使用 -e nsr）。 例子：

```shell
hydra -C default_accounts.txt ftp://localhost/
```

最后，有一个带有 -x 选项的蛮力模式（不能与 -p/-P/-C 一起使用）：

```text
-x minimum_length:maximum_length:charset
```

字符集定义是 `a` 表示小写字母，`A` 表示大写字母，`1` 表示数字，对于您提供的任何其他内容，它都是它们的真实表示。 例子：

```text
-x 1:3:a 生成长度为 1 到 3 的所有小写字母的密码
-x 2:5:/ 生成长度为 2 到 5 的密码，仅包含斜杠
-x 5:8:A1 使用大写和数字生成长度为 5 到 8 的密码
```

例子：

```shell
hydra -l ftp -x 3:3:a ftp://localhost/
```

## 特殊模块和选项

通过第三个命令行参数 (TARGET SERVICE OPTIONAL) 或 -m 命令行选项，您可以将一个选项传递给模块。

许多模块使用它，少数需要它！

要查看模块的特殊选项，请键入：

  `hydra -U <module>`

例如:

  `./hydra -U http-post-form`

特殊选项可以通过 -m 参数作为第三个命令行选项或 service://target/option 格式传递。

示例（它们都是一样的）：

```shell
./hydra -l test -p test -m PLAIN 127.0.0.1 imap
./hydra -l test -p test 127.0.0.1 imap PLAIN
./hydra -l test -p test imap://127.0.0.1/PLAIN
```

## 恢复中止/崩溃的会话

当 hydra 被 Control-C 中止、杀死或崩溃时，它会留下一个“hydra.restore”文件，其中包含恢复会话所需的所有信息。 此会话文件每 5 分钟写入一次。

> **注意**：不能将 hydra.restore 文件复制到不同的平台（例如，从小端到大端，或从 Solaris 到 AIX）

## 如何扫描/破解代理

环境变量 HYDRA_PROXY_HTTP 定义了 Web 代理（这仅适用于 http 服务！）。 以下语法是有效的：

```env
HYDRA_PROXY_HTTP="http://123.45.67.89:8080/"
HYDRA_PROXY_HTTP="http://login:password@123.45.67.89:8080/"
HYDRA_PROXY_HTTP="proxylist.txt"
```

最后一个示例是一个包含多达 64 个代理的文本文件（格式定义与其他示例相同）。

对于所有其他服务，使用 HYDRA_PROXY 变量来扫描/破解。 它使用相同的语法。 例如：

```text
HYDRA_PROXY=[connect|socks4|socks5]://[login:password@]proxy_addr:proxy_port
```

例如：

```env
HYDRA_PROXY=connect://proxy.anonymizer.com:8000
HYDRA_PROXY=socks4://auth:pw@127.0.0.1:1080
HYDRA_PROXY=socksproxylist.txt
```

## 其他提示

- 按可能性对密码文件进行排序，并使用 -u 选项更快地找到密码！
- 唯一化你的字典文件！ 这可以为您节省大量时间: -)
  - `cat words.txt | sort | uniq > dictionary.txt`
- 如果您知道目标正在使用密码策略（只允许用户选择最小长度为 6、至少包含一个字母和一个数字等的密码），请使用 hydra 软件包附带的工具 pw-inspector 减少密码列表：
  - `cat dictionary.txt | pw-inspector -m 6 -c 2 -n > passlist.txt`

## 输出结果

结果与其他信息一起输出到 stdio。 通过 -o 命令行选项，也可以将结果写入文件。 使用 -b，可以指定输出的格式。 目前，支持这些：

- `text`   - 纯文本格式
- `jsonv1` - 使用 1.x 版模式的 JSON 数据（定义如下）。
- `json`   - JSON 数据使用最新版本的 schema，目前只有版本 1。

如果使用 JSON 输出，如果在引导 Hydra 时出现严重错误，结果文件可能不是有效的JSON。

### JSON格式

这是 JSON 输出的示例。 一些字段的注释：

- `errormessages` - 一个由零个或多个字符串组成的数组，通常在 Hydra 运行结束时打印到 stderr。 文本是非常自由的形式。
- `success` - 指示 Hydra 是否正确运行且没有错误（**NOT** 如果检测到密码）。 此参数是 JSON 值 `true` 或 `false` 取决于完成。
- `quantityfound` - 发现了多少个用户名+密码组合。
- `jsonoutputversion` - 模式的版本，1.00、1.01、1.11、2.00、2.03 等。Hydra 将使版本的第二个元组始终为两位数，以使下游处理器更容易（相对于 v1.1 与 v1.10）。 次要版本是附加的，因此 1.02 将包含比 1.00 更多的字段，并且将向后兼容。 2.x 版会破坏 1.x 版输出的某些内容。

版本 1.00 示例：

```json
{
    "errormessages": [
        "[ERROR] Error Message of Something",
        "[ERROR] Another Message",
        "These are very free form"
    ],
    "generator": {
        "built": "2021-03-01 14:44:22",
        "commandline": "hydra -b jsonv1 -o results.json ... ...",
        "jsonoutputversion": "1.00",
        "server": "127.0.0.1",
        "service": "http-post-form",
        "software": "Hydra",
        "version": "v8.5"
    },
    "quantityfound": 2,
    "results": [
        {
            "host": "127.0.0.1",
            "login": "bill@example.com",
            "password": "bill",
            "port": 9999,
            "service": "http-post-form"
        },
        {
            "host": "127.0.0.1",
            "login": "joe@example.com",
            "password": "joe",
            "port": 9999,
            "service": "http-post-form"
        }
    ],
    "success": false
}
```

## 速率

通过并行化功能，这个密码破解工具可以非常快，但是它取决于协议。 最快的一般是 POP3 和 FTP。

尝试使用任务选项 (-t) 来加快速度！ 越高 - 越快 ;-) （但太高 - 它会禁用服务）

## 分析

使用包含 295 个条目的“-C FILE”在 localhost 上针对 SuSE Linux 7.2 运行（294 次尝试无效登录，1 次有效）。 每个测试都运行了 3 次（仅针对“1 项任务”一次），平均值记下。

```text
                         P A R A L L E L    T A S K S
SERVICE 1        4       8       16      32      50      64      100     128
------- --------------------------------------------------------------------
telnet  23:20    5:58    2:58    1:34    1:05    0:33    0:45*   0:25*   0:55*
ftp     45:54    11:51   5:54    3:06    1:25    0:58    0:46    0:29    0:32
pop3    92:10    27:16   13:56   6:42    2:55    1:57    1:24    1:14    0:50
imap    31:05    7:41    3:51    1:58    1:01    0:39    0:32    0:25    0:21
```

(*)

***注意***: 64 到 128 个任务的 telnet 时间可能非常不同！ 例如 有 128 个任务，运行四次导致时间在 28 到 97 秒之间！ 原因不明……

每个任务的猜测（四舍五入）：

`295    74    38    19    10    6    5    3    3`

每次连接可能的猜测（取决于服务器软件和配置）：

```text
telnet    4
   ftp    6
  pop3    1
  imap    3
```

## bugs和功能

Hydra:

如果您发现错误或编写了新模块，请给我或 David 发送电子邮件。
vh@thc.org（并在主题行中输入“反垃圾邮件”）

您应该使用 PGP 加密发往 vh@thc.org 的电子邮件：

```text
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v3.3.3 (vh@thc.org)

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
zB3yrr+vYBT0uDWmxwPjiJs=
=ytEf
-----END PGP PUBLIC KEY BLOCK-----
```
