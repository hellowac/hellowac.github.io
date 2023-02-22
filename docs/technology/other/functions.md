# 函数

## 为何要用sys.exit()退出？

原文: [为何要用sys.exit()退出？](https://www.pynote.net/archives/1036)

Python有4个不同的退出程序的函数，`exit()`，`quit()`，`os._exit()`和本文要介绍的`sys.exit()`。

`exit()`和`quit()`是一样的，它俩的功能基本上与`sys.exit()`一样，只有`os._exit()`有些简单粗暴。

**exit和quit函数**

这两个函数的作用，就是直接退出程序，可以带一个参数作为程序的返回码，如果不带参数，默认就是返回0.

```python
xinlin@ubuntu:~/test$ python3 -q
>>> exit(111)
xinlin@ubuntu:~/test$ echo $?
111
xinlin@ubuntu:~/test$ python3 -q
>>> quit(222)
xinlin@ubuntu:~/test$ echo $?
222
xinlin@ubuntu:~/test$ python3 -q
>>> exit()
xinlin@ubuntu:~/test$ echo $?
0
xinlin@ubuntu:~/test$ python3 -q
>>> quit()
xinlin@ubuntu:~/test$ echo $?
0
```

这两个函数一般在交互式的python解释器中使用。其实它俩也会抛出`SystemExit异常`，因此说跟`sys.exit()`一样。

**sys.exit()函数**

`sys模块`的`exit`函数，通过抛出一个`SystemExit异常`来尝试结束程序，Python代码可以捕获这个异常来进行一些程序退出前的清理工作，也可以不退出程序。

`sys.exit`函数同样可以带一个参数来作为程序的退出码，默认是`0`.

```python
>>> import sys
>>> try:
...     sys.exit(101)
... except SystemExit as e:
...     print(repr(e))
...     print(str(e))
...
SystemExit(101)
101
>>>
```

看起来使用`str()`函数在`except`分支获取返回码，比较判断不同的返回码，并做响应的清理动作，是比较方便的。另外一个细节，上面这段代码在Python解释器中执行，因为异常被捕获，所以不会导致解释器退出！

捕获了`sys.exit()`函数抛出的异常，处理之后，还要程序继续退出，就需要直接使用`exit`或`quit`函数。实践中，完整的使用`sys.exit`函数的逻辑应该是如下这样的代码：

```python
import sys

def main():
    sys.exit(123)
    return

if __name__ == '__main__':
    try:
        main()
    except SystemExit as e:
        if str(e) == '123':
            print('---123---')
            exit(123)
```

一般在`python`脚本中都选择使用`sys.exit`函数退出程序，可以有个异常捕获机制来做清理扫尾的工作，程序会更加灵活健壮。

**os._exit()函数**

这个函数简单粗暴，就是直接退出python解释器，后面的代码都不执行了！一般程序不推荐使用这种退出方式。

补充一个细节：

**在python线程中，使用`sys.exit`（包括`exit`和`quit`），都只能实现退出子线程，而不能退出主线程；**

**如果在子线程中调用`os._exit`，可以实现整个程序的退出。**

## 驼峰命名法和骆驼命名法互转

原文: <https://blog.csdn.net/mouday/article/details/90079956>

```python
# -*- coding: utf-8 -*-


def get_lower_case_name(text):
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)

    return "".join(lst).lower()


if __name__ == '__main__':
    print(get_lower_case_name("StudentNameModel"))

# student_name_model
```

另一种实现方式:

```python
# -*- coding: utf-8 -*-
import re


def pascal_case_to_snake_case(camel_case: str):
    """大驼峰（帕斯卡）转蛇形"""
    snake_case = re.sub(r"(?P<key>[A-Z])", r"_\g<key>", camel_case)
    return snake_case.lower().strip('_')


def snake_case_to_pascal_case(snake_case: str):
    """蛇形转大驼峰（帕斯卡）"""
    words = snake_case.split('_')
    return ''.join(word.title() for word in words)

```
