# 内置原子数据类型

我们将通过考虑原子数据类型来开始我们的审查。 Python 有两个主要的内置数字类，它们实现**整数**和**浮点数据类型**。 这些 Python 类称为 `int` 和“float”。 标准算术运算符 +、-、\*、/ 和 \*\*（求幂）可以与括号一起使用，强制操作顺序偏离正常运算符优先级。 其他非常有用的运算符是**余数（模）运算符** (%) 和**整数除法** (//)。 请注意，当两个整数相除时，结果是浮点数。 整数除法运算符通过截断任何小数部分来返回商的整数部分。

```pycon title="Basic Arithmetic Operators"
>>> print(2 + 3 * 4)
14
>>> print((2 + 3) * 4)
20
>>> print(2 ** 10)
1024
>>> print(6 / 3)
2.0
>>> print(7 / 3)
2.3333333333333335
>>> print(7 // 3)
2
>>> print(7 % 3)
1
>>> print(3 / 6)
0.5
>>> print(3 // 6)
0
>>> print(3 % 6)
3
>>> print(2 ** 100)
1267650600228229401496703205376
```

布尔数据类型，作为Python `bool` 类实现，对于表示真值非常有用。 布尔对象的可能状态值是`True`和`False`，以及标准布尔运算符`and`、`or`和`not`。

```pycon
>>> True
True
>>> False
False
>>> False or True
True
>>> not (False or True)
False
>>> True and True
True
```

布尔数据对象还用作比较运算符的结果，例如**等于** (==) 和**大于** ($>$)。 此外，关系运算符和逻辑运算符可以组合在一起形成复杂的逻辑问题。 “表 1”显示了关系运算符和逻辑运算符，并在随后的会话中显示了示例。

**表 1: 关系运算符和逻辑运算符**

| **运算符名称** | **运算符** | **解释**                                   |
| -------------- | ---------- | ------------------------------------------ |
| 小于           | $<$        | 小于运算符                                 |
| 大于           | $>$        | 大于运算符                                 |
| 小于或等于     | $<=$       | 小于或等于运算符                           |
| 大于或等于     | $>=$       | 大于或等于运算符                           |
| 等于           | $==$       | 等于运算符                                 |
| 不等于         | $!=$       | 不等于运算符                               |
| 逻辑和         | $\and$     | 两个操作数都为 True 时结果为 True          |
| 逻辑或         | $\or$      | 一个或另一个操作数为 True 则结果为 True    |
| 逻辑非         | $\not$     | 否定真值，False 变为 True，True 变为 False |

```pycon title="基本关系和逻辑运算符"
>>> print(5 == 10)
False
>>> print(10 > 5)
True
>>> print((5 >= 1) and (5 <= 10))
True
>>> print((1 < 5) or (10 < 1))
True
>>> print(1 < 5 < 10)
True
```

标识符在编程语言中用作名称。 在 Python 中，标识符以字母或下划线 (_) 开头，区分大小写，并且可以是任意长度。 请记住，使用传达含义的名称始终是一个好主意，以便您的程序代码更易于阅读和理解。

当第一次在赋值语句的左侧使用名称时，就会创建 Python 变量。 赋值语句提供了一种将名称与值关联起来的方法。 该变量将保存对一段数据的引用，但不保存数据本身。 考虑以下会话：

```pycon
>>> the_sum = 0
>>> the_sum
0
>>> the_sum = the_sum + 1
>>> the_sum
1
>>> the_sum = True
>>> the_sum
True
```

赋值语句`the_sum = 0`创建一个名为`the_sum`的变量，并让它保存对数据对象`0`的引用（参见“图3”）。 通常，对赋值语句的右侧进行求值，并对结果数据对象的引用分配给左侧的名称。 在我们的示例中，此时变量的类型是整数，因为这是`the_sum`当前引用的数据的类型。 如果数据类型发生变化（参见“图 4”），如上面布尔值`True`所示，变量的类型也会发生变化（`the_sum`现在是布尔类型）。 赋值语句更改变量所持有的引用。 这是Python的动态特性。 同一变量可以引用许多不同类型的数据。

<figure markdown>
![Image title](./Figures/assignment1.png)
<figcaption>图 3：变量保存对数据对象的引用</figcaption>
</figure>

<figure markdown>
![Image title](./Figures/assignment2.png)
<figcaption>图 4：分配改变引用</figcaption>
</figure>

???- info "原文"

    **Built-in Atomic Data Types**

    We will begin our review by considering the atomic data types. Python has two main built-in numeric classes that implement the integer and floating-point data types. These Python classes are called ``int`` and ``float``. The standard arithmetic operators, +, -, \*, /, and \*\* (exponentiation), can be used with parentheses forcing the order of operations away from normal operator precedence. Other very useful operators are the remainder (modulo) operator (%) and integer division (//). Note that when two integers are divided, the result is a floating point. The integer division operator returns the integer portion of the quotient by truncating any fractional part.

    ```pycon title="Basic Arithmetic Operators"
    >>> print(2 + 3 * 4)
    14
    >>> print((2 + 3) * 4)
    20
    >>> print(2 ** 10)
    1024
    >>> print(6 / 3)
    2.0
    >>> print(7 / 3)
    2.3333333333333335
    >>> print(7 // 3)
    2
    >>> print(7 % 3)
    1
    >>> print(3 / 6)
    0.5
    >>> print(3 // 6)
    0
    >>> print(3 % 6)
    3
    >>> print(2 ** 100)
    1267650600228229401496703205376
    ```


    The Boolean data type, implemented as the Python ``bool`` class, will be quite useful for representing truth values. The possible state values for a Boolean object are ``True`` and ``False`` with the standard Boolean operators, ``and``, ``or``, and ``not``.

    ```pycon
    >>> True
    True
    >>> False
    False
    >>> False or True
    True
    >>> not (False or True)
    False
    >>> True and True
    True
    ```

    Boolean data objects are also used as results for comparison operators such as equality (==) and greater than ($>$). In addition, relational operators and logical operators can be combined together to form complex logical questions. `Table 1` shows the relational and logical operators with examples shown in the session that follows.

    **Table 1: Relational and Logical Operators**

    | **Operation Name**    | **Operator** | **Explanation**                                                 |
    | --------------------- | ------------ | --------------------------------------------------------------- |
    | less than             | $<$          | Less than operator                                              |
    | greater than          | $>$          | Greater than operator                                           |
    | less than or equal    | $<=$         | Less than or equal to operator                                  |
    | greater than or equal | $>=$         | Greater than or equal to operator                               |
    | equal                 | $==$         | Equality operator                                               |
    | not equal             | $!=$         | Not equal operator                                              |
    | logical and           | $\and$       | Both operands True for result to be True                        |
    | logical or            | $\or$        | One or the other operand is True for the result to be True      |
    | logical not           | $\not$       | Negates the truth value, False becomes True, True becomes False |
        

    ```pycon title="Basic Relational and Logical Operators"
    >>> print(5 == 10)
    False
    >>> print(10 > 5)
    True
    >>> print((5 >= 1) and (5 <= 10))
    True
    >>> print((1 < 5) or (10 < 1))
    True
    >>> print(1 < 5 < 10)
    True
    ```

    Identifiers are used in programming languages as names. In Python, identifiers start with a letter or an underscore (_), are case sensitive, and can be of any length. Remember that it is always a good idea to use names that convey meaning so that your program code is easier to read and understand.

    A Python variable is created when a name is used for the first time on the left-hand side of an assignment statement. Assignment statements provide a way to associate a name with a value. The variable will hold a reference to a piece of data but not the data itself. Consider the following session:

    ```pycon
    >>> the_sum = 0
    >>> the_sum
    0
    >>> the_sum = the_sum + 1
    >>> the_sum
    1
    >>> the_sum = True
    >>> the_sum
    True
    ```

    The assignment statement ``the_sum = 0`` creates a variable called
    ``the_sum`` and lets it hold the reference to the data object ``0`` (see
    `Figure 3`). In general, the right-hand side of the assignment
    statement is evaluated and a reference to the resulting data object is
    assigned to the name on the left-hand side. At this point in our
    example, the type of the variable is integer as that is the type of the
    data currently being referred to by ``the_sum``. If the type of the data
    changes (see `Figure 4`), as shown above with the Boolean
    value ``True``, so does the type of the variable (``the_sum`` is now of
    the type Boolean). The assignment statement changes the reference being
    held by the variable. This is a dynamic characteristic of Python. The
    same variable can refer to many different types of data.
        
    <figure markdown>
    ![Image title](./Figures/assignment1.png)
    <figcaption>Figure 3: Variables Hold References to Data Objects</figcaption>
    </figure>
        
    <figure markdown>
    ![Image title](./Figures/assignment2.png)
    <figcaption>Figure 4: Assignment Changes the Reference</figcaption>
    </figure>
