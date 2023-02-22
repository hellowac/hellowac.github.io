# Supervisor

* 收录时间: 2022年09月20日15:30:48
* 官方文档: [Supervisor: A Process Control System](http://supervisord.org/)
* 原文参考: [Install And Configure Supervisor On Centos 7](https://fitdevops.in/install-and-configure-supervisor-on-centos-7/)

## 简介

### Supervisor 是什么

* Supervisor 是一个客户端/服务器系统，它允许其用户监视和控制类 UNIX 操作系统上的许多进程。
* 它与 launchd、daemontools 和 runit 等程序有一些相同的目标。 与其中一些程序不同，它并不意味着作为“进程 id 1”的 init 的替代品运行。
* 相反，它旨在用于控制与项目或客户相关的流程，并且旨在在启动时像任何其他程序一样启动。

### Supervisor 的组成部分

Supervisor 的组成部分如下：

**Supervisord:**

* supervisor 的服务部分被命名为 `supervisord`。
* 它负责在自己的调用中启动子程序，响应来自客户端的命令，重新启动崩溃或退出的子进程，记录其子进程的 `stdout` 和 `stderr` 输出，以及生成和处理与子进程生命周期中的点相对应的“事件”。

**Supervisorctl:**

* supervisor 的命令行客户端名为 `supervisorctl`。
* 它通过 `supervisord` 提供的类似于shell的接口提供功能。
* 通过 `supervisorctl`，用户可以连接到不同的 `supervisord` 进程（一次一个），获取受控子进程的状态，停止和启动一个 `supervisord` 的子进程，并获取一个 `supervisord` 的运行进程列表。

**Web Server:**

* 如果您针对 Internet 套接字启动 `supervisord`，则可以通过浏览器访问具有与 `supervisorctl` 相当的功能的 Web 用户界面。
* 激活配置文件的 \[inet_http_server\] 部分后，访问服务器 URL（例如 <http://localhost:9001/>），通过 Web 界面查看和控制进程状态。

**XML-RPC Interface:**

* 服务于 Web UI 的同一 HTTP 服务器提供一个 `XML-RPC` 接口，可用于询问和控制主管及其运行的程序。

### 最低要求

* Supervisor 已经过测试并且已知可以在 Linux (Ubuntu 9.10)、Mac OS X (10.4/10.5/10.6)、Solaris (10 for Intel) 和 FreeBSD 6.1 上运行。 它可能在大多数 UNIX 系统上都能正常工作。
* Supervisor 旨在在 Python 3 版本 3.4 或更高版本以及 Python 2 版本 2.7 上工作。
* Supervisor 将不会在任何版本的 Windows 下运行。

## 安装

确保您具有执行以下命令的 sudo 或 root 权限。

要在 Centos 上安装supervisor，我们需要将 `EPEL` 存储库添加到系统中，使用以下命令。

```shell
yum install epel-release -y
```

使用以下命令安装supervisor

```shell
yum install supervisor -y
```

一旦安装了supervisor包，我们需要为主管设置一个目录。

```shell
sudo mkdir /etc/supervisor
```

我们将示例supervisor配置添加到 `supervisord.conf` 文件。

```shell
echo_supervisord_conf > /etc/supervisor/supervisord.conf
```

打开 `/etc/supervisor/supervisord.conf` 文件并在 [include] 部分添加以下行

`conf.d`目录 是我们将托管所有程序的文件夹。

```shell
files=conf.d/*.conf
```

保存并关闭文件。

要在 `supervisor` 下设置程序，我们需要创建 `conf.d` 目录。

```shell
mkdir /etc/supervisor/conf.d
```

让我们启动supervisor服务。

```shell
systemctl start supervisord

# 检查服务的状态并使其在系统启动时启动，
systemctl status supervisord

systemctl enable supervisord
```

## 添加程序

* 官方文档说明参考: <http://supervisord.org/running.html#adding-a-program>
* 官方配置说明参考: <http://supervisord.org/configuration.html>

对于本教程，我们将创建 shell 脚本，我们将其配置为一个程序，因为我们希望它继续运行。

以下设置是如何将程序添加到主管并由主管管理的示例。您可以添加自己的程序。

我们要添加的脚本是监控 Linux 进程的 CPU 和内存使用情况。

我们将在 `/opt` 目录下创建 4 个文件。

创建一个名为 `cpu-top` 的文件并添加以下内容。

```bash
#！usr/bin/env bash
z=$(ps aux)
while read -r z
do
var=$var$(awk '{print "cpu_usage{process=\""$11"\", pid=\""$2"\"}", $3z}');
done <<< "$z"
curl -X POST -H "Content-Type: text/plain" --data "$var" http://localhost:9091/metrics/job/top/instance/machine
```

创建一个名为 `memory-top` 的文件并添加以下内容。

```bash
#！usr/bin/env bash
z=$(ps aux)
while read -r z
do
var=$var$(awk '{print "memory_usage{process=\""$11"\", pid=\""$2"\"}", $4z}');
done <<< "$z"
curl -X POST -H "Content-Type: text/plain" --data "$var" http://localhost:9091/metrics/job/top/instance/machine
```

我们现在创建了 2 个名为 `memory-top` 和 `cpu-top` 的文件。

我们将创建 2 个 .sh 文件（bash 脚本）以保持脚本运行。

创建一个文件 `memory.sh` 并添加以下内容

```shell
cd /opt
while sleep 1; do ./memory-top; done;
```

创建一个名为 `cpu.sh` 的文件并添加以下内容

```shell
cd /opt
while sleep 1; do ./cpu-top; done;
```

通过运行确保 bash 脚本是可执行的，

```shell
chmod +x cpu.sh && chmod +x memory.sh
chmod +x cpu-top && chmod +x memory-top
```

此时，我们将在 `/opt` 目录下有四个文件

现在我们需要在 `supervisor` 下设置一个程序来管理这些 bash 脚本。

```shell
cd /etc/supervisord.d/
```

创建一个名为 `cpu.ini` 的文件并添加以下配置。

```ini
[program:cpu]
command=sh /opt/cpu.sh
autostart=true
autorestart=true
stderr_logfile=/var/log/long.err.log
stdout_logfile=/var/log/long.out.log
```

创建一个名为 `memory.ini` 的文件并添加以下配置。

```conf
[program:memory]
command=sh /opt/memory.sh
autostart=true
autorestart=true
stderr_logfile=/var/log/long.err.log
stdout_logfile=/var/log/long.out.log
```

保存并关闭文件。

我们需要运行以下命令让主管重新读取配置文件并应用最新的更改。

```shell
supervisorctl reread

supervisorctl update
```

要运行supervisor客户端，请运行

```shell
supervisorctl
```

要检查进程的状态，运行

```shell
status
```

您应该得到以下响应。

```shell
supervisor> status
cpu                              RUNNING   pid 12042, uptime 0:00:09
memory                           RUNNING   pid 12043, uptime 0:00:09
```

我们还可以通过 linux bash 来运行`status`检查程序的状态，

```shell
supervisorctl status
```

我们可以从supervisor客户端管理每个程序。

现在 bash 脚本将继续收集顶级运行的 Linux 进程的 CPU 和内存使用情况。

这些脚本将由supervisor服务管理。

要列出主管客户端的所有可用命令，

```shell
(venv) [root@ch1 opt]# supervisorctl
supervisor> help

default commands (type help <topic>):
=====================================
add    exit      open  reload  restart   start   tail
avail  fg        pid   remove  shutdown  status  update
clear  maintail  quit  reread  signal    stop    version

supervisor>
```

我们可以通过运行命令来管理每个程序

```shell
command programname
```

```shell
supervisor> version
3.4.0
supervisor> tail memory stderr
   0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0curl: (7) Failed connect to localhost:9091; 拒绝连接
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
curl: (7) Failed connect to localhost:9091; 拒绝连接
supervisor> tail cpu stderr
   0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
curl: (7) Failed connect to localhost:9091; 拒绝连接
```

## 配置supervisor Webserver 客户端

要允许访问 supervisord webserver，请打开 `/etc/supervisord.conf` 文件并转到 \[inet_http_server\] 部分。

取消注释所有四行并如下所示进行配置。

```ini
[inet_http_server]
port=*:9001
username=give_username
password=give_password
```

不要忘记将 `give_username` 和 `give_password` 替换为所需的凭据。

保存并关闭文件。

我们需要重新启动 supervisord 服务才能使更改生效。

```shell
systemctl restart supervisord
```

我们可以使用服务器的ip地址和端口9001访问supervisor webservice接口。

```shell
http://IPaddress:9001
```

一旦通过身份验证，它将询问用户名和密码。

您将看到以下屏幕。

![11](https://cdn.shortpixel.ai/client/q_lossless,ret_img,w_790,h_202/https://fitdevops.in/wp-content/uploads/Screenshot-from-2020-06-22-20-37-12.png)

从这个界面我们可以管理程序。

## 总结

我们已经在 Centos 上成功安装和配置了 supervisor，并且我们已经学会了使用 supervisor 服务来管理程序。

希望对您有所帮助。请查看我的其他文章。

* [Top 24 Docker Commands Explained With Examples](https://fitdevops.in/top-24-docker-commands-explained-with-examples/)
* [Launch ECS Cluster Using AWS Console](https://fitdevops.in/how-to-launch-ecs-cluster-using-aws-console/)
* [Setup Memcached Cluster In AWS](https://fitdevops.in/how-to-setup-memcached-cluster-in-aws/)
* [Audit AWS Resources Using AWS Config](https://fitdevops.in/audit-aws-resources-using-aws-config/)
* [Create Elasticsearch Cluster In AWS](https://fitdevops.in/create-elasticsearch-cluster-in-aws/)
