# 最优秀的蜜罐列表 [![Awesome Honeypots](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome){target="_blank"}

优秀的蜜罐、组件等等相关的工具列表，分为 Web、服务等多个类别，重点放在开源项目上

每个类别中没有顺序，按照提交的先后顺序排列，如果您也想提交，请阅读 [指南](CONTRIBUTING.md){target="_blank"}.

探索更多优秀的列表请参阅：[sindresorhus/awesome](https://github.com/sindresorhus/awesome){target="_blank"}.

翻译自: <https://github.com/paralax/awesome-honeypots/blob/master/README_CN.md>{target="_blank"}

## 相关列表

- [awesome-pcaptools](https://github.com/caesar0301/awesome-pcaptools){target="_blank"} 网络流量分析
- [awesome-malware-analysis](https://github.com/rshipp/awesome-malware-analysis){target="_blank"} 与上表有些重复，更侧重恶意软件分析

## 蜜罐

- 数据库蜜罐
    - [Delilah](https://github.com/SecurityTW/delilah){target="_blank"} - Python 编写的 Elasticsearch 蜜罐
    - [ESPot](https://github.com/mycert/ESPot){target="_blank"} - 一个用 NodeJS 编写的 Elasticsearch 蜜罐，用于对 CVE-2014-3120 的利用
    - [Elastic honey](https://github.com/jordan-wright/elastichoney){target="_blank"} - 简单的 Elasticsearch 蜜罐
    - [MongoDB-HoneyProxy](https://github.com/Plazmaz/MongoDB-HoneyProxy){target="_blank"} - MongoDB 蜜罐代理
    - [NoSQLpot](https://github.com/torque59/nosqlpot){target="_blank"} - NoSQL 蜜罐框架
    - [mysql-honeypotd](https://github.com/sjinks/mysql-honeypotd){target="_blank"} - C 编写的低交互 MySQL 蜜罐
    - [MysqlPot](https://github.com/schmalle/MysqlPot){target="_blank"} - MySQL 蜜罐
    - [pghoney](https://github.com/betheroot/pghoney){target="_blank"} - 低交互 Postgres 蜜罐
    - [sticky_elephant](https://github.com/betheroot/sticky_elephant){target="_blank"} - 中交互 postgresql 蜜罐

- Web 蜜罐
    - [Express honeypot](https://github.com/christophe77/express-honeypot){target="_blank"} - 使用 nodeJS 和 express 实现的 RFI & LFI 蜜罐
    - [EoHoneypotBundle](https://github.com/eymengunay/EoHoneypotBundle){target="_blank"} - Symfony2 类型的蜜罐
    - [Glastopf](https://github.com/mushorg/glastopf){target="_blank"} - Web 应用蜜罐
    - [Google Hack Honeypot](http://ghh.sourceforge.net){target="_blank"} - 旨在提供针对那些使用搜索引擎探测资源的攻击者的侦察
    - [HellPot](https://github.com/yunginnanet/HellPot){target="_blank"} - 试图让请求位置的 Bot 和客户端崩溃的蜜罐
    - [Laravel Application Honeypot](https://github.com/msurguy/Honeypot){target="_blank"} - Honeypot - Laravel 应用程序的简单垃圾邮件预防软件包
    - [Nodepot](https://github.com/schmalle/Nodepot){target="_blank"} - NodeJS Web 应用蜜罐
    - [PasitheaHoneypot](https://github.com/Marist-Innovation-Lab/PasitheaHoneypot){target="_blank"} - RestAPI 蜜罐
    - [Servletpot](https://github.com/schmalle/servletpot){target="_blank"} - Web 应用蜜罐
    - [Shadow Daemon](https://shadowd.zecure.org/overview/introduction/){target="_blank"} - 用于 PHP、Perl 和 Python 应用程序的模块化Web应用程序防火墙/高交互式蜜罐
    - [StrutsHoneypot](https://github.com/Cymmetria/StrutsHoneypot){target="_blank"} - 基于 Struts Apache 2 的蜜罐
    - [WebTrap](https://github.com/IllusiveNetworks-Labs/WebTrap){target="_blank"} - 旨在创建欺骗性网页，重定向到真实网站
    - [basic-auth-pot (bap)](https://github.com/bjeborn/basic-auth-pot){target="_blank"} bap - HTTP 基本认证蜜罐
    - [bwpot](https://github.com/graneed/bwpot){target="_blank"} - Web 应用蜜罐
    - [django-admin-honeypot](https://github.com/dmpayton/django-admin-honeypot){target="_blank"} - 虚假的 Django 管理登录页面，记录未经授权的访问尝试
    - [drupo](https://github.com/d1str0/drupot){target="_blank"} - Drupal 蜜罐
    - [honeyhttpd](https://github.com/bocajspear1/honeyhttpd){target="_blank"} - 基于 Python 的 Web 服务器蜜罐构建工具
    - [honeyup](https://github.com/LogoiLab/honeyup){target="_blank"} - 模拟不安全网站的 Web 蜜罐
    - [owa-honeypot](https://github.com/joda32/owa-honeypot){target="_blank"} - 基于 Flask 的 Outlook Web 蜜罐
    - [phpmyadmin_honeypot](https://github.com/gfoss/phpmyadmin_honeypot){target="_blank"} - - 简单有效的 phpMyAdmin 蜜罐
    - [shockpot](https://github.com/threatstream/shockpot){target="_blank"} - 检测 Shell Shock 利用尝试的 Web 应用蜜罐
    - [smart-honeypot](https://github.com/freak3dot/smart-honeypot){target="_blank"} - PHP 脚本编写的智能蜜罐
    - Snare/Tanner - Glastopf 的后继者
      - [Snare](https://github.com/mushorg/snare){target="_blank"} - 下一代高交互 honEypot
      - [Tanner](https://github.com/mushorg/tanner){target="_blank"} - 评估 SNARE 事件
    - [stack-honeypot](https://github.com/CHH/stack-honeypot){target="_blank"} - 将针对垃圾邮件机器人的陷阱插入到响应中
    - [tomcat-manager-honeypot](https://github.com/helospark/tomcat-manager-honeypot){target="_blank"} - Tomcat 蜜罐。记录请求并保存攻击者的 WAR 文件
    - WordPress honeypots
        - [HonnyPotter](https://github.com/MartinIngesen/HonnyPotter){target="_blank"} - WordPress 的登录蜜罐，用于收集和分析失败的登录尝试
        - [HoneyPress](https://github.com/kungfuguapo/HoneyPress){target="_blank"} - Docker 容器中基于 Python 的 WordPress 蜜罐
        - [wp-smart-honeypot](https://github.com/freak3dot/wp-smart-honeypot){target="_blank"} - 减少垃圾邮件的 WordPress 插件
        - [wordpot](https://github.com/gbrindisi/wordpot){target="_blank"} - WordPress 蜜罐

- 服务蜜罐
    - [ADBHoney](https://github.com/huuck/ADBHoney){target="_blank"} - 安卓低交互蜜罐.
    - [AMTHoneypot](https://github.com/packetflare/amthoneypot){target="_blank"} - 针对 Intel 的 AMT 固件漏洞（CVE-2017-5689）的蜜罐
    - [DolosHoneypot](https://github.com/Marist-Innovation-Lab/DolosHoneypot){target="_blank"} - SDN 蜜罐
    - [Ensnare](https://github.com/ahoernecke/ensnare){target="_blank"} - 易部署的 Ruby 蜜罐
    - [HoneyPy](https://github.com/foospidy/HoneyPy){target="_blank"} - 低交互蜜罐
    - [Honeygrove](https://github.com/UHH-ISS/honeygrove){target="_blank"} - 基于 Twisted 的多用途、模块化蜜罐
    - [Honeyport](https://github.com/securitygeneration/Honeyport){target="_blank"} - Bash 和 Python 写成的简单 honeyport
    - [Honeyprint](https://github.com/glaslos/honeyprint){target="_blank"} - 打印机蜜罐
    - [Lyrebird](https://hub.docker.com/r/lyrebird/honeypot-base/){target="_blank"} - 现代高交互蜜罐框架
    - [MICROS honeypot](https://github.com/Cymmetria/micros_honeypot){target="_blank"} - 在带有 Oracle Hospitality Simphony 的 Oracle Hospitality Applications (MICROS) 中检测 CVE-2018-2636 的低交互蜜罐
    - [RDPy](https://github.com/citronneur/rdpy){target="_blank"} - Python 实现的 RDP 蜜罐
    - [SMB Honeypot](https://github.com/r0hi7/HoneySMB){target="_blank"} -  可以捕获类似 Wannacry 的恶意软件的高交互 SMB 蜜罐
    - [Tom's Honeypot](https://github.com/inguardians/toms_honeypot){target="_blank"} - 低交互 Python 蜜罐
    - [WebLogic honeypot](https://github.com/Cymmetria/weblogic_honeypot){target="_blank"} - 在带有 Oracle WebLogic Server 的 Oracle Fusion Middleware 中检测 CVE-2017-10271 的低交互蜜罐
    - [WhiteFace Honeypot](https://github.com/csirtgadgets/csirtg-honeypot){target="_blank"} - 基于 Twisted 开发的针对 WhiteFace 蜜罐
    - [dhp](https://github.com/ciscocsirt/dhp){target="_blank"} - 模拟 Docker HTTP API 的 Docker 蜜罐
    - [honeycomb_plugins](https://github.com/Cymmetria/honeycomb_plugins){target="_blank"} - Honeycomb 插件仓库，Cymmetria 的蜜罐框架
    - [honeyntp](https://github.com/fygrave/honeyntp){target="_blank"} - NTP 蜜罐
    - [honeypot-camera](https://github.com/alexbredo/honeypot-camera){target="_blank"} - 相机蜜罐
    - [honeypot-ftp](https://github.com/alexbredo/honeypot-ftp){target="_blank"} - FTP 蜜罐
    - [honeytrap](https://github.com/honeytrap/honeytrap){target="_blank"} - 用 Go 编写的高级蜜罐框架，可以连接其他蜜罐
    - [pyrdp](https://github.com/gosecure/pyrdp){target="_blank"} - Python 3 实现的 RDP 中间人库，能监视连接
    - [troje](https://github.com/dutchcoders/troje/){target="_blank"} - 围绕 LXC 容器的蜜罐，将每一个服务的连接都放到单独的 LXC 容器内

- 分布式蜜罐
    - [DemonHunter](https://github.com/RevengeComing/DemonHunter){target="_blank"} - 低交互蜜罐服务器

- 反蜜罐
    - [kippo_detect](https://github.com/andrew-morris/kippo_detect){target="_blank"} - 检测 Kippo 蜜罐

- ICS/SCADA 蜜罐
    - [Conpot](https://github.com/mushorg/conpot){target="_blank"} - ICS/SCADA 蜜罐
    - [GasPot](https://github.com/sjhilt/GasPot){target="_blank"} - Veeder Root Gaurdian AST, 常见于石油、天然气行业
    - [SCADA honeynet](http://scadahoneynet.sourceforge.net){target="_blank"} - 建立工业网络的蜜罐
    - [gridpot](https://github.com/sk4ld/gridpot){target="_blank"} - 模拟实际电网的开源蜜罐
    - [scada-honeynet](http://www.digitalbond.com/blog/2007/07/24/scada-honeynet-article-in-infragard-publication/){target="_blank"} - 模拟流行的 PLC 服务，更好地帮助 SCADA 研究人员了解暴露的控制系统设备的潜在风险

- 其他/随机
    - [DSHP](https://github.com/naorlivne/dshp){target="_blank"} - 带有插件化支持的简单蜜罐
    - [NOVA](https://github.com/DataSoft/Nova){target="_blank"} 看起来像完整系统的蜜罐
    - [OpenFlow Honeypot（OFPot）](https://github.com/upa/ofpot){target="_blank"} - 基于 POX 的 OpenFlow 蜜罐，将未使用的IP地址的流量重定向到蜜罐中
    - [OpenCanary](https://pypi.org/project/opencanary/){target="_blank"} - 模块化、分布式蜜罐
    - [ciscoasa_honeypot](https://github.com/cymmetria/ciscoasa_honeypot){target="_blank"} 用于思科 ASA 低交互蜜罐，检测 CVE-2018-0101 远程代码执行漏洞
    - [miniprint](https://github.com/sa7mon/miniprint){target="_blank"} - 打印机中交互蜜罐

- 僵尸网络 C&C 工具
    - [Hale](https://github.com/pjlantz/Hale){target="_blank"} - 僵尸网络 C&C 监视器
    - [dnsMole](https://code.google.com/archive/p/dns-mole/){target="_blank"} - 分析 DNS 流量，检测潜在的僵尸网络 C&C 服务器和受感染的主机

- IPv6 攻击检测工具
    - [ipv6-attack-detector](https://github.com/mzweilin/ipv6-attack-detector/){target="_blank"}  - Honeynet 项目支持的 Googel Summer of Code 2012 项目

- 动态代码检查工具包
    - [Frida](https://www.frida.re){target="_blank"} - 注入 JavaScript 来探索Windows、Mac、Linux、iOS 和 Android 上的应用程序

- 将网站转换为服务器蜜罐
    - [HIHAT](http://hihat.sourceforge.net/){target="_blank"} - 将任意 PHP 页面转换成基于 Web 的高交互蜜罐

- 恶意软件收集
    - [Kippo-Malware](https://bruteforcelab.com/kippo-malware){target="_blank"} - 用于在 Kippo SSH 蜜罐数据库中记录的 URL 上下载恶恶意文件的 Python 脚本

- 分布式传感器部署
    - [Community Honey Network](https://communityhoneynetwork.readthedocs.io/en/stable/){target="_blank"} - CHN 旨在使部署蜜罐和蜜罐管理变得简单灵活，默认使用 Docker Compose 和 Docker 进行部署
    - [Modern Honey Network](https://github.com/threatstream/mhn){target="_blank"} - 分布式 Snort 与蜜罐传感器管理，使用虚拟网络，最小指纹的 SNORT 安装，服务器提供隐形侦察与集中管理

- 网络分析工具
    - [Tracexploit](https://code.google.com/archive/p/tracexploit/){target="_blank"} - 重放网络数据包

- 日志匿名工具
    - [LogAnon](http://code.google.com/archive/p/loganon/){target="_blank"} - 日志匿名库

- 低交互蜜罐（路由器后门）
    - [Honeypot-32764](https://github.com/knalli/honeypot-for-tcp-32764){target="_blank"} - 路由器后门蜜罐(TCP 32764).
    - [WAPot](https://github.com/lcashdol/WAPot){target="_blank"} - 能够观察家庭路由器流量的蜜罐

- 蜜罐流量重定向
  - [Honeymole](https://web.archive.org/web/20100326040550/http://www.honeynet.org.pt:80/index.php/HoneyMole){target="_blank"} - 部署多个传感器回传流量到集中蜜罐中的工具

- HTTPS 代理
    - [mitmproxy](https://mitmproxy.org/){target="_blank"} - 拦截、检查、修改、重放流量

- 系统插桩
    - [Sysdig](https://sysdig.com/opensource/){target="_blank"} - 捕获 Linux 系统的状态与活动，可以进行保存、过滤与分析的开源系统级探索工具
    - [Fibratus](https://github.com/rabbitstack/fibratus){target="_blank"} - 用于探索和跟踪 Windows 内核的工具

- 检测 USB 恶意传播的蜜罐
    - [Ghost-usb](https://github.com/honeynet/ghost-usb-honeypot){target="_blank"} - 检测通过 USB 存储设备传播恶意软件的蜜罐

- 数据采集
    - [Kippo2MySQL](https://bruteforcelab.com/kippo2mysql){target="_blank"} - 从 Kippo 的日志文件中提取一些基本的统计信息插入到数据库中
    - [Kippo2ElasticSearch](https://bruteforcelab.com/kippo2elasticsearch){target="_blank"} - 用于将 Kippo SSH 蜜罐数据从 MySQL 数据库传输到 ElasticSearch 实例（服务器或集群）的 Python 脚本

- 被动网络审计框架解析工具
    - [Passive Network Audit Framework（pnaf）](https://github.com/jusafing/pnaf){target="_blank"} - 被动网络审计框架

- 虚拟机监控工具
    - [Antivmdetect](https://github.com/nsmfoo/antivmdetection){target="_blank"} - 用于创建 VirtualBox 虚拟机模版的脚本，使检测虚拟机更困难
    - [VMCloak](https://github.com/hatching/vmcloak){target="_blank"} - Cuckoo 沙盒的自动虚拟机生成和隐藏
    - [vmitools](http://libvmi.com/){target="_blank"} - 带有 Python 接口的 C 库，可以轻松监视运行中的虚拟机的底层细节

- 二进制调试器
    - [Hexgolems - Pint Debugger Backend](https://github.com/hexgolems/pint){target="_blank"} - 一个调试器后端与 Pin 的 Lua 接口
    - [Hexgolems - Schem Debugger Frontend](https://github.com/hexgolems/schem){target="_blank"} - 一个调试器前端

- 移动应用分析工具
    - [Androguard](https://github.com/androguard/androguard){target="_blank"} - 安卓应用程序逆向工程工具
    - [APKinspector](https://github.com/honeynet/apkinspector/){target="_blank"} - 带有界面的安卓应用程序分析工具

- 低交互蜜罐
    - [Honeyperl](https://sourceforge.net/projects/honeyperl/){target="_blank"} - 基于 Perl 的蜜罐，有很多插件
    - [T-Pot](https://github.com/dtag-dev-sec/tpotce){target="_blank"} - 为电信服务商 T-Mobile 提供的蜜罐

- 蜜罐数据融合
    - [HFlow2](https://projects.honeynet.org/hflow){target="_blank"} - 用于蜜罐/网络分析的数据融合工具

- 服务器
    - [Amun](http://amunhoney.sourceforge.net){target="_blank"} - 漏洞模拟蜜罐
    - [Artillery](https://github.com/trustedsec/artillery/){target="_blank"} - 开源蓝队工具，旨在通过多种办法保护 Linux 和 Windows 操作系统
    - [Bait and Switch](http://baitnswitch.sourceforge.net){target="_blank"} - 将恶意流量重定向到生产系统镜像的蜜罐
    - [Bifrozt](https://github.com/Ziemeck/bifrozt-ansible){target="_blank"} - 自动部署带有 ansible 的 bifrozt
    - [Conpot](http://conpot.org/){target="_blank"} - 低交互的工业控制系统蜜罐
    - [Heralding](https://github.com/johnnykv/heralding){target="_blank"} - 捕获凭据的蜜罐
    - [HoneyWRT](https://github.com/CanadianJeff/honeywrt){target="_blank"} - 基于 Python 的低交互蜜罐，旨在模拟攻击者可能攻击的服务或端口
    - [Honeyd](https://github.com/provos/honeyd){target="_blank"} 请查看[更多 honeyd 工具](#honeyd)
    - [Honeysink](http://www.honeynet.org/node/773){target="_blank"} - 开源网络陷阱，提供了检测与阻止指定网络上恶意流量的机制
    - [Hontel](https://github.com/stamparm/hontel){target="_blank"} - Telnet 蜜罐
    - [KFSensor](http://www.keyfocus.net/kfsensor/){target="_blank"} - 基于 Windows 的入侵检测系统蜜罐
    - [LaBrea](http://labrea.sourceforge.net/labrea-info.html){target="_blank"} - 接管未使用的 IP 地址，创建对蠕虫、黑客有吸引力的虚拟服务
    - [MTPot](https://github.com/Cymmetria/MTPot){target="_blank"} - 专注于 Mirai 的开源 Telnet 蜜罐
    - [SIREN](https://github.com/blaverick62/SIREN){target="_blank"} - 半智能蜜罐网络 - 蜜网只能虚拟环境
    - [TelnetHoney](https://github.com/balte/TelnetHoney){target="_blank"} - 简单的 telnet 蜜罐
    - [UDPot Honeypot](https://github.com/jekil/UDPot){target="_blank"} - 简单 UDP / DNS 蜜罐脚本
    - [Yet Another Fake Honeypot (YAFH)](https://github.com/fnzv/YAFH){target="_blank"} - 使用 Go 编写的简单蜜罐
    - [arctic-swallow](https://github.com/ajackal/arctic-swallow){target="_blank"} - 低交互蜜罐
    - [fapro](https://github.com/fofapro/fapro){target="_blank"} - 虚假协议服务器
    - [glutton](https://github.com/mushorg/glutton){target="_blank"} - 可喂食蜜罐
    - [go-HoneyPot](https://github.com/Mojachieee/go-HoneyPot){target="_blank"} - 使用 Go 编写的蜜罐
    - [go-emulators](https://github.com/kingtuna/go-emulators){target="_blank"} - Go 蜜罐模拟器
    - [honeymail](https://github.com/sec51/honeymail){target="_blank"} - 使用 Go 编写的 SMTP 蜜罐
    - [honeytrap](https://github.com/tillmannw/honeytrap){target="_blank"} - 一个用于捕获针对 TCP 和 UDP 服务攻击的低交互蜜罐
    - [imap-honey](https://github.com/yvesago/imap-honey){target="_blank"} - 使用 Go 编写的 IMAP 蜜罐
    - [mwcollectd](https://www.openhub.net/p/mwcollectd){target="_blank"} - 联合 nepenthes 和 honeytrap 的最佳功能实现的多功能恶意软件收集蜜罐
    - [potd](https://github.com/lnslbrty/potd){target="_blank"} - 使用 Linux 的 Namespaces、Seccomp 与 Capabilities 构建针对 OpenWrt/IoT 设备的低中交互 SSH/TCP 蜜罐
    - [portlurker](https://github.com/bartnv/portlurker){target="_blank"} - 用于协议猜测和安全字符显示的端口监听工具/蜜罐
    - [slipm-honeypot](https://github.com/rshipp/slipm-honeypot){target="_blank"} - 简单的低交互端口监听蜜罐
    - [telnet-iot-honeypot](https://github.com/Phype/telnet-iot-honeypot){target="_blank"} - 为了捕获僵尸网络二进制文件，使用 Python 编写的 telnet 蜜罐
    - [telnetlogger](https://github.com/robertdavidgraham/telnetlogger){target="_blank"} - 跟踪 Mirai 的 Telnet 蜜罐
    - [vnclowpot](https://github.com/magisterquis/vnclowpot){target="_blank"} - 低交互的 VNC 蜜罐

- IDS 签名生成
    - [Honeycomb](http://www.icir.org/christian/honeycomb/){target="_blank"} - 使用蜜罐自动创建签名

- 查找服务提供商的 ASN 与前缀
    - [CC2ASN](http://www.cc2asn.com/){target="_blank"} - 属于世界上任何给定国家的 AS 编号和前缀的查询服务

- 数据收集/数据共享
    - [HPfriends](http://hpfriends.honeycloud.net/#/home){target="_blank"} - 蜜罐数据共享平台
        - [hpfriends](https://heipei.io/sigint-hpfriends/){target="_blank"} - 关于 HPFriends feed 系统的介绍
    - [HPFeeds](https://github.com/rep/hpfeeds/){target="_blank"} - 轻量认证的订阅发布协议

- 集中管理工具
    - [PHARM](http://www.nepenthespharm.com/){target="_blank"} - 管理、统计、分析你的分布式 Nepenthes 蜜罐

- 网络连接分析工具
    - [Impost](http://impost.sourceforge.net/){target="_blank"} - 网络安全审计工具，用于取证分析被破坏/易受攻击的守护进程

- 蜜罐部署
    - [Modern Honeynet Network](http://threatstream.github.io/mhn/){target="_blank"} - 让蜜罐的管理与部署更简单

- Wireshark 的蜜罐扩展
    - [Wireshark Extensions](https://www.honeynet.org/project/WiresharkExtensions){target="_blank"} - 支持应用针对 PCAP 文件的 Snort IDS 规则与签名

- 客户端蜜罐
    - [CWSandbox / GFI Sandbox](https://www.gfi.com/products-and-solutions/all-products){target="_blank"}
    - [Capture-HPC-Linux](https://redmine.honeynet.org/projects/linux-capture-hpc/wiki){target="_blank"}
    - [Capture-HPC-NG](https://github.com/CERT-Polska/HSN-Capture-HPC-NG){target="_blank"}
    - [Capture-HPC](https://projects.honeynet.org/capture-hpc){target="_blank"} - 高交互客户端蜜罐
    - [HoneyBOT](http://www.atomicsoftwaresolutions.com/){target="_blank"}
    - [HoneyC](https://projects.honeynet.org/honeyc){target="_blank"}
    - [HoneySpider Network](https://github.com/CERT-Polska/hsn2-bundle){target="_blank"} - 集成多个客户端蜜罐检测恶意网站的可扩展系统
    - [HoneyWeb](https://code.google.com/archive/p/gsoc-honeyweb/){target="_blank"} - 为管理与远程共享 Honeyclients 资源而创建的 Web 界面
    - [Jsunpack-n](https://github.com/urule99/jsunpack-n){target="_blank"}
    - [MonkeySpider](http://monkeyspider.sourceforge.net){target="_blank"}
    - [PhoneyC](https://github.com/honeynet/phoneyc){target="_blank"}
    - [Pwnypot](https://github.com/shjalayeri/pwnypot){target="_blank"} - 高交互客户端蜜罐
    - [Rumal](https://github.com/thugs-rumal/){target="_blank"}
    - [Shelia](https://www.cs.vu.nl/~herbertb/misc/shelia/){target="_blank"}
    - [Thug](https://buffer.github.io/thug/){target="_blank"}
    - [Thug Distributed Task Queuing](https://thug-distributed.readthedocs.io/en/latest/index.html){target="_blank"}
    - [Trigona](https://www.honeynet.org/project/Trigona){target="_blank"}
    - [URLQuery](https://urlquery.net/){target="_blank"}
    - [YALIH (Yet Another Low Interaction Honeyclient)](https://github.com/Masood-M/yalih){target="_blank"} - 低交互客户端蜜罐，旨在通过签名，异常和模式匹配技术检测恶意网站

- 蜜罐
    - [Deception Toolkit](http://www.all.net/dtk/dtk.html){target="_blank"}
    - [IMHoneypot](https://github.com/mushorg/imhoneypot){target="_blank"}

- PDF 文档检查工具
    - [peepdf](https://github.com/jesparza/peepdf){target="_blank"}

- 混合低/高交互蜜罐
    - [HoneyBrid](http://honeybrid.sourceforge.net){target="_blank"}

- SSH 蜜罐
    - [Blacknet](https://github.com/morian/blacknet){target="_blank"} - SSH 蜜罐系统
    - [Cowrie](https://github.com/cowrie/cowrie){target="_blank"} - Cowrie SSH 蜜罐 (基于 kippo)
    - [DShield docker](https://github.com/xme/dshield-docker){target="_blank"} - 启用了 DShield 输出的 Docker 容器
    - [HonSSH](https://github.com/tnich/honssh){target="_blank"} - 记录客户端与服务器之间所有 SSH 通信
    - [HUDINX](https://github.com/Cryptix720/HUDINX){target="_blank"} - 用于记录暴力破解的低交互 SSH 蜜罐，记录攻击者全部 Shell 交互
    - [Kippo](https://github.com/desaster/kippo){target="_blank"} - 中交互 SSH 蜜罐
    - [Kippo_JunOS](https://github.com/gregcmartin/Kippo_JunOS){target="_blank"} - 基于 Kippo 的蜜罐
    - [Kojoney2](https://github.com/madirish/kojoney2){target="_blank"} - Jose Antonio Coret 使用 Python 编写，基于 Kojoney 的低交互 SSH 蜜罐
    - [Kojoney](http://kojoney.sourceforge.net/){target="_blank"} - 基于 Python 的低交互蜜罐，使用 Twisted Conch 模拟 SSH 服务
    - [Longitudinal Analysis of SSH Cowrie Honeypot Logs](https://github.com/deroux/longitudinal-analysis-cowrie){target="_blank"} - 基于 Python 的命令行工具，用于分析一段时间内的 cowrie 日志
    - [LongTail Log Analysis @ Marist College](http://longtail.it.marist.edu/honey/){target="_blank"} - 分析 SSH 蜜罐日志
    - [Malbait](https://github.com/batchmcnulty/Malbait){target="_blank"} - 使用 Perl 实现的 TCP/UDP 蜜罐
    - [MockSSH](https://github.com/ncouture/MockSSH){target="_blank"} - 支持定义的所有命令的 SSH 服务器
    - [cowrie2neo](https://github.com/xlfe/cowrie2neo){target="_blank"} - 解析 cowrie 蜜罐日志到 neo4j 数据库
    - [go-sshoney](https://github.com/ashmckenzie/go-sshoney){target="_blank"} - SSH 蜜罐
    - [go0r](https://github.com/fzerorubigd/go0r){target="_blank"} - 使用 Go 编写的简单 SSH 蜜罐
    - [gohoney](https://github.com/PaulMaddox/gohoney){target="_blank"} - 使用 Go 编写的 SSH 蜜罐
    - [hived](https://github.com/sahilm/hived){target="_blank"} - 基于 Go 编写的蜜罐
    - [hnypots-agent)](https://github.com/joshrendek/hnypots-agent){target="_blank"} - 记录用户名和密码组合的 SSH 服务器
    - [honeypot.go](https://github.com/mdp/honeypot.go){target="_blank"} - 使用 Go 编写的 SSH 蜜罐
    - [honeyssh](https://github.com/ppacher/honeyssh){target="_blank"} - 凭据 dumping 的 SSH 蜜罐
    - [hornet](https://github.com/czardoz/hornet){target="_blank"} - 支持多虚拟主机的中交互 SSH 蜜罐
    - [ssh-auth-logger](https://github.com/JustinAzoff/ssh-auth-logger){target="_blank"} - 低\零交互 SSH 蜜罐
    - [ssh-honeypot](https://github.com/droberson/ssh-honeypot){target="_blank"} - 伪造 SSHD，记录 IP 地址、用户名与密码
    - [ssh-honeypot](https://github.com/amv42/sshd-honeypot){target="_blank"} - OpenSSH DEAMON 的改版，将命令转发到 Cowrie
    - [ssh-honeypotd](https://github.com/sjinks/ssh-honeypotd){target="_blank"} - C 编写的低交互 SSH 蜜罐
    - [sshForShits](https://github.com/traetox/sshForShits){target="_blank"} - 高交互 SSH 蜜罐框架
    - [sshesame](https://github.com/jaksi/sshesame){target="_blank"} - 记录登录活动的虚假 SSH 服务器
    - [sshhipot](https://github.com/magisterquis/sshhipot){target="_blank"} - 高交互中间人 SSH 蜜罐
    - [sshlowpot](https://github.com/magisterquis/sshlowpot){target="_blank"} - Go 编写的低交互 SSH 蜜罐
    - [sshsyrup](https://github.com/mkishere/sshsyrup){target="_blank"} - 简单的 SSH 蜜罐，捕获终端活动并上传到 asciinema.org
    - [twisted-honeypots](https://github.com/lanjelot/twisted-honeypots){target="_blank"} - 基于 Twisted 的 SSH\FTP\Telnet 的蜜罐

- 分布式传感器项目
    - [DShield Web Honeypot Project](https://sites.google.com/site/webhoneypotsite/){target="_blank"}

- PCAP 分析工具
    - [Honeysnap](https://projects.honeynet.org/honeysnap/){target="_blank"}

- 网络流量重定向工具
    - [Honeywall](https://projects.honeynet.org/honeywall/){target="_blank"}

- 混合内容的分布式蜜罐
    - [HoneyDrive](https://bruteforcelab.com/honeydrive){target="_blank"}

- 蜜罐传感器
    - [Honeeepi](https://redmine.honeynet.org/projects/honeeepi/wiki){target="_blank"} - Raspberry Pi 上一款基于定制 Raspbian 操作系统的蜜罐

- File carving
    - [TestDisk & PhotoRec](https://www.cgsecurity.org/){target="_blank"}

- Windows 可用的行为分析工具
    - [Capture BAT](https://www.honeynet.org/node/315){target="_blank"}

- Live CD
    - [DAVIX](https://www.secviz.org/node/89){target="_blank"} - DAVIX Released

- Spamtrap
    - [Mail::SMTP::Honeypot](https://metacpan.org/pod/release/MIKER/Mail-SMTP-Honeypot-0.11/Honeypot.pm){target="_blank"} - 提供标准 SMTP 服务器工具的 Perl 模块
    - [Mailoney](https://github.com/awhitehatter/mailoney){target="_blank"} - Python 编写的 SMTP 蜜罐，具有开放中继、凭据记录等功能
    - [SendMeSpamIDS.py](https://github.com/johestephan/VerySimpleHoneypot){target="_blank"} - 获得所有 IDS 和分析设备的简单 SMTP
    - [Shiva](https://github.com/shiva-spampot/shiva){target="_blank"} - 垃圾邮件蜜罐与智能分析工具
        - [Shiva The Spam Honeypot Tips And Tricks For Getting It Up And Running](https://www.pentestpartners.com/security-blog/shiva-the-spam-honeypot-tips-and-tricks-for-getting-it-up-and-running/){target="_blank"}
    - [SpamHAT](https://github.com/miguelraulb/spamhat){target="_blank"} - 垃圾邮件蜜罐工具
    - [Spamhole](http://www.spamhole.net/){target="_blank"}
    - [honeypot](https://github.com/jadb/honeypot){target="_blank"} - 蜜罐项目组非官方 PHP 的 SDK
    - [spamd](http://man.openbsd.org/cgi-bin/man.cgi?query=spamd%26apropos=0%26sektion=0%26manpath=OpenBSD+Current%26arch=i386%26format=html){target="_blank"}

- 商业蜜网
    - [Cymmetria Mazerunner](https://cymmetria.com/products/mazerunner/){target="_blank"} - 可引导攻击者远离真实目标，并创建攻击痕迹跟踪

- 服务器（蓝牙）
    - [Bluepot](https://github.com/andrewmichaelsmith/bluepot){target="_blank"}

- Android 应用程序动态分析
    - [Droidbox](https://code.google.com/archive/p/droidbox/){target="_blank"}

- Docker 化的低交互蜜罐
    - [Docker honeynet](https://github.com/sreinhardt/Docker-Honeynet){target="_blank"} - 部署与 Docker 容器中的一些蜜网工具
    - [Dockerized Thug](https://hub.docker.com/r/honeynet/thug/){target="_blank"} - 基于 [Thug](https://github.com/buffer/thug){target="_blank"} 的 Docker 蜜罐，用于分析恶意 Web 内容
    - [Dockerpot](https://github.com/mrschyte/dockerpot){target="_blank"} - 基于 Docker 的蜜罐
    - [Manuka](https://github.com/andrewmichaelsmith/manuka){target="_blank"} - 基于 Docker 的蜜罐 (Dionaea & Kippo)
    - [honey_ports](https://github.com/run41/honey_ports){target="_blank"} - 利用 Docker 进行蜜罐的部署发现端口扫描简单有效的办法
    - [mhn-core-docker](https://github.com/MattCarothers/mhn-core-docker){target="_blank"} - 在 Docker 中实现的现代蜜网核心元素

- 网络分析
    - [Quechua](https://bitbucket.org/zaccone/quechua){target="_blank"}

- SIP Server
    - [Artemnesia VoIP](http://artemisa.sourceforge.net){target="_blank"}

- IOT 蜜罐
    - [HoneyThing](https://github.com/omererdem/honeything){target="_blank"} - TR-069 蜜罐
    - [Kako](https://github.com/darkarnium/kako){target="_blank"} - 常见嵌入式设备漏洞的蜜罐

- Honeytokens
    - [CanaryTokens](https://github.com/thinkst/canarytokens){target="_blank"} - Honeytoken 生成器，Dashboard 在 [CanaryTokens.org](https://canarytokens.org/generate){target="_blank"}
    - [Honeybits](https://github.com/0x4D31/honeybits){target="_blank"} - 旨在通过在生产服务器和工作站中传播 breadcrumbs 和 honeytokens 来诱使攻击者进入蜜罐，从而提高诱捕率
    - [Honeyλ (HoneyLambda)](https://github.com/0x4D31/honeylambda){target="_blank"} - 简单的无服务器应用程序，旨在创建和监控 AWS Lambda 和 Amazon API Gateway 之上的网址 honeytokens
    - [dcept](https://github.com/secureworks/dcept){target="_blank"} - 部署、检测活动目录使用情况的 honeytokens
    - [honeyku](https://github.com/0x4D31/honeyku){target="_blank"} - 基于 Heroku 的 Web 蜜罐

## Honeyd工具

- Honeyd 插件
    - [Honeycomb](http://www.honeyd.org/tools.php){target="_blank"}

- Honeyd 查看工具
    - [Honeyview](http://honeyview.sourceforge.net/){target="_blank"}

- Honeyd 与 MySQL 的连接
    - [Honeyd2MySQL](https://bruteforcelab.com/honeyd2mysql){target="_blank"}

- Honeyd 统计数据可视化脚本
    - [Honeyd-Viz](https://bruteforcelab.com/honeyd-viz){target="_blank"}

- Honeyd 统计
    - [Honeydsum.pl](https://github.com/DataSoft/Honeyd/blob/master/scripts/misc/honeydsum-v0.3/honeydsum.pl){target="_blank"}

## 网络与行为分析

- 沙盒
    - [Argos](http://www.few.vu.nl/argos/){target="_blank"} - 用于捕获零日攻击的模拟器
    - [COMODO automated sandbox](https://help.comodo.com/topic-72-1-451-4768-.html){target="_blank"}
    - [Cuckoo](https://cuckoosandbox.org/){target="_blank"} - 领先的开源自动化恶意软件分析系统
    - [Pylibemu](https://github.com/buffer/pylibemu){target="_blank"} - Libemu Cython
    - [RFISandbox](https://monkey.org/~jose/software/rfi-sandbox/){target="_blank"} - 使用 PHP 5.x 脚本在 [funcall](https://pecl.php.net/package/funcall) 上构建的沙盒
    - [dorothy2](https://github.com/m4rco-/dorothy2){target="_blank"} - Ruby 编写的恶意软件/僵尸网络分析框架
    - [imalse](https://github.com/hbhzwj/imalse){target="_blank"} - 集成的恶意软件仿真工具与模拟工具
    - [libemu](https://github.com/buffer/libemu){target="_blank"} - Shellcode 模拟库，对 Shellcode 检测十分有用

- 沙盒即服务
    - [Hybrid Analysis](https://www.hybrid-analysis.com){target="_blank"} - 由 Payload Security 提供的免费恶意软件分析服务，可使用其独特的混合分析技术检测和分析未知威胁
    - [Joebox Cloud](https://jbxcloud.joesecurity.org/login){target="_blank"} - 确定 Windows、Android 和 Mac OS X 上的恶意文件（包括 PE、PDF、DOC、PPT、XLS、APK、URL 和 MachO）的行为，判断其是否存在可疑活动
    - [VirusTotal](https://www.virustotal.com/){target="_blank"}
    - [malwr.com](https://malwr.com/){target="_blank"} - 提供免费恶意软件分析服务与社区

## 数据分析工具

- 前端
    - [DionaeaFR](https://github.com/rubenespadas/DionaeaFR){target="_blank"} - Dionaea 蜜罐前端 Web
    - [Django-kippo](https://github.com/jedie/django-kippo){target="_blank"} - 用于 kippo SSH 蜜罐的 Django 程序
    - [Shockpot-Frontend](https://github.com/GovCERT-CZ/Shockpot-Frontend){target="_blank"} - 用于可视化 Shockpot 蜜罐中数据的脚本
    - [Tango](https://github.com/aplura/Tango){target="_blank"} - 使用 Splunk 处理蜜罐情报
    - [Wordpot-Frontend](https://github.com/GovCERT-CZ/Wordpot-Frontend){target="_blank"} - 用于可视化 Wordpot 蜜罐中数据的脚本
    - [honeyalarmg2](https://github.com/schmalle/honeyalarmg2){target="_blank"} - 用于显示蜜罐数据的简化 UI
    - [honeypotDisplay](https://github.com/Joss-Steward/honeypotDisplay){target="_blank"} - 展示 SSH 蜜罐的 Flask 网站

- 可视化
    - [Acapulco](https://github.com/hgascon/acapulco){target="_blank"} - 自动攻击群体图构建
    - [Afterglow Cloud](https://github.com/ayrus/afterglow-cloud){target="_blank"}
    - [Afterglow](http://afterglow.sourceforge.net/){target="_blank"}
    - [Glastopf Analytics](https://github.com/katkad/Glastopf-Analytics){target="_blank"} - 简单蜜罐统计
    - [HoneyMalt](https://github.com/SneakersInc/HoneyMalt){target="_blank"} - Maltego 转换映射蜜罐系统
    - [HoneyMap](https://github.com/fw42/honeymap){target="_blank"} - 显示实时 Websocket 流的 SVG 地图
    - [HoneyStats](https://sourceforge.net/projects/honeystats/){target="_blank"} - Honeynet 的统计视图
    - [HpfeedsHoneyGraph](https://github.com/yuchincheng/HpfeedsHoneyGraph){target="_blank"} - 可视化 hpfeeds 日志的程序
    - [Kippo stats](https://github.com/mfontani/kippo-stats){target="_blank"} - 为 kippo SSH 蜜罐展示数据的程序
    - [Kippo-Graph](https://bruteforcelab.com/kippo-graph){target="_blank"} - 用于可视化 Kippo 蜜罐中数据的脚本
    - [The Intelligent HoneyNet](https://github.com/jpyorre/IntelligentHoneyNet){target="_blank"} - 试图创建蜜罐中可操作信息的智能蜜网项目
    - [ovizart](https://github.com/oguzy/ovizart){target="_blank"} - 可视化网络流量分析

## 指南

- [T-Pot: 多蜜罐平台](https://dtag-dev-sec.github.io/mediator/feature/2015/03/17/concept.html){target="_blank"}
- [蜜罐 (Dionaea and kippo) 设置脚本](https://github.com/andrewmichaelsmith/honeypot-setup-script/){target="_blank"}

- 部署
    - [Dionaea and EC2 in 20 Minutes](http://andrewmichaelsmith.com/2012/03/dionaea-honeypot-on-ec2-in-20-minutes/){target="_blank"} - 在 EC2 上设置 Dionaea 的教程
    - [Using a Raspberry Pi honeypot to contribute data to DShield/ISC](https://isc.sans.edu/diary/22680){target="_blank"} - 基于 Raspberry Pi 的系统可以收集比防火墙日志更丰富的日志
    - [honeypotpi](https://github.com/free5ty1e/honeypotpi){target="_blank"} - 将 Raspberry Pi 变成 HoneyPot Pi 的脚本

- 研究论文
    - [Honeypot research papers](https://github.com/shbhmsingh72/Honeypot-Research-Papers){target="_blank"} - 研究蜜罐论文的 PDF
    - [vEYE](https://link.springer.com/article/10.1007%2Fs10115-008-0137-3){target="_blank"} - 自传播蠕虫行为痕迹的检测与分析
