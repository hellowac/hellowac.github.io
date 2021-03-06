---
nav: blog
layout: post
title: "流畅的python - 对象引用和回收"
author: "wangchao"
tags:
  - python
  - 'function'
  - '对象'
  - '弱引用'
category:
  - 'Programing Teach'
show: true
---

[{{ site.nav.home.name }}]({% link index.md %})/
[{{ site.nav.blog.name }}]({% link blog/index.md %})/
[{{ site.nav.blog.subnav.programing.name }}]({% link blog/programing/index.md %})/
{{ page.title }}

参考:[流畅的python](https://book.douban.com/subject/27028517/)

- [对象比较](#对象比较)
- [对象复制](#对象复制)
- [参数作为引用](#参数作为引用)
- [del和对象回收](#del和对象回收)
- [弱引用](#弱引用)
- [其他](#其他)
- [延伸阅读](#延伸阅读)

- **变量**
  - 变量是一个 `对象` 的 `标识` ，不是 `副本`.
  - 变量是一个 `对象` 的 `别名` .
  - 每个变量都有 `标识` 、`类型` 和 `值`。对象一旦创建，它的标识绝不会变；可以把标识理解为对象在内存中的地址。`is` 运算符比较两个对象的标识；`id()` 函数返回对象标识的整数表示。
  - 其他：
    - 对象 ID 的真正意义在不同的实现中有所不同。在 CPython 中，`id()` 返回对象的内存地址，但是在其他 Python 解释器中可能是别的值。
    - 关键是，ID 一定是唯一的数值标注，而且在对象的生命周期中绝不会变。

- **`==`和`is`之间的比较** <span id="对象比较"></span>
  - `==` 运算符比较两个对象的值（对象中保存的数据），而 `is` 比较对象的标识。
  - 在变量和单例值之间比较时，应该使用 `is` 。目前，最常使用 `is` 检查变量绑定的值是不是 `None` 。
    - `x is None` 和 `x is not None`
    - `is` 运算符比 `==` 速度快，因为它不能重载.接比较两个对象的 整数 ID。
    - `a == b` 是语法糖，等同于 `a.__eq__(b)`。
  - `__eq__` 方法继承自 `object`, 比较两个对象的 ID，结果与 `is` 一样。但是多数内置类型使用更有意义的方式覆盖了 `__eq__` 方法，会考虑对象属性的值。相等性测试可能涉及大量处理工作，例如，比较大型集合或嵌套层级深的结构时。
- **元组的相对不可变性**
  - 元组与多数 Python 集合（列表、字典、集，等等）一样，保存的是对象的引用。如果引用的元素是可变的，即便元组本身不可变，元素依然可变。【指 tuple 数据结构的物理内容（即保存的引用）不可变，与引用的对象无关。】
  - **注意:** 而 `str`、`bytes` 和 `array.array` 等 单一类型序列 是扁平的，它们保存的不是引用，而是在连续的内存中保存数据本身（字符、字节和数字）。

```python
# 对象引用示例：
In [82]: a = [1,2,3]  # a 引用一个 list 实例.

In [83]: b = a  # 将 a 的引用 复制 给 b .

In [84]: a.append(4)  # 执行 a 引用 的 list 实例的 append 方法.

In [85]: b
Out[85]: [1, 2, 3, 4]  # 由于 指向 同一个 实例. 所以 a 的 动作 反应在 b 上.

# id 示例
In [86]: class Gizmo:
    ...:     def __init__(self):
    ...:         print('Gizmo id:%d' % id(self))
    ...:

In [87]: x = Gizmo()
Gizmo id:4574173560  # 当前实例的对象ID（标识）

In [88]: y = Gizmo() * 10
Gizmo id:4574264848  # 未支持 * 运算符(__mul__). 导致报错. 赋值 标识符 失败.
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-88-0f524f080953> in <module>()
----> 1 y = Gizmo() * 10

TypeError: unsupported operand type(s) for *: 'Gizmo' and 'int'

In [89]: dir()  # 未 创建 y 变量.
['Gizmo', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'x']

# 元组的相对不可变性.
In [90]: t1 = (1, 2, [30, 40])  # t1 不可变，但是 t1[-1] 可变。

In [91]: t2 = (1, 2, [30, 40])  # 元素 与 t1 一样。

In [92]: t1 == t2  # 判断值是否相等.
Out[92]: True

In [93]: id(t1[-1])  # 查看 t1[-1] 列表的标识符.
Out[93]: 4574830344

In [94]: t1[-1].append(99) # 修改 列表 t1[-1]

In [95]: t1
Out[95]: (1, 2, [30, 40, 99])

In [96]: id(t1[-1])
Out[96]: 4574830344  # t1[-1] 列表值变了，但 标识符 没变.

In [97]: t1 == t2  # 现在 t1 和 t2 的 值不相等.
Out[97]: False
```

- **对象复制** <span id="对象复制"></span>
  - 有一个在线调试工具：[pythontutor](http://www.pythontutor.com/) 非常好.
  - **浅复制** ：即复制了最外层容器，副本中的元素是源容器中元素的引用
    - 复制列表（或多数内置的可变集合）最简单的方式是使用内置的类型构造方法。 但是 `构造方法` 和 `[:]` 做的是 `浅复制`, 如果所有元素都是不可变的，这样没有问题，能节省内存。但是，如果有可变的元素，可能就会导致意想不到的问题。
  - **深复制** : 副本不共享内部对象的引用
  - `copy` 模块的 `copy()` 提供浅复制， `deepcopy` 提供深复制. 且能为任意对象做 深浅复制。
    - 深复制不是件简单的事。如果对象有循环引用，那么这个朴素的算法会进入无限循环。`deepcopy` 函数会记住已经复制的对象，因此能优雅地处理循环引用.
    - 深复制有时可能太深了.例如，对象可能会引用不该复制的外部资源或单例值。我们可以实现特殊方法 `__copy__()` 和 `__deepcopy__()`，控制 `copy` 和 `deepcopy` 的行为，详情参见 [copy 模块](http://python.usyiyi.cn/documents/python_352/library/copy.html) 的文档。

```python
# 可变对象的复制， 可拷贝 到  pythontutor 网站看 数据动态变化.
l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)      # l2 是 l1 的浅复制.
l1.append(100)     # l1 中增加 100， 对 l2 没影响.
l1[1].remove(55)   # 将 内部列表 中的元素删除， 对 l2 有影响.
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22]  # 对 l2[1] 中的列表，为就地修改，同时反应到 l1[1] 列表. 因为他们引用的同一个列表.
l2[2] += (10, 11)  # 对 l2[2] 中的元祖, 为不可变类型，会重新创建一个并返回，不会影响 l1[2] 中的 元组.
print('l1:', l1)
print('l2:', l2)


In [125]: class a:
     ...:     def __copy__(self):
     ...:         print('浅复制')
     ...:         copy_data = a()
     ...:         copy_data.data = ['asdf']
     ...:         return copy_data
     ...:     def __deepcopy__(self,a_dict):  # a_dict 为 已复制的对象 映射 字典.
     ...:         print('深复制')
     ...:         copy_data = a()
     ...:         copy_data.data = ['深复制']
     ...:         a_dict[id(copy_data)] = copy_data
     ...:         return copy_data
     ...:

In [126]: b = a()

In [130]: c = copy.copy(b)
浅复制

In [131]: c.data
Out[131]: ['asdf']

In [132]: d = copy.deepcopy(b)
深复制

In [133]: d.data
Out[133]: ['深复制']
```

- **函数的参数作为引用** <span id="参数作为引用"></span>
  - Python 唯一支持的参数传递模式是共享传参（call by sharing). 指函数的各个形式参数获得实参中各个引用的副本。【函数内部的形参是实参的别名。】
  - 结果： 函数可能会修改作为参数传入的可变对象，但是无法修改那些对象的标识。【无法替换传入的对象为另一个对象】
  - **不使用可变类型作为参数的默认值** , 因为对于可变类型 函数内部 对 参数 的修改，会反应到函数外部 或 其他共享该参数的对象.
  - **防御可变参数:** 如果定义的函数接收可变参数，应该谨慎考虑调用方是否期望修改传入的参数。

```python
In [134]: def f(a, b):
     ...:     a += b
     ...:     return a
     ...:

In [135]: x = 1

In [136]: y = 2

In [137]: f(x, y)  # 传入 不可变 对象, 会返回 全新的 结果对象. 【对于当前函数】
Out[137]: 3

In [138]: x, y  # 原 参数并没有改变.
Out[138]: (1, 2)

In [139]: a = [1, 2]

In [140]: b = [3, 4]

In [141]: f(a, b)  # 传入 可变 对象， 会在 原参数的 对象 上 就地修改. 【对于当前函数】
Out[141]: [1, 2, 3, 4]

In [142]: a, b
Out[142]: ([1, 2, 3, 4], [3, 4])

In [143]: t = (10, 20)

In [144]: u = (30 ,40)

In [145]: f(t, u)  # 传入 不可变对象, 内部操作 不会反应在 原 参数上.
Out[145]: (10, 20, 30, 40)

In [146]: t, u
Out[146]: ((10, 20), (30, 40))

# 示例：
class HauntedBus:
    """备受幽灵乘客折磨的校车"""

    def __init__(self, passengers=[]):  # 默认参数为可变类型，列表.
        self.passengers = passengers  # 没有传参时，赋值默认参数给当前对象.

    def pick(self, name):
        self.passengers.append(name)  # 其实修改的是默认列表，【未传参时】

    def drop(self, name):
        self.passengers.remove(name)

# 执行：
In [148]: bus1 = HauntedBus(['Alice', 'Bill'])  # 传入参数， 不使用默认参数

In [149]: bus1.passengers
Out[149]: ['Alice', 'Bill']

In [150]: bus1.pick('Charlie')

In [151]: bus1.drop('Alice')

In [152]: bus1.passengers  # 不会出现异常.
Out[152]: ['Bill', 'Charlie']

In [153]: bus2 = HauntedBus()  # 使用默认的参数.

In [154]: bus2.pick('Carrie')

In [155]: bus2.passengers
Out[155]: ['Carrie']

In [156]: bus3 = HauntedBus()  # 使用默认的参数.

In [157]: bus3.passengers  # 同 bus2 的 passengers 属性 指向 同一个默认列表.
Out[157]: ['Carrie']

In [158]: bus3.pick('Dave')

In [159]: bus2.passengers
Out[159]: ['Carrie', 'Dave']

In [160]: bus2.passengers is bus3.passengers
Out[160]: True

In [161]: bus1.passengers  # 未 使用默认参数 ， 同 bus2 和 bus3 是不同的列表。
Out[161]: ['Bill', 'Charlie']

In [163]: HauntedBus.__init__.__defaults__
Out[163]: (['Carrie', 'Dave'],)

In [164]: HauntedBus.__init__.__defaults__[0] is bus2.passengers
Out[164]: True   # 可见 bus2 和 bus3 的 passengers 属性 绑定到 HauntedBus.__init__.__defaults__ 属性的第一个元素上

# 优化方案1：
class TwilightBus:
    """让乘客销声匿迹的校车"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  # 为 None 时 ，创建一个新列表.
        else:
            self.passengers = passengers  # 创建 传入参数的别名. 应确定类中的修改是否要反应到外部中.

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)  # 会反应到传入的参数的对象上.

# 优化方案2：
class TwilightBus:
    """让乘客销声匿迹的校车"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  # 为 None 时 ，创建一个新列表.
        else:
            self.passengers = list(passengers)  # 创建副本，不是列表，就把他转为列表.【维护自己的列表】

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)  # 会反应到传入的参数的对象上.
```

- **del和对象回收** <span id="del和对象回收"></span>
  - 对象绝不会自行销毁；然而，无法得到对象时，可能会被当作垃圾回收。
  - del 语句删除名称，而不是对象。
    - del 命令可能会导致对象被当作垃圾回收，但是仅当删除的变量保存的是对象的最后一个引用，或者无法得到对象时。
    - 重新绑定也可能会导致对象的引用数量归零，导致对象被销毁。
      - 如果两个对象相互引用,当它们的引用只存在二者之间时，垃圾回收程序会判定它们都无法获取，进而把它们都销毁。
    - `__del__` 特殊方法.不会销毁实例，不应该在代码中调用。即将销毁实例时，Python 解释器会调用 `__del__` 方法，给实例最后的机会，释放外部资源。 参考标准库[__del__](https://docs.python.org/3/reference/datamodel.html#object.__del__)特殊方法.
  - 在 CPython 中，垃圾回收使用的主要算法是引用计数。
    - 实际上，每个对象都会统计有多少引用指向自己.
    - 当引用计数归零时，对象立即就被销毁：CPython 会在对象上调用 `__del__` 方法（如果定义了），然后释放分配给对象的内存。
    - CPython　2.0 增加了分代垃圾回收算法，用于检测引用循环中涉及的对象组——如果一组对象之间全是相互引用，即使再出色的引用方式也会导致组中的对象不可获取。
    - Python 的其他实现有更复杂的垃圾回收程序，而且不依赖引用计数，这意味着，对象的引用数量为零时可能不会立即调用 `__del__` 方法。
    - A. Jesse Jiryu Davis 写的“[PyPy, Garbage Collection, and a Deadlock](https://emptysqua.re/blog/pypy-garbage-collection-and-a-deadlock/)”一文对 `__del__` 方法的恰当用法和不当用法做了讨论。

```python
# 使用 weakref.finalize 注册一个在销毁对象时调用的回调函数。
In [166]: import weakref

In [167]: s1 = {1,2,3}

In [168]: s2 =  s1  # 指向同一个集合.

In [169]: def bye():  # 回调函数一定不能是要销毁的对象的绑定方法（类方法），否则会有一个指向对象的引用。
     ...:     print("拜拜，你被销毁了")
     ...:

In [170]: ender = weakref.finalize(s1,bye)  # 注册回调， 并返回一个变量，判断是否销毁。

In [171]: ender.alive
Out[171]: True

In [172]: del s1

In [173]: ender.alive # 说明 del s1 是删除引用，而不是对象。
Out[173]: True

In [174]: s2 = 'spam'  # 重新绑定 s2 后，表示 {1,2,3} 无法获取 （引用计数为0），此时调用 bye 回调函数.
拜拜，你被销毁了

In [175]: ender.alive  # ender 为 弱引用， 不在 计数 范围内.
Out[175]: False
```

- **弱引用** <span id="弱引用"></span>
  - 弱引用不会增加对象的引用数量。引用的目标对象称为 `所指对象` （referent）。因此，弱引用不会妨碍所指对象被当作垃圾回收。
  - 弱引用在缓存应用中很有用，因为不想仅因为被缓存引用着而始终保存缓存对象。
  - 使用 `weakref.ref` 实例可以获取所指对象。如果对象存在，调用弱引用可以获取对象；否则返回 `None` 。
    - `weakref.ref` 类其实是低层接口，供高级用途使用，多数程序最好使用 [weakref](http://python.usyiyi.cn/translate/python_352/library/weakref.html) 工具集 和 `finalize` 。
    - `weakref` 工具集合： `WeakKeyDictionary` 、 `WeakValueDictionary` 、`WeakSet` 、`finalize`(内部使用弱引用)
  - **WeakValueDictionary：** 实现的是一种可变映射，里面的值是对象的弱引用。
    - 被引用的对象在程序中的其他地方被当作垃圾回收后，对应的键会自动从 `WeakValueDictionary` 中删除。因此，`WeakValueDictionary` 经常用于缓存。
  - **WeakSet**:  保存元素弱引用的集合类。元素没有强引用时，集合会把它删除。
    - 如果一个类需要知道所有实例，一种好的方案是创建一个 `WeakSet` 类型的类属性，保存实例的引用。
    - 如果使用常规的 `set` ，实例永远不会被垃圾回收，因为类中有实例的强引用，而类存在的时间与 Python 进程一样长，除非显式删除类。
  - 弱引用局限：
    - 基本的 `list` 和 `dict` 实例不能作为所指对象, 但是它们的子类可以作为弱引用所指对象.
    - 基本的 `int` 、 `list` 、 `tuple` 、`string` 、`dict` 实例不能作为弱引用的目标。
    - 但是 `set` 实例可以作为所指对象。
    - 但是， `str` 、 `dict` 、`list` 的子类实例 和 用户自定义的类型实例 可以作为弱引用所指对象.
    - 然而， `int` 、 `tuple` 的子类实例 也不能作为弱应用对象.

**基本类型及其子类是否可以作为弱引用所指对象**

类型 | 实例 | 子类实例
-----|-----|---------
int | n | n
tuple | n | n
str | n | y
set | y | y
list | n | y
自定义 | y | y

```python
# 前提： Python 控制台会自动把 _ 变量绑定到结果不为 None 的表达式结果上。
In [1]: import weakref

In [2]: a_set = {0,1}

In [3]: wref = weakref.ref(a_set)  # 弱引用对象 wref

In [4]: wref
Out[4]: <weakref at 0x10f29aea8; to 'set' at 0x10e906f28>

In [5]: wref()  # 返回的是被引用的对象，{0, 1}。因为是控制台会话，所以 {0, 1} 会绑定给 _ 变量。
Out[5]: {0, 1}

In [6]: a_set = {2, 3, 4}   # a_set 不再指代 {0, 1} 集合，因此集合的引用数量减少了。但是 _ 变量仍然指代它。

In [7]: wref()
Out[7]: {0, 1}

In [8]: wref() is None  # 计算这个表达式时，{0, 1} 存在，因此 wref() 不是 None。但是，随后 _ 绑定到结果值 False。现在 {0, 1} 没有强引用了。
Out[8]: False

In [9]: wref() is None  # 因为 {0, 1} 对象不存在了，所以 wref() 返回 None。
Out[9]: False  # 此时在 ipython 中， 隐藏了其他引用，所以返回False， 在 标准 Cpython解释器中，为 True.

# WeakValueDictionary 示例：
class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

# 执行：
In [2]: import weakref

In [3]: stock = weakref.WeakValueDictionary()  # 创建弱引用字典实例。

In [4]: catalog = [Cheese('Read Leicester'), Cheese('Tilsit'),Cheese('Brie'), Cheese('Parmesan')]

In [6]: for cheese in catalog:
   ...:     stock[cheese.kind] = cheese  # 名称映射到实例. [弱引用]
   ...:

In [7]: sorted(stock.keys())
Out[7]: ['Brie', 'Parmesan', 'Read Leicester', 'Tilsit']

In [8]: del catalog

In [9]: sorted(stock.keys())  # 为什么还剩一个？ 因为临时变量。
Out[9]: ['Parmesan']

In [10]: del cheese

In [11]: sorted(stock.keys())  # 临时变量删除后，为空.
Out[11]: []

# list, int 不能作为若引用.
In [12]: class MyList(list):
    ...:      """ list 的子类,实例可以作为弱引用的目标"""
    ...:

In [13]: a_list = MyList(range(10))

In [14]: wref_to_a_list = weakref.ref(a_list)

In [15]: _list = list(range(10))

In [16]: wref_to_list = weakref.ref(_list)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-64f030a51bda> in <module>()
----> 1 wref_to_list = weakref.ref(_list)

TypeError: cannot create weak reference to 'list' object

In [17]: _string = 'string'  # string 也不行.

In [18]: wref_to_a_string = weakref.ref(_string)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-18-9f2dcf6ba75a> in <module>()
----> 1 wref_to_a_string = weakref.ref(_string)

TypeError: cannot create weak reference to 'str' object

In [19]: _int = 12  # int 不行.

In [20]: wref_to_int = weakref.ref(_int)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-20-da8123a191c2> in <module>()
----> 1 wref_to_int = weakref.ref(_int)

TypeError: cannot create weak reference to 'int' object

In [21]: _tuple = (1,2,3)  # tuple 不行.

In [22]: wref_to_tuple = weakref.ref(_tuple)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-22-764c0b0be918> in <module>()
----> 1 wref_to_tuple = weakref.ref(_tuple)

TypeError: cannot create weak reference to 'tuple' object

In [23]: _dict = dict(a=1,b=2)  # dict 不行.

In [24]: wref_to_dict = weakref.ref(_dict)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-24-9979a3c69214> in <module>()
----> 1 wref_to_dict = weakref.ref(_dict)

TypeError: cannot create weak reference to 'dict' object

In [25]: class MyInt(int):  # int 的 子类不行.
    ...:     pass
    ...:

In [26]: a_int = MyInt(11)

In [27]: wref_to_a_int = weakref.ref(a_int)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-27-69adfbcf87a0> in <module>()
----> 1 wref_to_a_int = weakref.ref(a_int)

TypeError: cannot create weak reference to 'MyInt' object

In [28]: class MyStr(str):  # str 的子类可以.
    ...:     pass
    ...:

In [29]: a_str = MyStr('weakref')

In [30]: wref_to_a_str = weakref.ref(a_str)

In [31]: class MyTuple(tuple):  # tuple 的 子类不行.
    ...:     pass
    ...:

In [33]: a_tuple = MyTuple((1,2,3))

In [34]: wref_to_a_tuple = weakref.ref(a_tuple)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-34-e89498aa13ba> in <module>()
----> 1 wref_to_a_tuple = weakref.ref(a_tuple)

TypeError: cannot create weak reference to 'MyTuple' object

In [35]: class MyDict(dict):  # dict 的 子类可以
    ...:     pass
    ...:

In [36]: a_dict = MyDict(a=1,b=2)

In [37]: wref_to_a_dict = weakref.ref(a_dict)
```

- **其他：** <span id="其他"></span>
  - 对元组 `t` 来说，`t[:]` 不创建副本，而是返回同一个对象的引用。
  - 此外，`tuple(t)` 获得的也是同一个元组的引用。
  - `str`、`bytes` 和 `frozenset` 实例也有这种行为。注意，`frozense`t 实例不是序列，因此不能使用 `fs[:]`（`fs` 是一个 `frozenset` 实例）。但是，`fs.copy()` 具有相同的效果：它会欺骗你，返回同一个对象的引用，而不是创建一个副本.
    - copy 方法不会复制所有对象，这是一个善意的谎言，为的是接口的兼容性：这使得 frozenset 的兼容性比 set 强。 **两个不可变对象是同一个对象还是副本，反正对最终用户来说没有区别。**

```python
In [38]: t1 = (1,2,3)

In [39]: t2 = tuple(t1)  # 返回同一个 引用.

In [40]: t2 is t1
Out[40]: True

In [41]: t3 = t1[:]

In [42]: t3 is t2
Out[42]: True

# 共享对象：字符串字面量可能会创建共享的对象
In [43]: t1 = (1,2,3)

In [44]: t3 = (1,2,3)

In [45]: t3 is t1  # 相等，但不是同一个对象。
Out[45]: False

In [46]: s1 = 'ABC'

In [47]: s2 = 'ABC'

In [48]: s2 is s1  # 指向同一个 字符串对象， 一种优化措施，称为 驻留（interning）
Out[48]: True

# CPython 还会在小的整数上使用这个优化措施，防止重复创建“热门”数字，如 0、-1 和 42。注意，CPython 不会驻留所有字符串和整数，驻留的条件是实现细节，而且没有文档说明。
```

- **延伸阅读** <span id="延伸阅读"></span>
  - [Data Model](https://docs.python.org/3/reference/datamodel.html) ,Python 语言参考手册中开头清楚解释了对象的标识和值。
  - [Python 103: Memory Model & Best Practices](http://conferences.oreilly.com/oscon/oscon2013/public/schedule/detail/29374), 演讲页面 可以参考很多主题. [YouTube](https://www.youtube.com/watch?v=HHFCFJSPWrI) 视频
  - [Python Module of the Week](http://pymotw.com/), Doug Hellmann 所写一长串精彩的博客文章, 后来集结成书，即《Python 标准库》[py2](https://pymotw.com/2/)和[py3](https://pymotw.com/3/)
    - [copy - Duplicate Objects](http://pymotw.com/2/copy/) 和 [weakref - Garbage-Collectable References to Objects](http://pymotw.com/2/weakref/) 两篇涵盖本章内容，其中copy有基于新版本的python3, [copy-py3](https://pymotw.com/3/copy/) , weakref 的python3 版本为 [weakref - Impermanent References to Objects](https://pymotw.com/3/weakref/)
  - [gc](https://docs.python.org/3/library/gc.html), CPython 分代垃圾回收程序的更多信息.
    - 文档开头的第一句话是：“这个模块为可选的垃圾回收程序提供接口。”“可选的”这个修饰词可能让人惊讶，不过“[Data Model](https://docs.python.org/3/reference/datamodel.html)”一章也说：
      - **垃圾回收可以延缓实现，或者完全不实现——如何实现垃圾回收是实现的质量问题，只要不把还能获得的对象给回收了就行。**
  - [How Does Python Manage Memory?](http://effbot.org/pyfaq/how-does-python-manage-memory.htm), Fredrik Lundh（很多核心库的创建者，如 ElementTree、Tkinter 和图像库 PIL）所写的一篇短文，谈论了 Python 的垃圾回收程序。强调垃圾回收程序是一种实现的特性，其行为在不同的 Python 解释器中有所不同。例如，Jython 用的是 Java 垃圾回收程序。
  - [PEP 442—Safe object finalization](https://www.python.org/dev/peps/pep-0442/), CPython 3.4 改进了处理有 `__del__` 方法的对象的方式
  - [字符串驻留](https://en.wikipedia.org/wiki/String_interning), 维基百科中一篇文章,提到了几种语言对这个技术的利用，包括 Python。
