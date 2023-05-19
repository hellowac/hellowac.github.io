# django

## django orm 外键引用自身

在 Django 中，可以使用外键来引用自身。这种情况通常被称为“自连接”。

假设我们有一个 `Category` 模型，其中每个分类可以具有父分类。要实现这一点，我们可以定义一个 `parent` 字段，并将其设置为指向 `self`：

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
```

上述代码中的 `ForeignKey` 定义了与自己的关系。通过在 `'self'` 参数中指定模型名称，我们告诉 Django 这是一个自连接。

注意，我们还需要指定 `null=True` 和 `blank=True`，以允许顶级分类没有父分类。

在创建模型实例时，您可以像处理任何其他外键一样设置父分类。例如，要将分类 A 设置为分类 B 的父分类：

```python
a = Category.objects.create(name='A')
b = Category.objects.create(name='B', parent=a)
```

上述代码将创建两个分类：`A` 和 `B`，其中 `B` 作为 `A` 的子分类。

如果要获取所有属于某个分类的子分类，可以使用以下查询：

```python
children = Category.objects.filter(parent=my_category)
```

其中 `my_category` 是要查询的分类。该查询将返回所有直接属于 `my_category` 的子分类。

## django orm 定义 多对多关系，并且支持null

在 Django 中，您可以使用 `ManyToManyField` 来定义多对多关系。默认情况下，该字段不支持 NULL 值，但是您可以通过将其设置为 `blank=True` 和 `null=True` 来支持 NULL 值：

```python
class Person(models.Model):
    name = models.CharField(max_length=100)
    friends = models.ManyToManyField('self', blank=True, null=True)
```

在上述代码中，我们定义了一个 `Person` 模型，并创建了一个名为 `friends` 的 `ManyToManyField` 字段，它指向自己的模型。

由于该字段设置为 `blank=True` 和 `null=True`，因此每个 `Person` 对象可以选择不具有任何朋友，并且可以将朋友设置为 `NULL`。

要add一些朋友，则可以使用以下语法：

```python
john = Person.objects.create(name='John')
jane = Person.objects.create(name='Jane')

# John and Jane are friends:
john.friends.add(jane)

# Jane is no longer John's friend:
john.friends.remove(jane)
```

在上述代码中，我们首先创建了两个人物对象（John 和 Jane），然后将 Jane 添加到 John 的朋友列表中。接着我们从 John 的朋友列表中删除了 Jane。

要获取某个人的所有朋友，可以使用以下查询：

```python
my_person.friends.all()
```

其中 `my_person` 是要查询的人物对象。该查询将返回该人物的所有朋友作为一个 queryset 对象。

## django orm 外键on_delete键设置

在 Django ORM 中，`ForeignKey` 字段表示一个数据模型与另一个数据模型之间的关系。当删除引用的对象时，您可以使用 `on_delete` 参数指定如何处理该字段上的引用。

以下是可用选项：

- `models.CASCADE`: 删除引用对象，并删除对该对象的所有引用。
- `models.PROTECT`: 防止删除引用对象。如果尝试删除引用对象，则会引发 `ProtectedError` 异常。
- `models.SET_NULL`: 删除引用对象，并将该字段设置为 NULL（仅适用于具有 null=True 的字段）。
- `models.SET_DEFAULT`: 删除引用对象，并将该字段设置为默认值（仅适用于具有默认值的字段）。
- `models.SET()`: 删除引用对象，并将该字段设置为指定的值。使用此选项时，您需要提供一个 `value` 参数，该参数表示要设置的值。例如：`models.SET(0)` 将该字段设置为 0。
- `models.DO_NOTHING`: 什么都不做。删除引用对象时，数据库可能会引发引用完整性错误。

下面是一个示例模型，其中包含一个外键字段，使用了 `on_delete` 参数：

```python
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
```

在上述代码中，我们定义了一个 `Book` 模型，并使用 `ForeignKey` 字段创建了一个名为 `author` 的外键字段。`on_delete=models.CASCADE` 表示当引用的作者对象被删除时，将删除所有对该对象的引用。

当使用 `ForeignKey` 字段时，始终应该考虑如何处理引用的对象被删除的情况。根据您的需求选择正确的选项是非常重要的，并确保数据的完整性和一致性。

## django orm 对外键进行赋值时检查

在 Django ORM 中，可以使用 ForeignKey 来建立模型之间的关系。如果要在赋值时限制外键的值，可以通过重写模型的 save 方法来实现。以下是一个示例：

```python
class MyModel(models.Model):
    foreign_key = models.ForeignKey(OtherModel)

    def save(self, *args, **kwargs):
        if self.foreign_key.some_condition():
            super().save(*args, **kwargs)
