---
comments: true
---

# stringIO

## io.StringIO

参考: <https://www.jianshu.com/p/c9ecddf8b87f>

python2中：

```python
from StringIO import StringIO
```

python3中：

```python
from io import StringIO
```

`StringIO`的行为与`file对象`非常像，但它不是磁盘上文件，而是一个内存里的"**文件**"，在内存中读写`str`，我们可以像操作磁盘文件那样来操作`StringIO`，主要用于在内存缓冲区中读写数据。

<!-- more -->

创建一个StingIO对象，寄存在缓冲区，可选参数buf是一个str或unicode类型，它将会与后续写的数据存放一起。如下:

```python
output=StringIO([buf])
```

如：`'Hello\n'`和`Word\n'`会被放在一个缓冲区中。

```python
output=StringIO('Hello\n')
output.write('Word\n')
print(output.getvalue())

>>> Word
# 将原来默认的Hello覆盖了，因此在写入数据之前，
# 应先将读写位置移动到结尾【s.seek(0, os.SEEK_END)】，然后再写入，
# 否则，初始化数据会被覆盖掉，因为读写位置默认是0
```

## `StringIO`的方法

### read([n])

参数n限定读取长度，int类型；缺省状态为从当前读写位置读取对象output中存储的所有数据。读取结束后，读写位置被移动

### readline([length])

参数length限定读取的结束位置，int类型; 缺省状态为None,从当前读写位置读取至下一个以"\n"为结束符的当前行。读写位置被移动

### readlines([sizehint])

参数sizehint为int类型；缺省状态为读取所有行并作为列表返回, 且从当前读写位置读取至下一个以"\n"为结束符的当前行。读写位置被移动

### write(s)

从读写位置将参数s写入给对象output。参数s为str或unicode类型。读写位置被移动

### writelines(list)

从读写位置将list写入给对象output。参数list为一个列表，列表的成员为str或unicode类型。读写位置被移动。

### getvalue()

此函数没有参数，无论读写位置在哪里，都能够返回对象output中的所有数据

### truncate([size])

有size参数，无论读写位置在哪里，都从起始位置开始，裁剪size字节的数据
无size参数，将当前读写位置之前的数据，裁剪下来

### tell()

返回当前读写位置，读写位置默认是0，因此，之后写入的数据（"xxxxx!!!xxxxxx"）会将之前的数据覆盖掉  

### seek(pos[,mode])

移动当前读写位置至pos处，
可选参数`mode`：
为0时将读写位置移动至pos处，mode的默认值为0。
为1时将读写位置从当前位置起向前或向后移动|pos|个长度，
为2时将读写位置置于末尾处再向前或向后移动|pos|个长度；

### close()

释放缓冲区，执行此函数后，数据将被释放，也不可再进行操作。

### isatty()

此函数总是返回0。

### flush()

刷新内部缓冲区。

举例1：

```python
output=StringIO('Hello\n')
output.seek(0,2)               #将读写位置移动到末尾
output.write('Word\n')         #这样再写入字符串时，就不会覆盖之前默认的值
print(output.getvalue())       

>>> Hello
>>> Word
```

如果使用`read()`方法读取，则应该先将指针移动到开头，否则读取结果为空

```python
print(output.read())
output.seek(0,0)
print(output.read())

>>> Hello
>>> Word
```

## 应用：求一个StringIO 的 数据长度

参考: <https://stackoverflow.com/questions/4677433/in-python-how-do-i-check-the-size-of-a-stringio-object>

```python
import os
from StringIO import StringIO

s = StringIO()
s.write("abc")
pos = s.tell()  # 返回当前位置
s.seek(0, os.SEEK_END)  # 移动到末尾
print s.tell()  # 返回末尾位置 这里就得出 s 的字节数了。
s.seek(pos)  # 返回之前位置 
```
