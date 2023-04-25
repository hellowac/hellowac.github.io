# django

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