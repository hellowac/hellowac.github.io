# python-petl使用简介

- 参考： <https://www.cnblogs.com/wry789/p/14459977.html>
- 翻译来自: <https://www.cnblogs.com/wry789/p/14459977.html>
- 官方文档: <https://petl.readthedocs.io/en/stable/>
- Source Code: <https://github.com/petl-developers/petl>
- Download: <http://pypi.python.org/pypi/petl>
- Mailing List: <http://groups.google.com/group/python-etl>

## petl简介

petl是使用原生python编写的ETL包，数据操作逻辑简单，但是处理数据的速度较慢。

<!--more-->

### ETL pipelines

petl包使用了大量的迭代器和延迟计算，在没有请求函数请求数据时，pipelines 不会开始处理数据。

```python
import petl as etl
table1 = etl.fromcsv('example.csv')
table2 = etl.convert(table1, 'foo', 'upper')
table3 = etl.convert(table2, 'bar', int)
table4 = etl.convert(table3, 'baz', float)
table5 = etl.addfield(table4, 'quux', lambda row: row.bar * row.baz)
```

petl.util.vis.look()，petl.io.csv.tocsv()，petl.io.text.totext()，petl.io.sqlite3.tosqlite3()，petl.io.db.todb()这些都是请求函数。执行请求函数后，根据pipelines ，顺序地处理数据。

```python
etl.look(table5)
```

### 面向对象编程

petl支持函数式和面向对象编程，例如

```python
>>> import petl as etl
>>> table = (
...     etl
...     .fromcsv('example.csv')
...     .convert('foo', 'upper')
...     .convert('bar', int)
...     .convert('baz', float)
...     .addfield('quux', lambda row: row.bar * row.baz)
... )
>>> table.look()
```

petl中的wrap()函数，可以把有效表容器数据转化为表结构数据

```python
>>> l = [['foo', 'bar'], ['a', 1], ['b', 2], ['c', 2]]
>>> table = etl.wrap(l)
>>> table.look()
+-----+-----+
| foo | bar |
+=====+=====+
| 'a' |   1 |
+-----+-----+
| 'b' |   2 |
+-----+-----+
| 'c' |   2 |
+-----+-----+
```

### 交互式使用

交互式环境使用petl时，对象表达默认调用petl.util.vis.look()函数

```python
>>> l = [['foo', 'bar'], ['a', 1], ['b', 2], ['c', 2]]
>>> table = etl.wrap(l)
>>> table
+-----+-----+
| foo | bar |
+=====+=====+
| 'a' |   1 |
+-----+-----+
| 'b' |   2 |
+-----+-----+
| 'c' |   2 |
+-----+-----+
```

默认调用时使用repr() 函数，以数值型方式打印数据，使用print函数，使用str()，以字符串方式打印数据

```python
>>> print(table)
+-----+-----+
| foo | bar |
+=====+=====+
| a   |   1 |
+-----+-----+
| b   |   2 |
+-----+-----+
| c   |   2 |
+-----+-----+
```

### 从操作系统调用petl脚本

```shell
petl "dummytable().tocsv()" > example.csv
cat example.csv | petl "fromcsv().cut('foo', 'baz').convert('baz', float).selectgt('baz', 0.5).head().data().totsv()"
```

提供一个位置参数"example.csv"给执行函数

### 表容器和表迭代器

表容器：

1. 实现了`__iter__` 方法
2. `__iter__` 返回一个表迭代器
3. `__iter__` 返回的所有表迭代器都是独立的，也就是说，从一个迭代器中消耗项不会影响其他迭代器

表迭代器：

1. 迭代器返回的每个项都是一个序列(例如，元组或列表)
2. 迭代器返回的第一个项是包含一系列标题值的标题行
3. 迭代器返回的每个后续项都是由一系列数据值组成的数据行
4. 标题值通常是字符串(str) ，但是可以是任何类型的对象，只要它实现了 \_\_ str\_\_ 并且可以选择
5. 数据值是任何可以取出的对象

