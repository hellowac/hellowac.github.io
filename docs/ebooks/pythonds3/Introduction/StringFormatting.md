# 字符串格式化

我们已经看到，`print`函数提供了一种非常简单的方法来从 Python 程序输出值。 ``print`` 接受零个或多个参数，并使用单个空格作为默认分隔符来显示它们。 可以通过设置`sep`参数来更改分隔符。 此外，默认情况下，每次打印都会以换行符结尾。 可以通过设置 ``end`` 参数来更改此行为。 这些变化显示在以下会话中：

```pycon
>>> print("Hello")
Hello
>>> print("Hello", "World")
Hello World
>>> print("Hello", "World", sep="***")
Hello***World
>>> print("Hello", "World", end="***")
Hello World***>>>
```

对输出的外观进行更多控制通常很有用。 幸运的是，Python 为我们提供了一种替代方案，称为 **格式化字符串(formatted strings)**。 格式化字符串是一个模板，其中保持不变的单词或空格与将插入到字符串中的变量的占位符组合在一起。 例如，声明

```pycon
>>> print(a_name, "is", age, "years old.")
```

包含单词`is`和`years old`，但是名字和年龄会根据执行时的变量值而改变。 使用格式化字符串，我们将前面的语句写为

```pycon
>>> print("%s is %d years old." % (a_name, age))
```

这个简单的示例说明了一个新的字符串表达式。 ``%`` 运算符是一个字符串运算符，称为 **格式运算符(format operator)**。 表达式的左侧保存模板或格式字符串，右侧保存将替换到格式字符串中的值的集合。 请注意，右侧集合中值的数量与格式字符串中`%`字符的数量相对应。 从集合中按顺序从左到右获取值并将其插入到格式字符串中。

让我们更详细地看看这个格式化表达式的两边。 格式字符串可以包含一个或多个转换规范。 转换字符告诉格式运算符什么类型的值将被插入到字符串中的该位置。 在上面的示例中，`%s`指定一个字符串，而`%d`指定一个整数。 其他可能的类型规范包括`i`、`u`、`f`、`e`、`g`、`c`或`%`。 “表 9”总结了所有各种类型的规格。

**表 9：字符串格式转换字符**

| **转换字符** | **输出格式**                                                |
| ------------ | ----------------------------------------------------------- |
| ``d``, ``i`` | 整数                                                        |
| ``u``        | 无符号整数                                                  |
| ``f``        | 浮点数为 m.ddddd                                            |
| ``e``        | 浮点数为 m.ddddde+/-xx                                      |
| ``E``        | 浮点为 m.dddddE+/-xx                                        |
| ``g``        | 对于小于`-4`或大于`+5`的指数使用``%e``，否则使用``%f``      |
| ``c``        | 单个字符                                                    |
| ``s``        | 字符串，或任何可以使用`str`函数转换为字符串的Python数据对象 |
| ``%``        | 插入文字 ``%`` 字符                                         |

除了格式字符之外，您还可以在`%`和格式字符之间包含格式修饰符。 格式修饰符可用于左对齐或右对齐具有指定字段宽度的值。 修饰符还可用于指定字段宽度以及小数点后的位数。 `表 10` 解释了这些格式修饰符。

**表 10：其他格式选项**

| **修饰符** | **例子**     | **描述**                                          |
| ---------- | ------------ | ------------------------------------------------- |
| number     | ``%20d``     | 将值放入宽度为 20 的字段中                        |
| ``-``      | ``%-20d``    | 将值放入 20 个字符宽的字段中，左对齐              |
| ``+``      | ``%+20d``    | 将值放入 20 个字符宽的字段中，右对齐              |
| ``0``      | ``%020d``    | 将值放入 20 个字符宽的字段中，并用前导零填充      |
| ``.``      | ``%20.2f``   | 将值放入 20 个字符宽、小数点右侧 2 个字符的字段中 |
| ``(name)`` | ``%(name)d`` | 使用`name`作为键从提供的字典中获取值              |

如前所述，格式运算符的右侧是将插入到格式字符串中的值的集合。 该集合可以是元组或字典。 如果集合是元组，则按位置顺序插入值。 也就是说，元组中的第一个元素对应于格式字符串中的第一个格式字符。 如果集合是字典，则根据键插入值。 在这种情况下，所有格式字符必须使用`(name)`修饰符来指定键的名称。

```pycon
>>> price = 24
>>> item = "banana"
>>> print("The %s costs %d cents" % (item, price))
The banana costs 24 cents
>>> print("The %+10s costs %5.2f cents" % (item, price))
The     banana costs 24.00 cents
>>> print("The %+10s costs %10.2f cents" % (item, price))
The     banana costs      24.00 cents
>>> itemdict = {"item": "banana", "cost": 24}
>>> print("The %(item)s costs %(cost)7.1f cents" % itemdict)
The banana costs    24.0 cents
```

