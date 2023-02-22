# Rabbitmq 消息队列服务

- 编写时间: 2022年08月26日15:21:16
- rabbitmq官方文档: <https://www.rabbitmq.com/documentation.html>
- docker hub 官方地址: <https://hub.docker.com/_/rabbitmq>
- 默认端口:
    - 5672: 通信端口
    - 15672: http管理端口

## 下载和安装

官方文档: <https://www.rabbitmq.com/download.html>

```shell
# docker 安装:
# latest RabbitMQ 3.10
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
```

## rpm安装

原文: [Install RabbitMQ Server on CentOS 7](https://www.cwiki.us/display/RabbitMQZH/Install+RabbitMQ+Server+on+CentOS+7)

### 下载地址和软件更新

Erlang 23.3.4.11 版本的下载地址，请参考链接： <https://packagecloud.io/rabbitmq/erlang/packages/el/7/erlang-23.3.4.11-1.el7.x86_64.rpm>

RabbitMQ 3.9.15 的下载地址，请参考链接：<https://www.rabbitmq.com/install-rpm.html>

使用登录上你的 CentOS 7 服务器后，首先需要查看你的服务器是否安装了 wget，如果没有安装 wget，请运行 yum install wget 进行安装。

```shell
yum install wget
```

当 wget 安装完成后，运行

```shell
yum update
```

来更新你的服务器。

### 安装 Erlang

首先你需要下载 Erlang ，然后进行安装，在上面提到的地址  <https://packagecloud.io/rabbitmq/erlang/packages/el/7/erlang-23.3.4.11-1.el7.x86_64.rpm?distro_version_id=140> 中的右侧有一个 wget 的地址。

![aa](https://www.cwiki.us/download/attachments/53969106/Erlang-download.jpg?version=1&modificationDate=1570851866000&api=v2)

你可以运行

```shell
wget --content-disposition https://packagecloud.io/rabbitmq/erlang/packages/el/7/erlang-23.3.4.11-1.el7.x86_64.rpm/download.rpm?distro_version_id=140
```

来进行下载。

当你下载到你的本地计算机后，运行命令

```shell
yum localinstall rabbitmq-server-3.9.15-1.el7.noarch.rpm
```

来安装你下载的 rpm 包。

当你安装完成后，你可以运行命令

```shell
erl -version
```

来查看你安装的 erl 版本。

在这里，你可以看到这显示的版本低 Erlang emulator 版本，与你下载的 Erlang 版本是不同的。

### 安装 RabbitMQ

运行下面的命令，将 RabbitMQ 下载到你服务器上。

```shell
wget https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.9.15/rabbitmq-server-3.9.15-1.el7.noarch.rpm
```

当你下载完成后，你需要运行下面的命令来将 Key 导入。

```shell
rpm --import https://www.rabbitmq.com/rabbitmq-release-signing-key.asc
```

使用 yum 进行本地安装，运行命令：

```shell
yum localinstall  rabbitmq-server-3.9.15-1.el7.noarch.rpm
```

当安装完成后，你可以使用命令来启动 rabbitmq 服务器：

```shell
systemctl start rabbitmq-server
```

### RabbitMQ 防火墙配置

RabbitMQ 的运行需要一系列的端口。因此你需要配置你的防火墙将下面的端口打开。

如果你使用的是 firewalld，那么请依次执行下面的命令。

打开防火墙端口：

```shell
firewall-cmd --zone=public --permanent --add-port=4369/tcp
firewall-cmd --zone=public --permanent --add-port=25672/tcp
firewall-cmd --zone=public --permanent --add-port=5671-5672/tcp
firewall-cmd --zone=public --permanent --add-port=15672/tcp
firewall-cmd --zone=public --permanent --add-port=61613-61614/tcp
firewall-cmd --zone=public --permanent --add-port=1883/tcp
firewall-cmd --zone=public --permanent --add-port=8883/tcp
```

将防火墙配置重新载入：

```shell
firewall-cmd --reload
```

绝大部分情况，当你执行完上面的命令后，你的 RabbitMQ 应该能够正常访问了。

如果你的服务器还启用了 SELinux 的话，你还需要执行下面的命令来让让 RabbitMQ 服务器能够接收发送网络数据：

```shell
setsebool -P nis_enabled 1
```

### RabbitMQ 设置自动启动

在安装完成后，我们希望 RabbitMQ 能开机自动启动。

请执行下面的命令，来让 RabbitMQ 随着计算机开机后自动启动：

```shell
systemctl enable rabbitmq-server
```

使用下面命令查看 RabbitMQ 的进程运行状态：

```shell
systemctl status rabbitmq-server
```

根据服务器的不同，会有不同的输出，我们的输出如下，表示 RabbitMQ 目前是正在运行的。

```shell
[root@vps263579 yhu]# systemctl status rabbitmq-server

● rabbitmq-server.service - RabbitMQ broker
Loaded: loaded (/usr/lib/systemd/system/rabbitmq-server.service; enabled; vendor preset: disabled)
Active: active (running) since Fri 2019-10-11 14:10:14 EDT; 9h ago
Main PID: 14895 (beam.smp)
Status: "Initialized"
CGroup: /system.slice/rabbitmq-server.service
├─14895 /usr/lib64/erlang/erts-10.3.5.6/bin/beam.smp -W w -A 64 -MBas ageffcbf -MHas ageffcbf -MBlmbcs 512 -MHlmbcs 512 -MMmcs 30 -P 1048576 -t 5000000 -stbt db -zdbbl 128000 -K true -- -root /usr/lib64/erlang -progn...
├─15123 /usr/lib64/erlang/erts-10.3.5.6/bin/epmd -daemon
├─15259 erl_child_setup 32768
├─15280 inet_gethost 4
└─15281 inet_gethost 4
```

### RabbitMQ 启用 Web 管理界面

在默认的情况下 RabbitMQ 的 Web 管理控制台是没有启用的，你需要通过下面的命令来进行启用。

安装 Web 管理界面的插件：

```shell
rabbitmq-plugins enable rabbitmq_management
```

提供 RabbitMQ 用户和对用户使用的权限进行赋权：

```shell
chown -R rabbitmq:rabbitmq /var/lib/rabbitmq/
```

分别执行下面的命令：

```shell
rabbitmqctl add_user admin StrongPassword
rabbitmqctl set_user_tags admin administrator
rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
```

针对上面命令的解释是，第一个命令创建了一个 admin 的用户，这个用户使用的密码为 StrongPassword。

你可以使用不同的用户名，在我们执行的上面的命令中，用户登录使用的密码为字符 StrongPassword，你可以将这个字符修改为其他的字符，或者你也可以登录成功后在 UI 界面中进行修改。

后面的话是针对这个用户进行赋权。

当上面命令执行成功后，你可以重启你的 RabbitMQ，然后通过浏览器进行登录。UI 界面使用的端口是 15672。因此访问的 URL 为你服务器的地址 + 15672。

<http://Your_Server_IP:15672/>

如果一切正常，你应该能够看到下面的登录界面：

![2](https://www.cwiki.us/download/attachments/53969106/Erlang-ui-login.jpg?version=1&modificationDate=1570853130000&api=v2)

如果你不能访问下面的登录界面，有可能是你的服务器防火墙。

最简单的办法是先禁用服务器的防火墙以确定所有的进程是正常运行的。

如果你登录成功后，你应该能够看到下面 RabbitMQ 的运行界面：

![3](https://www.cwiki.us/download/attachments/53969106/Erlang-ui-dashboard.jpg?version=1&modificationDate=1570853703000&api=v2)

## 消息队列模式

官方文档: <https://www.rabbitmq.com/getstarted.html>

1. 简单队列模式: <https://www.rabbitmq.com/tutorials/tutorial-one-python.html>
2. 分布式worker模式: <https://www.rabbitmq.com/tutorials/tutorial-two-python.html>
3. 发布/订阅模式: <https://www.rabbitmq.com/tutorials/tutorial-three-python.html>
4. 路由模式: <https://www.rabbitmq.com/tutorials/tutorial-four-python.html>
5. 主题模式: <https://www.rabbitmq.com/tutorials/tutorial-five-python.html>
6. RPC模式: <https://www.rabbitmq.com/tutorials/tutorial-six-python.html>
7. 自定义模式: <https://www.rabbitmq.com/tutorials/tutorial-seven-java.html>

## 用户角色管理

rabbitmq默认的用户名和密码是`guest`和`guest`,但为了安全考虑，该用户名和密码只允许本地访问，如果是远程操作的话，需要创建新的用户名和密码；

**新建用户**

```shell
# root权限
rabbitmqctl add_user username passwd  # 添加用户，后面两个参数分别是用户名和密码
rabbitmqctl set_permissions -p / username ".*" ".*" ".*"  # 添加权限
rabbitmqctl set_user_tags username administrator  # 修改用户角色,将用户设为管理员
```

**用户的角色说明**

```yaml
management: 用户可以访问管理插件
policymaker: 用户可以访问管理插件，并管理他们有权访问的vhost的策略和参数。
monitoring: 用户可以访问管理插件，查看所有连接和通道以及与节点相关的信息。
administrator: 用户可以做任何监视可以做的事情，管理用户，vhost和权限，关闭其他用户的连接，并管理所有vhost的政策和参数。
```

> 使用添加的账户远程访问后台管理站点，将原来的账号guest删除；

**用户管理命令汇总**

- 新建用户: `rabbitmqctl add_user username passwd`
- 删除用户: `rabbitmqctl delete_user username`
- 改密码: `rabbimqctl change_password {username} {newpassword}`
- 设置用户角色: `rabbitmqctl set_user_tags {username} {tag ...}`

```shell
rabbitmqctl set_permissions -p / username ".*" ".*" ".*"  # 添加权限
```

**权限说明**

```shell
rabbitmqctl set_permissions [-pvhostpath] {user} {conf} {write} {read}
```

- Vhostpath: 虚拟主机，表示该用户可以访问那台虚拟主机；
- user: 用户名。
- Conf: 一个正则表达式match哪些配置资源能够被该用户访问。
- Write: 一个正则表达式match哪些配置资源能够被该用户设置。
- Read: 一个正则表达式match哪些配置资源能够被该用户访问。

## 虚拟主机

默认的用户和队列都是在`/`虚拟机下。

```shell
# 创建一个虚拟主机
rabbitmqctl add_vhost vhost_name
# 删除一个虚拟主机
rabbitmqctl delete_vhost vhost_name
```

**常用文件路径**

- `/usr/local/rabbitmq_server/var/log/rabbitmq/rabbit@tms.log`: 记录rabbitmq运行日常的日志
- `/usr/local/rabbitmq_server/var/log/rabbitmq/rabbit@tms-sasl.log`: rabbitmq的崩溃报告
- `/usr/local/rabbitmq_server/etc/rabbitmq/rabbitmq.config`: rabbitmq的配置文件
- `/usr/local/rabbitmq_server/var/lib/rabbitmq/mnesia/rabbit@tms`: rabbit消息持久化文件

> 注意：
>
> 如果相应路径的文件不存在就自己创建，如果是使用apt安装或yum安装那么这些文件夹都被自动创建好了。

## 启用后台管理插件

通过后台管理插件我们可以动态监控mq的流量，创建用户，队列等。

```shell
# 创建目录
mkdir /etc/rabbitmq

# 启用插件
/usr/lib/rabbitmq/bin/rabbitmq-plugins enable rabbitmq_management

# 其会在/etc/rabbitmq目录下创建一个enabled_plugins文件，这是后台管理的配置文件。
```

> rabbitmq的网页管理的端口是`15672`，如果你是远程操作服务器，输入`<http://ip:15672>`,发现连接不上，因为服务器防火墙不允许这个端口远程访问；

```shell
# 将mq的tcp监听端口和网页管理端口都设置成允许远程访问

firewall-cmd --permanent --add-port=15672/tcp
firewall-cmd --permanent --add-port=5672/tcp
systemctl restart firewalld.service
```

**管理界面介绍**

```yaml
# 输入用户名密码登录后进入主界面
Overview: 用来显示流量，端口，节点等信息，以及修改配置文件；
Connections: 显示所有的TCP连接；
channels: 显示所有的信道连接；
exchanges: 显示所有的交换机以及创建删除等；
queues: 显示所有的队列以及创建删除等；
admins: 显示所有的用户以及用户管理；
```