例如：

```python
>>> table = [['foo', 'bar'], ['a', 1], ['b', 2]]
```

table是有效的表容器，实现了\_\_iter\_\_ 方法，返回一个迭代器，第一个项是标题值\['foo', 'bar'\]，后续是数据值\['a', 1\]和\['b', 2\]。

要求表容器支持独立的表迭代器(第3点)的主要原因是，来自表的数据可能需要在同一个程序或交互会话中进行多次迭代。例如，当在交互式会话中使用 petl 建立一系列数据转换步骤时，用户可能希望在定义所有步骤和完整执行转换之前检查来自几个中间步骤的输出。

### 扩展-集成自定义数据源

io 模块具有从许多已知数据源中提取数据的功能。但是，编写支持与其他数据源集成的扩展也很简单。为了使对象可用作 petl 表，它必须实现上面描述的表容器约定。下面是 ArrayView 类的源代码，该类允许将 petl 与 numpy 数组集成。这个类包含在 petl.io.numpy 模块中，但是也提供了一个如何集成其他数据源的例子:

```python
>>> import petl as etl
>>> class ArrayView(etl.Table):
...     def __init__(self, a):
...         # assume that a is a numpy array
...         self.a = a
...     def __iter__(self): # 实现了__iter__ 方法
...         # yield the header row
...         header = tuple(self.a.dtype.names) # 迭代器返回的第一个项是包含一系列标题值的标题行
...         yield header # 是一个迭代器
...         # yield the data rows
...         for row in self.a:
...             yield tuple(row) # 迭代器返回的每个后续项都是由一系列数据值组成的数据行
```

此类允许将numpy数组与petl函数一起使用

```python
>>> import numpy as np
>>> a = np.array([('apples', 1, 2.5),
...               ('oranges', 3, 4.4),
...               ('pears', 7, 0.1)],
...              dtype='U8, i4,f4')
>>> t1 = ArrayView(a)
>>> t1
+-----------+----+-----------+
| f0        | f1 | f2        |
+===========+====+===========+
| 'apples'  | 1  | 2.5       |
+-----------+----+-----------+
| 'oranges' | 3  | 4.4000001 |
+-----------+----+-----------+
| 'pears'   | 7  | 0.1       |
+-----------+----+-----------+

>>> t2 = t1.cut('f0', 'f2').convert('f0', 'upper').addfield('f3', lambda row: row.f2 * 2)
>>> t2
+-----------+-----------+---------------------+
| f0        | f2        | f3                  |
+===========+===========+=====================+
| 'APPLES'  | 2.5       |                 5.0 |
+-----------+-----------+---------------------+
| 'ORANGES' | 4.4000001 |  8.8000001907348633 |
+-----------+-----------+---------------------+
| 'PEARS'   | 0.1       | 0.20000000298023224 |
+-----------+-----------+---------------------+
```python

只要t1符合表容器的定义，就可以使用petl的函数和管道

# pyetl

- github：<https://github.com/taogeYT/pyetl>
- 参考： <https://www.yisu.com/zixun/146943.html>

`pyetl`是一个纯`python`开发的ETL框架， 相比`sqoop`, `datax `之类的ETL工具，`pyetl`可以对每个字段添加`udf函数`，使得数据转换过程更加灵活，相比专业ETL工具`pyetl`更轻量，纯`python`代码操作，更加符合开发人员习惯

*****

## 安装

```shell
pip3 install pyetl
```

*****

## **使用示例**

### 数据库表之间数据同步

```python
from pyetl import Task, DatabaseReader, DatabaseWriter
reader = DatabaseReader("sqlite:///db1.sqlite3", table_name="source")
writer = DatabaseWriter("sqlite:///db2.sqlite3", table_name="target")
Task(reader, writer).start()
```