除了使用格式字符和格式修饰符的格式字符串之外，Python 字符串还包含一个`format`方法，可以与新的`Formatter`类结合使用来实现复杂的字符串格式化。 有关这些功能的更多信息可以在 Python 库参考手册中找到。

```pycon
>>> print("The {} costs {} cents".format(item, price))
The banana costs 24 cents
>>> print("The {:s} costs {:d} cents".format(item, price))
The banana costs 24 cents
```

Python 3.6 引入了 **f-strings**，这是一种使用正确的变量名称而不是占位符的方法。 格式化转换符号仍然可以在 f 字符串内使用，但对齐符号与占位符中使用的对齐符号不同（请参阅“表 11”）。 我们将对文本的其余部分使用这种格式设置方法。

**表 11：f-string格式选项**

| **修饰符** | **例子**   | **描述**                                            |
| ---------- | ---------- | --------------------------------------------------- |
| number     | ``:20d``   | 将值放入宽度为 20 的字段中                          |
| ``<``      | ``:<20d``  | 将值放入 20 个字符宽的字段中，左对齐                |
| ``>``      | ``:>20d``  | 将值放入 20 个字符宽的字段中，右对齐                |
| ``^``      | ``:^20d``  | 将值放入 20 个字符宽、居中对齐的字段中              |
| ``0``      | ``:020d``  | 将值放入 20 个字符宽的字段中，并用前导零填充。      |
| ``.``      | ``:20.2f`` | 将值放入 20 个字符宽、小数点右侧 2 个字符的字段中。 |

```pycon
>>> print(f"The {item:10} costs {price:10.2f} cents")
The banana     costs      24.00 cents
>>> print(f"The {item:<10} costs {price:<10.2f} cents")
The banana     costs 24.00      cents
>>> print(f"The {item:^10} costs {price:^10.2f} cents")
The   banana   costs   24.00    cents
>>> print(f"The {item:>10} costs {price:>10.2f} cents")
The     banana costs      24.00 cents
>>> print(f"The {item:>10} costs {price:>010.2f} cents")
The     banana costs 0000024.00 cents
>>> itemdict = {"item": "banana", "price": 24}
>>> print(f"Item:{itemdict['item']:.>10}\n" +
... f"Price:{'$':.>4}{itemdict['price']:5.2f}")
Item:....banana
Price:...$24.00
```

有关这些功能的更多信息可以在 Python 库参考手册中找到。

