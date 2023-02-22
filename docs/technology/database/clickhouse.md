# clickhouse

* 官网: <https://clickhouse.com/>
* 文档: <https://clickhouse.com/docs/en/intro/>

## 常用查询

### 查询数据库表大小

```sql
SELECT
    concat(database, '.', table) AS table,
    formatReadableSize(sum(bytes)) AS size,
    sum(bytes) AS bytes_size,
    sum(rows) AS rows,
    max(modification_time) AS latest_modification,
    any(engine) AS engine
FROM system.parts
WHERE active
GROUP BY
    database,
    table
ORDER BY bytes_size DESC
```

结果:

table                               |size      |bytes_size  |rows      |latest_modification    |engine             |
------------------------------------|----------|------------|----------|-----------------------|-------------------|
system.asynchronous_metric_log      |9.02 GiB  |  9684296449|7632396946|2022-06-01 15:23:21.000|MergeTree          |
system.metric_log                   |1.66 GiB  |  1783387541|  24864079|2022-06-01 15:23:25.000|MergeTree          |
system.query_thread_log             |1.40 GiB  |  1502640094|  54269589|2022-06-01 15:22:14.000|MergeTree          |
system.query_log                    |364.15 MiB|   381840631|   2324632|2022-06-01 15:23:19.000|MergeTree          |
system.trace_log                    |43.55 MiB |    45665106|   1529712|2022-06-01 15:18:53.000|MergeTree          |

### 集群查询

参考: <https://clickhouse.com/docs/en/sql-reference/table-functions/cluster/>

```sql
SELECT 
    table,
    sum(rows) AS `rows`,
    formatReadableSize(sum(data_uncompressed_bytes)) AS `uncps_bytes`,
    formatReadableSize(sum(data_compressed_bytes)) AS `bytes`,
    round((sum(data_compressed_bytes) / sum(data_uncompressed_bytes)) * 100, 0) AS `cps_rate`
FROM cluster('rz_cluster', system.parts)
GROUP BY table
```

结果:

table                          |rows       |uncps_bytes|bytes     |cps_rate|
-------------------------------|-----------|-----------|----------|--------|
trace_log                      |    2162927|452.87 MiB |60.91 MiB |    13.0|
query_log                      |    3167006|3.95 GiB   |466.63 MiB|    12.0|
asynchronous_metric_log        |30720829855|686.76 GiB |32.01 GiB |     5.0|
dimension_process_info         |      21618|506.67 KiB |101.94 KiB|    20.0|
metric_log                     |  103575826|220.51 GiB |6.44 GiB  |     3.0|
query_thread_log               |   57482489|41.82 GiB  |1.60 GiB  |     4.0|
dimension_send_info            |         12|354.00 B   |260.00 B  |    73.0|

## Clickhouse 时区

### 默认设置

Clickhouse默认是读取操作系统的时区 我们可以通过操作系统命令和clickhouse的命令查看验证：

```shell
# clickhouse查看当前时间
Clickhouse> select now();
 
SELECT now()
 
┌───────────────now()─┐
│ 2020-07-11 23:47:56 │
└─────────────────────┘
 
1 rows in set. Elapsed: 0.003 sec. 
 
Clickhouse> exit;
Bye.

# 查看系统时间
[root@hadoop ~]# date
Sat Jul 11 23:48:01 CST 2020
 
 
# 此时操作系统的时区和时间是：
> timedatectl
      Local time: Sat 2020-07-11 23:49:06 CST
  Universal time: Sat 2020-07-11 15:49:06 UTC
        RTC time: Sat 2020-07-11 15:49:05
       Time zone: Asia/Shanghai (CST, +0800)
     NTP enabled: n/a
NTP synchronized: no
 RTC in local TZ: no
      DST active: n/a
 
# 操作系统的命令：
# timedatectl list-timezones
# list-timezones 列出系统上支持的时区
# set-timezone 设定时区
# set-time 设置时间
# set-btp 设置同步ntp
 
# 示例:设置时区示例：
# timedatec 修改时区

timedatectl set-timezone "America/New_York"
 
# timedatectl set-timezone Asia/Shanghai

# ntp设置：
yum -y install ntp 
systemctl enable ntpd 
systemctl start ntpd

# 同步时间
ntpdate -u cn.pool.ntp.org
```

### clickhouse配置

clickhouse提供了配置的参数选型：

1. 修改设置

    `sudo vim /etc/clickhouse-server/config.xml`

    `<timezone>Asia/Shanghai</timezone>`

    由于clickhouse是俄罗斯人主导开发的，默认设置为`Europe/Moscow`

2. 重启服务器：

    `sudo service clickhouse-server restart`

我们可以看到选型的说明如下：

