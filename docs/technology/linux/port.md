# 端口占用查找

查看端口的占用情况、找出并杀死占用进程的方法

参考: <https://www.cnblogs.com/shoufeng/p/11308614.html>

## lsof

参考: <http://linux.51yip.com/search/lsof>{target="_blank"}

### 命令使用示例

```shell
# 命令为 lsof -i
[root@onepiece ~]# lsof -i
# 将会显示 命令 + 进程ID + 进程所属用户, 以及监听的协议、状态等信息
COMMAND     PID USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
dhclient    728 root    6u  IPv4   11262      0t0  UDP *:bootpc
ntpd        839  ntp   16u  IPv4   13671      0t0  UDP *:ntp
ntpd        839  ntp   18u  IPv4   13677      0t0  UDP localhost:ntp
```

!!! warn "若提示无此命令, 则需要安装, 命令如下:"

    ```shell
    [root@onepiece ~]# lsof -i
    -bash: lsof: command not found
    [root@onepiece ~]# yum install -y lsof
    ......
    Installed:
    lsof.x86_64 0:4.87-6.el7
    Complete!
    # 出现上述的 "Complete!"，说明安装成功。
    ```

### 查看某一端口的占用情况

```shell
# 比如查看80端口的占用情况，命令为：
[root@onepiece ~]# lsof -i:22
COMMAND  PID USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
sshd    3187 root    3u  IPv4   16278      0t0  TCP *:ssh (LISTEN)
sshd    9528 root    3u  IPv4 4436480      0t0  TCP onepiece:ssh->120.253.xx.xx:30214 (ESTABLISHED)
```

这里显示出22号端口正被sshd所使用, 状态是LISTEN(监听).

### 杀死某个端口的所有进程

!!! err ""

    不建议通过 kill 的方式解决端口冲突问题!
    
    某些极少的情况下是可以直接杀死进程、释放端口的, 比如某个 Tomcat 进程没有成功退出, 导致重启失败.

```shell
# 命令如下：
[root@onepiece ~]# killall sshd
# 这样，所有sshd的进程都会被结束掉 —— 我这里通过ssh远程操作阿里云服务器, 杀死之后将退出连接, 提示如下:
Connection to 47.52.xx.xx closed by remote host.
Connection to 47.52.xx.xx closed.
# 此时需要从阿里云控制台通过终端进入, 并开启sshd服务, 命令如下:
service sshd start
```

这样, 所有与 sshd 的相关进程都会被结束掉 —— 务必慎用.

## netstat

参考文档: <http://linux.51yip.com/search/netstat>{target="_blank"}

### 命令使用示例

```shell
# 命令示例如下：
[root@onepiece ~]# netstat -anp | grep 22
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      9646/sshd
tcp        0     36 172.31.xx.xx:22       120.253.xx.xx:30307     ESTABLISHED 9649/sshd: root@pts
unix  2      [ ]         DGRAM                    15722    476/dbus-daemon
unix  3      [ ]         STREAM     CONNECTED     11122    476/dbus-daemon      
```

可以看出22端口被9646号进程监听着.

### 查看占用某个端口的进程

```shell
# 命令为fuser：
[root@onepiece ~]# fuser -v -n tcp 22
                     USER        PID ACCESS COMMAND
22/tcp:              root       9646 F.... sshd
                     root       9649 F.... sshd
```

### 杀死某个端口的占用进程

```shell
[root@onepiece ~]# kill -s 9 9646(进程号)
```

!!! info "参数"

    `-9`参数表示告诉操作系统直接杀死进程, 无论进程的状态是否可杀死;
    
    该命令只杀死某个进程, 比 `killall` 命令相对安全一点.

## 参考资料

* [Linux中如何解除端口占用](https://blog.csdn.net/zhu_xun/article/details/16823577)
* [linux下如何搜索一个文件或程序所在位置](https://blog.csdn.net/whynotldch/article/details/78163389)
