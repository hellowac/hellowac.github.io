# Mysql & Mariadb

## 创建/修改数据库设置

官网: <https://dev.mysql.com/doc/refman/8.0/en/charset-database.html>

**创建/修改特定字符集**

```sql
-- utf8mb4_unicode_ci;
CREATE DATABASE sina DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- utf8mb4_0900_ai_ci; mysql 8.0+支持
CREATE DATABASE risk_check DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

-- utf8mb4_general_ci; mysql5.7支持
CREATE DATABASE risk_check DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- database utf8mb4_general_ci; mysql5.7, 8.0+ 支持
ALTER DATABASE risk_check DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- table utf8mb4_general_ci; mysql5.7, 8.0+ 支持
ALTER TABLE alembic_version DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

```

## mysqldump导出数据

官网: <https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html>

```sql
-- 要备份整个数据库:
mysqldump db_name > backup-file.sql

-- 要将转储文件加载回服务器：
mysql db_name < backup-file.sql

-- 重新加载转储文件的另一种方法：
mysql -e "source /path-to-backup/backup-file.sql" db_name

-- mysqldump 对于通过将数据从一个 MySQL 服务器复制到另一个来填充数据库也非常有用：
mysqldump --opt db_name | mysql --host=remote_host -C db_name

-- 您可以使用一个命令转储多个数据库：
mysqldump --databases db_name1 [db_name2 ...] > my_databases.sql

-- 要转储所有数据库，请使用 --all-databases 选项：
mysqldump --all-databases > all_databases.sql

-- 对于 InnoDB 表，mysqldump 提供了一种进行在线备份的方法：
mysqldump --all-databases --master-data --single-transaction > all_databases.sql
-- 或者来自 MySQL 8.0.26:
mysqldump --all-databases --source-data --single-transaction > all_databases.sql
```

此备份在转储开始时获取所有表的全局读锁（使用 [FLUSH TABLES WITH READ LOCK](https://dev.mysql.com/doc/refman/8.0/en/flush.html#flush-tables-with-read-lock)）。 一旦获得了这个锁，就会读取二进制日志坐标并释放锁。 如果在发出 [FLUSH](https://dev.mysql.com/doc/refman/8.0/en/flush.html) 语句时正在运行长更新语句，MySQL 服务器可能会停止，直到这些语句完成。 之后，转储变为无锁并且不会干扰对表的读取和写入。 如果 MySQL 服务器接收到的更新语句很短（就执行时间而言），那么即使有很多更新，初始锁定周期也不应该是明显的。

对于时间点恢复（也称为“前滚”，当您需要恢复旧备份并重放自该备份以来发生的更改时），轮换二进制日志通常很有用（参见[第 5.4.4 节, “The Binary Log”](https://dev.mysql.com/doc/refman/8.0/en/binary-log.html)）或者至少知道转储对应的二进制日志坐标：

```shell
mysqldump --all-databases --master-data=2 > all_databases.sql

-- MySQL 8.0.26:
mysqldump --all-databases --source-data=2 > all_databases.sql
```

或者:

```shell
mysqldump --all-databases --flush-logs --master-data=2 > all_databases.sql

-- MySQL 8.0.26:
mysqldump --all-databases --flush-logs --source-data=2 > all_databases.sql
```

[--source-data](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_source-data) 或 [--master-data](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_master-data) 选项可以与 [--single-transaction](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_single-transaction) 选项同时使用，如果表是 使用 InnoDB 存储引擎存储。

有关进行备份的更多信息，请参阅第 [7.2 节“数据库备份方法”](https://dev.mysql.com/doc/refman/8.0/en/backup-methods.html)和第 [7.3 节“示例备份和恢复策略”](https://dev.mysql.com/doc/refman/8.0/en/backup-strategy-example.html)。

* 要选择 [--opt](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_opt) 的效果（某些功能除外），请对每个功能使用 `--skip` 选项。 要禁用扩展插入和内存缓冲，请使用 [--opt](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_opt) [--skip-extended-insert](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_extended-insert) [--skip-quick](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_quick)。 （实际上， `--skip-extended-insert` `--skip-quick` 就足够了，因为 `--opt` 默认是开启的。）
* 要反转 [--opt](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_opt) 除禁用索引和表锁定之外的所有功能，请使用 [--skip-opt](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_skip-opt) [--disable-keys](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_disable-keys) [--lock-tables](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_lock-tables)。

## 其他注意事项

1. 多列作为唯一键时，最好指定所有的列都是不能为Null的，因为两个Null值默认是不一样的，所以会导致即使多个列除了Null值以外其他列的值相同，还是会插入数据成功.

    参考: <https://stackoverflow.com/questions/429805/mysql-question-unique-key-not-functioning-correctly-or-am-i-misunderstanding>