???- info "原文"

        **String Formatting**

    We have already seen that the ``print`` function provides a very simple way to output values from a Python program. ``print`` takes zero or more parameters and displays them using a single blank as the default separator. It is possible to change the separator character by setting the ``sep`` argument. In addition, each print ends with a newline character by default. This behavior can be changed by setting the ``end`` argument. These variations are shown in the following session:

    ```pycon
    >>> print("Hello")
    Hello
    >>> print("Hello", "World")
    Hello World
    >>> print("Hello", "World", sep="***")
    Hello***World
    >>> print("Hello", "World", end="***")
    Hello World***>>>
    ‵‵`

    It is often useful to have more control over the look of your output. Fortunately, Python provides us with an alternative called **formatted strings**. A formatted string is a template in which words or spaces that will remain constant are combined with placeholders for variables that will be inserted into the string. For example, the statement

    ```pycon
    >>> print(a_name, "is", age, "years old.")
    ‵‵`

    contains the words ``is`` and ``years old``, but the name and the age will change depending on the variable values at the time of execution. Using a formatted string, we write the previous statement as

    ```pycon
    >>> print("%s is %d years old." % (a_name, age))
    ‵‵`

    This simple example illustrates a new string expression. The ``%`` operator is a string operator called the **format operator**. The left side of the expression holds the template or format string, and the right side holds a collection of values that will be substituted into the format string. Note that the number of values in the collection on the right side corresponds with the number of ``%`` characters in the format string. Values are taken—in order, left to right—from the collection and inserted into the format string.

    Let’s look at both sides of this formatting expression in more detail. The format string may contain one or more conversion specifications. A conversion character tells the format operator what type of value is going to be inserted into that position in the string. In the example above, the ``%s`` specifies a string, while the ``%d`` specifies an integer. Other possible type specifications include ``i``, ``u``, ``f``, ``e``, ``g``, ``c``, or ``%``. `Table 9` summarizes all of the
    various type specifications.

    **Table 9: String Formatting Conversion Characters**

    | **Character** | **Output Format**                                                                                 |
    | ------------- | ------------------------------------------------------------------------------------------------- |
    | ``d``, ``i``  | Integer                                                                                           |
    | ``u``         | Unsigned integer                                                                                  |
    | ``f``         | Floating point as m.ddddd                                                                         |
    | ``e``         | Floating point as m.ddddde+/-xx                                                                   |
    | ``E``         | Floating point as m.dddddE+/-xx                                                                   |
    | ``g``         | Use ``%e`` for exponents less than :math:`-4` or greater than :math:`+5`, otherwise use ``%f``    |
    | ``c``         | Single character                                                                                  |
    | ``s``         | String, or any Python data object that can be converted to a string by using the ``str`` function |
    | ``%``         | Insert a literal ``%`` character                                                                  |

    In addition to the format character, you can also include a format modifier between the ``%`` and the format character. Format modifiers may be used to left-justify or right-justify the value with a specified field width. Modifiers can also be used to specify the field width along with a number of digits after the decimal point. :ref:`Table 10 <tab_fmtaddsa>` explains these format modifiers.

    **Table 10: Additional formatting options**

        
    | **Modifier** | **Example**  | **Description**                                                                                 |
    | ------------ | ------------ | ----------------------------------------------------------------------------------------------- |
    | number       | ``%20d``     | Put the value in a field width of 20                                                            |
    | ``-``        | ``%-20d``    | Put the value in a field 20 characters wide, left-justified                                     |
    | ``+``        | ``%+20d``    | Put the value in a field 20 characters wide, right-justified                                    |
    | ``0``        | ``%020d``    | Put the value in a field 20 characters wide, fill in with leading zeros                         |
    | ``.``        | ``%20.2f``   | Put the value in a field 20 characters wide with 2 characters to the right of the decimal point |
    | ``(name)``   | ``%(name)d`` | Get the value from the supplied dictionary using ``name`` as the key                            |

    As mentioned, the right side of the format operator is a collection of values that will be inserted into the format string. The collection will be either a tuple or a dictionary. If the collection is a tuple, the values are inserted in order of position. That is, the first element in the tuple corresponds to the first format character in the format string. If the collection is a dictionary, the values are inserted according to their keys. In this case all format characters must use the ``(name)`` modifier to specify the name of the key.

    ```pycon
    >>> price = 24
    >>> item = "banana"
    >>> print("The %s costs %d cents" % (item, price))
    The banana costs 24 cents
    >>> print("The %+10s costs %5.2f cents" % (item, price))
    The     banana costs 24.00 cents
    >>> print("The %+10s costs %10.2f cents" % (item, price))
    The     banana costs      24.00 cents
    >>> itemdict = {"item": "banana", "cost": 24}
    >>> print("The %(item)s costs %(cost)7.1f cents" % itemdict)
    The banana costs    24.0 cents
    ```

    In addition to format strings that use format characters and format modifiers, Python strings also include a ``format`` method that can be used in conjunction with a new ``Formatter`` class to implement complex string formatting. More about these features can be found in the Python library reference manual.

    ```pycon
    >>> print("The {} costs {} cents".format(item, price))
    The banana costs 24 cents
    >>> print("The {:s} costs {:d} cents".format(item, price))
    The banana costs 24 cents
    ```

    Python 3.6 introduced **f-strings**, a way to use proper variable names instead of placeholders. Formatting conversion symbols can still be used inside an f-string, but the alignment symbols are different from those used with placeholders (see `Table 11`). We are going to use this formatting method for the rest of the text.

    **Table 11: f-string Formatting Options**

    | **Modifier** | **Example** | **Description**                                                                                  |
    | ------------ | ----------- | ------------------------------------------------------------------------------------------------ |
    | number       | ``:20d``    | Put the value in a field width of 20                                                             |
    | ``<``        | ``:<20d``   | Put the value in a field 20 characters wide, left-aligned                                        |
    | ``>``        | ``:>20d``   | Put the value in a field 20 characters wide, right-aligned                                       |
    | ``^``        | ``:^20d``   | Put the value in a field 20 characters wide, center-aligned                                      |
    | ``0``        | ``:020d``   | Put the value in a field 20 characters wide, fill in with leading zeros.                         |
    | ``.``        | ``:20.2f``  | Put the value in a field 20 characters wide with 2 characters to the right of the decimal point. |

    ```pycon
    >>> print(f"The {item:10} costs {price:10.2f} cents")
    The banana     costs      24.00 cents
    >>> print(f"The {item:<10} costs {price:<10.2f} cents")
    The banana     costs 24.00      cents
    >>> print(f"The {item:^10} costs {price:^10.2f} cents")
    The   banana   costs   24.00    cents
    >>> print(f"The {item:>10} costs {price:>10.2f} cents")
    The     banana costs      24.00 cents
    >>> print(f"The {item:>10} costs {price:>010.2f} cents")
    The     banana costs 0000024.00 cents
    >>> itemdict = {"item": "banana", "price": 24}
    >>> print(f"Item:{itemdict['item']:.>10}\n" +
    ... f"Price:{'$':.>4}{itemdict['price']:5.2f}")
    Item:....banana
    Price:...$24.00
    ```

    More about these features can be found in the Python library reference manual.