```

在这个示例中，我们重写了 MyModel 的 save 方法，并添加了一个条件来检查外键的值。如果外键的值满足某个条件，就允许保存；否则就不保存。

请注意，在重写 save 方法时，一定要调用父类的 save 方法（即 super().save(*args, **kwargs)），否则会导致数据无法保存到数据库中。

## django orm 的元数据_meta属性

Django ORM中的 `_meta` 属性是一个特殊的元数据容器，它包含了与模型相关的各种信息。这些信息包括：

- 模型的名称
- 数据库表的名称
- 表中每个字段的信息（名称、类型、是否是主键等）
- 关联模型的信息（外键、多对多关系等）
- 模型的管理器

您可以在任何Django ORM模型实例上使用`_meta`属性来访问这些信息。例如，要获取某个模型的所有字段名称，可以使用以下代码：

``` python
from myapp.models import MyModel

fields = MyModel._meta.get_fields()
for field in fields:
    print(field.name)
```

在这个示例中，我们导入了`MyModel`模型，并使用`_meta`属性来获取该模型的所有字段。然后，我们使用循环遍历每个字段并打印其名称。

请注意，`_meta`属性返回一个`Options`对象，它是Django ORM内部用于存储模型元数据的类。因此，您可以通过查看Django ORM源代码或文档来获得有关`Options`类和其属性的更多信息。

```python
from django.db.models.options import Options
```

## 时区问题（USE_TZ）

参考原文: <https://blog.csdn.net/qq_41341757/article/details/109319850>{target="_blank"}

### Django出现的时间问题

问题描述：

不同时区的人所在的时间是不同的，如果都采用当地时间，那么导致数据库存储的时间，并不是同一时刻的时间。但如果都采用0时区时间，那么不在0时区的用户就会看到错误的时间，怎么做呢？

解决方案：

在代码和数据库中都采用UTC时间(0时区时间)，在和用户交互的时候采用当地时间。

### Django如何开启时区支持

1. 在配置文件中配置：

```python
USE_TZ = True
```

2. 配置文件指定自己所在的时间戳（不指定默认是0时区）

```python
LANGUAGE_CODE = 'zh-hans'  # 语言:简体中文

TIME_ZONE = 'Asia/Shanghai'  # 亚洲上海
```

3. 安装pytz模块：(时区转换专用模块)

```shell
pip install pytz 
```

### USe_TZ = True的效应

作用一：前端传递过来的`DateFiled`类型，经过模型类，存到数据库中，全部是`0`时区时间。

作用二： 后端自己写的代码，只要是使用`timezone`获取的时间（已知的时间）（带时区的时间），`django`会自己转换，无需我们手动转换。

作用三：模板显示问题：`django`模板，会将数据库中`0`时区的时间转换成当地时间，无需我们自己转换。

总结:

1. django中推荐使用`USE_TZ = True`，让数据库存储`0`时区时间。
2. django后端使用`timezone`获取当地时间，不使用原生的`datetime`。
3. django模板无需考虑时区问题，django将自动转换。
4. `USE_TZ = True`，和 `TIME_ZONE = ‘Asia/Shanghai’` # 亚洲上海必须设置。

### 了解django的配置文件

1：如果在没有django项目的情况下，django使用的自己的配置文件。

```text
python3.5.2/site_packages/django/conf/global_settings