### 数据库表到hive表同步

```python
from pyetl import Task, DatabaseReader, HiveWriter2
reader = DatabaseReader("sqlite:///db1.sqlite3", table_name="source")
writer = HiveWriter2("hive://localhost:10000/default", table_name="target")
Task(reader, writer).start()
```

### 数据库表同步ES

```python
from pyetl import Task, DatabaseReader, ElasticSearchWriter
reader = DatabaseReader("sqlite:///db1.sqlite3", table_name="source")
writer = ElasticSearchWriter(hosts=["localhost"], index_name="tartget")
Task(reader, writer).start()
```

### 添加字段映射

原始表目标表字段名称不同，需要添加字段映射

添加

```python
# 原始表source包含uuid，full_name字段
reader = DatabaseReader("sqlite:///db.sqlite3", table_name="source")
# 目标表target包含id，name字段
writer = DatabaseWriter("sqlite:///db.sqlite3", table_name="target")
# columns配置目标表和原始表的字段映射关系
columns = {"id": "uuid", "name": "full_name"}
Task(reader, writer, columns=columns).start()
```

### 指定字段的`udf映射`

字段的`udf映射`，对字段进行规则校验、数据标准化、数据清洗等

```python
# functions配置字段的udf映射，如下id转字符串，name去除前后空格
functions={"id": str, "name": lambda x: x.strip()}
Task(reader, writer, columns=columns, functions=functions).start()
```

### 扩展Task类

继承Task类灵活扩展ETL任务

```python
import json
from pyetl import Task, DatabaseReader, DatabaseWriter

class NewTask(Task):
  reader = DatabaseReader("sqlite:///db.sqlite3", table_name="source")
  writer = DatabaseWriter("sqlite:///db.sqlite3", table_name="target")
  
  def get_columns(self):
    """通过函数的方式生成字段映射配置，使用更灵活"""
    # 以下示例将数据库中的字段映射配置取出后转字典类型返回
    sql = "select columns from task where name='new_task'"
    columns = self.writer.db.read_one(sql)["columns"]
    return json.loads(columns)
   
  def get_functions(self):
    """通过函数的方式生成字段的udf映射"""
    # 以下示例将每个字段类型都转换为字符串
    return {col: str for col in self.columns}
   
  def apply_function(self, record):
    """数据流中对一整条数据的udf"""
    record["flag"] = int(record["id"]) % 2
    return record

  def before(self):
    """任务开始前要执行的操作, 如初始化任务表，创建目标表等"""
    sql = "create table destination_table(id int, name varchar(100))"
    self.writer.db.execute(sql)
  
  def after(self):
    """任务完成后要执行的操作，如更新任务状态等"""
    sql = "update task set status='done' where name='new_task'"
    self.writer.db.execute(sql)

NewTask().start()
```

## 目前已实现Reader和Writer列表

| Reader         | 介绍                                                                     |
| -------------- | ------------------------------------------------------------------------ |
| DatabaseReader | 支持所有[关系型数据库](https://www.yisu.com/mysql/ "关系型数据库")的读取 |
| FileReader     | 结构化文本数据读取，如csv文件                                            |
| ExcelReader    | Excel表文件读取                                                          |

| Writer              | 介绍                           |
| ------------------- | ------------------------------ |
| DatabaseWriter      | 支持所有关系型数据库的写入     |
| ElasticSearchWriter | 批量写入数据到es索引           |
| HiveWriter          | 批量插入hive表                 |
| HiveWriter2         | Load data方式导入hive表（推荐) |
| FileWriter          | 写入数据到文本文件             |

> 了解到的相关的其他文章和库
> 参考: <https://www.zhangshengrong.com/p/9MNlDz77NJ/>
> 英文原版：[Detailed explanation of Python data conversion tool for ETL](https://blog.karatos.in/a?ID=2837049d-fa78-4217-8c0d-f7cc7c9410a6)
