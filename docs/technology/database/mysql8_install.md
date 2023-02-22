# centos 7 安全 mysql 8

原文: <https://www.mysqltutorial.org/install-mysql-centos/>

1、 设置 Yum 存储库

执行以下命令在 CentOS 上启用 MySQL yum 存储库：

```shell
rpm -Uvh https://repo.mysql.com/mysql80-community-release-el7-3.noarch.rpm
```

2、安装 MySQL 8 社区版服务端

由于 MySQL yum 存储库有多个 MySQL 版本的多个存储库配置，因此您需要禁用 mysql repo 文件中的所有存储库：

```shell
sed -i 's/enabled=1/enabled=0/' /etc/yum.repos.d/mysql-community.repo
```

并执行以下命令安装 MySQL 8：

```shell
yum --enablerepo=mysql80-community install mysql-community-server
```

> 可能会报GPG秘钥的错，执行: `rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2022`

3、启动mysql服务

使用此命令启动 mysql 服务：

```shell
service mysqld start
```

4、 显示 root 用户的默认密码

当您安装 MySQL 8.0 时，会授予 root 用户帐户一个临时密码。 要显示 root 用户帐户的密码，请使用以下命令：

```shell
grep "A temporary password" /var/log/mysqld.log
```

这是输出：

```shell
[Note] A temporary password is generated for root@localhost: ahJ2D)wthie=
```

请注意，您的临时密码会有所不同。 您将需要此密码来更改 root 用户帐户的密码。

5、 MySQL 安全安装

执行命令 mysql_secure_installation 来保护 MySQL 服务器：

```shell
mysql_secure_installation
```

它将提示您输入 root 帐户的当前密码：

```shell
Enter password for user root:
```

输入上面的临时密码，然后回车。 将显示以下消息：

```shell
The existing password for the user account root has expired. Please set a new password.

New password:
Re-enter new password:
```

您需要输入两次 root 帐户的新密码。 会提示一些问题，建议输入yes(y)：

```shell
Remove anonymous users? (Press y|Y for Yes, any other key for No) : y
# 移除匿名用户？ （按 y|Y 表示是，任何其他键表示否）：y

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : y
# 远程禁止root登录？ （按 y|Y 表示是，任何其他键表示否）：y

Remove test database and access to it? (Press y|Y for Yes, any other key for No) : y
# 删除测试数据库并访问它？ （按 y|Y 表示是，任何其他键表示否）：y

Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y
# 现在重新加载权限表？ （按 y|Y 表示是，任何其他键表示否）：y
```

6、重启并启用 MySQL 服务

使用以下命令重启mysql服务：

```shell
systemctl restart mysqld
```

并在系统启动时自动启动 mysql 服务：

```shell
systemctl enable mysqld
```

7、 连接到 MySQL

使用此命令连接到 MySQL 服务器：

```shell
mysql -u root -p
```

它将提示您输入 root 用户的密码。 您输入密码并按 Enter：

```shell
Enter password:
```

它将显示 mysql 命令：

```shell
mysql>
```

使用 `SHOW DATABASES` 显示当前服务器中的所有数据库：

```shell
mysql> show databases;
```

这是输出：

```shell
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.05 sec)
```