在django项目的依赖包中寻找到。
```

2： django项目下，django启动的是

```text
项目中的settings文件
```

### 区分两类datetime对象

1： 时区关闭时，django使用**原生的datetime对象**保存本地时间。

2： 时区开启时，django使用**已知的datetime对象**保存本地时间。

验证：**时区关闭时**：django使用的timezone。

注意：此时使用的是`global_settings`配置文件，不存在`USE_TZ = True`这个配置项。

```python
(api_eduai) user@user-MS-7C18:~$ python3
>>> from django.conf import settings
>>> settings.configure()
>>> from django.utils import timezone
>>> now = timezone.now()  # 这里是不带时区的本地时间
>>> now
datetime.datetime(2023, 4, 25, 9, 12, 21, 346479)
```

结论：当关闭时区时，django 使用原生的 `datetime` 对象保存本地时间。

验证：时区开启时：django使用的timezone。
注意：此时我们进入django项目中使用python3 manager.py shell进入django环境：

```python
(api_eduai) user@user-MS-7C18:~/PycharmProjects/service/Grade$ python manage.py shell
>>> from django.utils import timezone
>>> timezone.now()  # 这里是不带时区的utc的时间
datetime.datetime(2023, 4, 25, 1, 21, 8, 308862, tzinfo=<UTC>)
>>> new = timezone.localtime()   # 这里是带时区的本地时间
>>> new
datetime.datetime(2023, 4, 25, 9, 21, 16, 612791, tzinfo=<DstTzInfo 'Asia/Shanghai' CST+8:00:00 STD>)
```

结论： 时区开启时，django使用已知的`datetime`对象保存本地时间。使用`localtime`获取的是本地东八区的时间。(注意：，`TIME_ZONE = ‘Asia/Shanghai’`， 这个配置项必须存在才可以)。

## datetime模块中的类

- date类： 日期对象(年，月，日)
- time类：时间对象（时，分， 秒，微秒）
- datetime类：日期时间对象 （年，月，日，时，分，秒，微秒）
- timedelta类：时间间隔对象
- tzinfo类：时区信息对象。

## datetime的常见用法

注意： 由于`timezone`返回的对象也是datetime对象，所以方法同样试用。

1、 获取当地是时间（年，月，日，时，分，秒，微秒）

```python
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2023, 4, 25, 9, 37, 18, 689534)
>>> today = datetime.datetime.today()
>>> today
datetime.datetime(2023, 4, 25, 9, 37, 34, 305245)
```

2、将时间转换成（时，分，秒，微秒）

```python
>>> new_time = datetime.datetime.now()
>>> new_time.time()
datetime.time(9, 38, 22, 8802)
```

3、将时间转换成（年，月，日）

```python
>>> new_time = datetime.datetime.now()
>>> new_time.date()
datetime.date(2023, 4, 25)
```

4、时间的加减计算：

```python
# 时间点-时间间隔 = 时间点
>>> import datetime
>>> now_time = datetime.datetime.now()
>>> now_time
datetime.datetime(2020, 10, 28, 8, 47, 30, 232944)
>>> day_3_ago = now_time - datetime.timedelta(days = 3)  # 减去3天
>>> day_3_ago
datetime.datetime(2020, 10, 25, 8, 47, 30, 232944)
```

5、格式化日期转换成datetime对象：

```python
>>> datetime.strptime('2023-04-25 12:22:12','%Y-%m-%d %H:%M:%S')
datetime.datetime(2023, 4, 25, 12, 22, 12)
```

## date的常用用法

1、date对象获取年月日

```python
>>> from datetime import date
>>> date_today = date.today()
>>> date_today
datetime.date(2023, 4, 25)
>>> date_today.year
2023
>>> date_today.month
4
>>> date_today.day
25
```

2、日期比较大小

```python
>>> from datetime import date
>>> a = date(2020, 10, 28)
>>> b = date(2020,10,27)
>>> a == b  # 等于
False
>>> a > b   # 大于
True        
>>> a < b   # 小于
False
>>> a <=b   # 小于等于
False
>>> a >= b  # 大于等于
True
>>> a !=b   # 不等于
True

```

3、replace替换

```python
>>> today_date = datetime.today().date()
>>> today_date
datetime.date(2023, 4, 25)  # 获取指定日期
>>> today_date = today_date.replace(day=3)  # 替换指定日期的day
>>> today_date
datetime.date(2023, 4, 3)
```

## Django的时区转换

1、`astimezone`的使用：将一个时间对象`（datetime）`转换成UTC时间对象`（datetime）`

```python
>>> from datetime import datetime
>>> import pytz
>>> utc = pytz.timezone('UTC')
>>> now_time = datetime.now()
>>> utc_time = now_time.astimezone(tz=utc)  # 转换为指定时区的时间
>>> print(now_time, utc_time)
2023-04-25 09:46:38.175286 2023-04-25 01:46:38.175286+00:00
```

2、`pytz.timezone(‘时区名’)`：此方法能获取一个`tzinfo`对象，该对象可在`datetime`生成时间中以参数的形式放入，即可生成对应时区的时间。

```python
>>> utc = pytz.timezone('UTC')
>>> datetime.now(tz=utc)  # 获取指定时区的时间
datetime.datetime(2023, 4, 25, 1, 48, 49, 844362, tzinfo=<UTC>)
```