```xml
<!-- Server time zone could be set here.
    Time zone is used when converting between String and DateTime types,
    when printing DateTime in text formats and parsing DateTime from text,
    it is used in date and time related functions, if specific time zone was not passed as an argument.
    Time zone is specified as identifier from IANA time zone database, like UTC or Africa/Abidjan.
    If not specified, system time zone at server startup is used.
    Please note, that server could display time zone alias instead of specified name.
    Example: W-SU is an alias for Europe/Moscow and Zulu is an alias for UTC.
-->
<!-- <timezone>Europe/Moscow</timezone> -->
 
<!-- 时区在日期时间相关的函数，若指定时区作为参数。在Datetime和String类型之间进行转换。
时区的指定是按照IANA标准的时区库指定的，可以在Linux系统中通过命令查询
若不指定则使用系统启动的时区。 -->

```

### clickhouse时区函数

原文: <https://blog.csdn.net/vkingnew/article/details/107227037/>

官网时间日期函数: <https://clickhouse.com/docs/zh/sql-reference/functions/date-time-functions/>

clickhouse相关的时区函数：

```sql
Clickhouse> select formatDateTime(now(),'%F %T') as dt,toString(toDateTime(dt),'Asia/Shanghai') as BJ_time,toString(toDateTime(dt),'America/New_York') as NY_time;

SELECT 
    formatDateTime(now(), '%F %T') AS dt,
    toString(toDateTime(dt), 'Asia/Shanghai') AS BJ_time,
    toString(toDateTime(dt), 'America/New_York') AS NY_time
 
┌─dt──────────────────┬─BJ_time─────────────┬─NY_time─────────────┐
│ 2020-07-12 00:13:29 │ 2020-07-12 00:13:29 │ 2020-07-11 12:13:29 │
└─────────────────────┴─────────────────────┴─────────────────────┘
 
1 rows in set. Elapsed: 0.006 sec. 

 
-- 可以看到Clickhouse默认采用的系统的UTC

 
Clickhouse> select formatDateTime(now(),'%F %T') as dt,toString(toDateTime(dt,'UTC'),'Asia/Shanghai') as BJ_time,toTimeZone(toDateTime(dt,'UTC'),'Asia/Shanghai') as random_time,toString(toDateTime(dt),'Asia/Shanghai') SH_TIME,toTimeZone(toDateTime(dt),'Asia/Shanghai') SH_time,toTimeZone(toDateTime(dt,'America/New_York'), 'Asia/Hong_Kong') HK_time;

SELECT 
    formatDateTime(now(), '%F %T') AS dt,
    toString(toDateTime(dt, 'UTC'), 'Asia/Shanghai') AS BJ_time,
    toTimeZone(toDateTime(dt, 'UTC'), 'Asia/Shanghai') AS random_time,
    toString(toDateTime(dt), 'Asia/Shanghai') AS SH_TIME,
    toTimeZone(toDateTime(dt), 'Asia/Shanghai') AS SH_time,
    toTimeZone(toDateTime(dt, 'America/New_York'), 'Asia/Hong_Kong') AS HK_time
 
┌─dt──────────────────┬─BJ_time─────────────┬─────────random_time─┬─SH_TIME─────────────┬─────────────SH_time─┬─────────────HK_time─┐
│ 2020-07-12 00:27:25 │ 2020-07-12 08:27:25 │ 2020-07-12 08:27:25 │ 2020-07-12 00:27:25 │ 2020-07-12 00:27:25 │ 2020-07-12 12:27:25 │
└─────────────────────┴─────────────────────┴─────────────────────┴─────────────────────┴─────────────────────┴─────────────────────┘

1 rows in set. Elapsed: 0.007 sec. 
 
-- 可以看到toTimeZone,与toString 的功能很像
 
 
Clickhouse> select formatDateTime(now(),'%F %T') as dt,toTypeName(toString(toDateTime(dt),'Asia/Shanghai')) SH_TIME,toTypeName(toTimeZone(toDateTime(dt),'Asia/Shanghai')) SH_time,toTypeName(toTimeZone(toDateTime(dt,'America/New_York'), 'Asia/Hong_Kong')) HK_time;
 
SELECT 
    formatDateTime(now(), '%F %T') AS dt,
    toTypeName(toString(toDateTime(dt), 'Asia/Shanghai')) AS SH_TIME,
    toTypeName(toTimeZone(toDateTime(dt), 'Asia/Shanghai')) AS SH_time,
    toTypeName(toTimeZone(toDateTime(dt, 'America/New_York'), 'Asia/Hong_Kong')) AS HK_time

┌─dt──────────────────┬─SH_TIME─┬─SH_time───────────────────┬─HK_time────────────────────┐
│ 2020-07-12 00:29:43 │ String  │ DateTime('Asia/Shanghai') │ DateTime('Asia/Hong_Kong') │
└─────────────────────┴─────────┴───────────────────────────┴────────────────────────────┘

1 rows in set. Elapsed: 0.002 sec. 
-- toTimeZone函数可以实现时区转换，通过toTypeName还可以获知字段类型，以及该字段对应的时区。
```
