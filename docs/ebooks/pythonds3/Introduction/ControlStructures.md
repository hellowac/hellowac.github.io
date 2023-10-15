# 结构控制

正如我们之前提到的，算法需要两个重要的控制结构：迭代(iteration)和选择(selection)。 Python 以各种形式支持这两者。 程序员可以选择对于给定情况最有用的语句。

对于迭代，Python 提供了一个标准的`while`语句和一个非常强大的`for`语句。 只要条件计算结果为`True`，while 语句就会重复一段代码。 例如，

```pycon
>>> counter = 1
>>> while counter <= 5:
...     print("Hello, world")
...     counter = counter + 1
... 
Hello, world
Hello, world
Hello, world
Hello, world
Hello, world
```

打印出五次`Hello, world`短语。 `while` 语句上的条件在每次重复开始时进行评估。 如果条件计算结果为`True`，则语句的主体将执行。 由于 Python 语言强制执行强制缩进模式，因此很容易看到 Python while 语句的结构。

while 语句是一种非常通用的迭代结构，我们将在许多不同的算法中使用它。 在许多情况下，复合条件将控制迭代。 一个片段如

```pycon
while counter <= 10 and not done:
...
```

只会在条件的两个部分都满足的情况下才执行语句主体。 变量`counter`的值需要小于或等于10，并且变量`done`的值需要为`False`（`not False`是 `True`），这样``True and True`` 就会得到``True``。

尽管这种类型的构造在多种情况下都非常有用，但另一种迭代结构`for`语句可以与许多 Python 集合结合使用。 ``for`` 语句可用于迭代集合的成员，只要集合是一个序列。 所以，举例来说，

```pycon
>>> for item in [1, 3, 6, 2, 5]:
...    print(item)
...
1
3
6
2
5
```

将变量`item`指定为列表 `[1, 3, 6, 2, 5]` 中的每个连续值。 然后执行迭代的主体。 这适用于任何序列集合（列表、元组和字符串）。

``for`` 语句的常见用途是在一系列值上实现明确的迭代。 该声明

```pycon
>>> for item in range(5):
...    print(item ** 2)
...
0
1
4
9
16
```

将执行`print`函数五次。 `range`函数将返回一个表示序列 0、1、2、3、4 的范围对象，每个值将分配给变量`item`。 然后对该值进行平方并打印。

此迭代结构的另一个有用版本用于处理字符串的每个字符。 以下代码片段迭代字符串列表，并通过将每个字符串附加到列表来处理每个字符串。 结果是所有单词中所有字母的列表。

```python title="处理字符串列表中的每个字符(Activecode 8)"
word_list = ["cat", "dog", "rabbit"]
letter_list = [ ]
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)
print(letter_list)
```

选择语句允许程序员提出问题，然后根据结果执行不同的操作。 大多数编程语言提供了这个有用结构的两个版本：`if...else`和`if`。 二进制选择的一个简单示例使用`if...else`语句。

```pycon
>>> import math
>>> n = 16
>>> if n < 0:
...   print("Sorry, value is negative")
... else:
...   print(math.sqrt(n))
... 
4.0
```

在此示例中，检查`n`引用的对象以查看它是否小于零。 如果是，则会打印一条消息，指出结果是否定的。 如果不是，则该语句执行`else`子句并计算平方根。

与任何控制结构一样，选择结构可以嵌套，以便一个问题的结果有助于决定是否询问下一个问题。 例如，假设`score`是一个变量，保存对计算机科学测试分数的引用。

```pycon
>>> if score >= 90:
...     print("A")
... else:
...     if score >= 80:
...         print("B")
...     else:
...         if score >= 70:
...             print("C")
...         else:
...             if score >= 60:
...                 print("D")
...             else:
...                 print("F")
```

该片段将通过打印获得的字母等级来对称为“分数(score)”的值进行分类。 如果分数大于或等于 90，则语句将打印“A”。 如果不是（``else``），则询问下一个问题。 如果分数大于或等于 80，那么它必须在 80 到 89 之间，因为第一个问题的答案是错误的。 在这种情况下，打印“B”。 您可以看到，Python 缩进模式有助于理解`if`和`else`之间的关联，而不需要任何额外的语法元素。

这种类型的嵌套选择的替代语法使用`elif`关键字。 将`else`和下一个`if`组合起来，以便消除额外嵌套级别的需要。 请注意，如果所有其他条件均失败，最后的`else`仍然需要提供默认情况。

```pycon
>>> if score >= 90:
...     print("A")
... elif score >= 80:
...     print("B")
... elif score >= 70:
...     print("C")
... elif score >= 60:
...     print("D")
... else:
...     print("F")
```

Python 还有一个单向选择结构，即`if`语句。 使用此语句，如果条件为真，则执行操作。 在条件为假的情况下，处理简单地继续到`if`之后的下一个语句。 例如，以下片段将首先检查变量“n”的值是否为负数。 如果是，则通过绝对值函数对其进行修改。 无论如何，下一步是计算平方根。

```python
if n < 0:
    n = abs(n)
print(math.sqrt(n))
```

!!! info  "自检"

    通过尝试以下练习来测试您对我们迄今为止所涵盖内容的理解。 修改 Activecode 8 中的代码，以便最终列表仅包含每个字母的一个副本。

    ```python
    # the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
    ```

    <iframe width="560" height="315" src="https://www.youtube.com/embed/vJ_KDaJZ4f4" title="list unique" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

回到列表，还有一种创建列表的替代方法，该方法使用迭代和选择结构，称为**列表推导式(list comprehension)**。 列表推导式允许您根据某些处理或选择标准轻松创建列表。 例如，如果我们想创建前 10 个完全平方数的列表，我们可以使用`for`语句：

```pycon
>>> sq_list = []
>>> for x in range(1, 11):
...     sq_list.append(x * x)
... 
>>> sq_list
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

使用列表推导式，我们可以一步完成此操作，如下所示

```pycon
>>> sq_list=[x * x for x in range(1, 11)]
>>> sq_list
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

变量`x`采用由`for`结构指定的从1到10的值。 然后计算`x * x`的值并将其添加到正在构造的列表中。

列表推导式的通用语法还允许添加选择标准，以便仅添加某些项目。 例如，

```pycon
>>> sq_list=[x * x for x in range(1,11) if x % 2 != 0]
>>> sq_list
[1, 9, 25, 49, 81]
```

此列表推导式构造一个仅包含 1 到 10 范围内的奇数的平方的列表。任何支持迭代的序列都可以在列表推导式中使用来构造新列表。

```pycon
>>>[ch.upper() for ch in 'comprehension' if ch not in 'aeiou']
['C', 'M', 'P', 'R', 'H', 'N', 'S', 'N']
```

!!! info  "自检"

    通过使用列表推导式重做 Activecode 1 来测试您对列表推导式的理解。 对于额外的挑战，看看您是否能弄清楚如何删除重复项。

    ```python
    # the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']
    ```

    <iframe width="560" height="315" src="https://www.youtube.com/embed/pcrcYy9UlVM" title="listcomp" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

???- info "原文"

    **Control Structures**

    As we noted earlier, algorithms require two important control structures: iteration and selection. Both of these are supported by Python in various forms. The programmer can choose the statement that is most useful for the given circumstance.

    For iteration, Python provides a standard ``while`` statement and a very powerful ``for`` statement. The while statement repeats a body of code as long as a condition evaluates to ``True``. For example,

    ```pycon
    >>> counter = 1
    >>> while counter <= 5:
    ...     print("Hello, world")
    ...     counter = counter + 1
    ... 
    Hello, world
    Hello, world
    Hello, world
    Hello, world
    Hello, world
    ```

    prints out the phrase ``Hello, world`` five times. The condition on the ``while`` statement is evaluated at the start of each repetition. If the condition evaluates to ``True``, the body of the statement will execute. It is easy to see the structure of a Python ``while`` statement due to the mandatory indentation pattern that the language enforces.

    The ``while`` statement is a very general-purpose iterative structure that we will use in a number of different algorithms. In many cases, a compound condition will control the iteration. A fragment such as

    ```pycon
    while counter <= 10 and not done:
    ...
    ```

    would cause the body of the statement to be executed only in the case where both parts of the condition are satisfied. The value of the variable ``counter`` would need to be less than or equal to 10, and the value of the variable ``done`` would need to be ``False`` (``not False`` is ``True``) so that ``True and True`` results in ``True``.

    Even though this type of construct is very useful in a wide variety of situations, another iterative structure, the ``for`` statement, can be used in conjunction with many of the Python collections. The ``for`` statement can be used to iterate over the members of a collection, so long as the collection is a sequence. So, for example,

    ```pycon
    >>> for item in [1, 3, 6, 2, 5]:
    ...    print(item)
    ...
    1
    3
    6
    2
    5
    ```

    assigns the variable ``item`` to be each successive value in the list [1, 3, 6, 2, 5]. The body of the iteration is then executed. This works for any collection that is a sequence (lists, tuples, and strings).

    A common use of the ``for`` statement is to implement definite iteration over a range of values. The statement

    ```pycon
    >>> for item in range(5):
    ...    print(item ** 2)
    ...
    0
    1
    4
    9
    16
    ```

    will perform the ``print`` function five times. The ``range`` function will return a range object representing the sequence 0, 1, 2, 3, 4 and each value will be assigned to the variable ``item``. This value is then squared and printed.

    Another useful version of this iteration structure is used to process each character of a string. The following code fragment iterates over a list of strings and for each string processes each character by appending it to a list. The result is a list of all the letters in all of the words.

    ```python title="Processing Each Character in a List of Strings"
    word_list = ["cat", "dog", "rabbit"]
    letter_list = [ ]
    for a_word in word_list:
        for a_letter in a_word:
            letter_list.append(a_letter)
    print(letter_list)
    ```

    Selection statements allow programmers to ask questions and then, based on the result, perform different actions. Most programming languages provide two versions of this useful construct: the ``if...else`` and the ``if``. A simple example of a binary selection uses the ``if...else`` statement.

    ```pycon
    >>> import math
    >>> n = 16
    >>> if n < 0:
    ...   print("Sorry, value is negative")
    ... else:
    ...   print(math.sqrt(n))
    ... 
    4.0
    ```

    In this example, the object referred to by ``n`` is checked to see if it is less than zero. If it is, a message is printed stating that it is negative. If it is not, the statement performs the ``else`` clause and computes the square root.

    Selection constructs, as with any control construct, can be nested so that the result of one question helps decide whether to ask the next. For example, assume that ``score`` is a variable holding a reference to a score for a computer science test.

    ```pycon
    >>> if score >= 90:
    ...     print("A")
    ... else:
    ...     if score >= 80:
    ...         print("B")
    ...     else:
    ...         if score >= 70:
    ...             print("C")
    ...         else:
    ...             if score >= 60:
    ...                 print("D")
    ...             else:
    ...                 print("F")
    ```

    This fragment will classify a value called ``score`` by printing the letter grade earned. If the score is greater than or equal to 90, the statement will print ``A``. If it is not (``else``), the next question is asked. If the score is greater than or equal to 80, then it must be between 80 and 89 since the answer to the first question was false. In this case print ``B`` is printed. You can see that the Python indentation pattern helps to make sense of the association between ``if`` and ``else`` without requiring any additional syntactic elements.

    An alternative syntax for this type of nested selection uses the ``elif`` keyword. The ``else`` and the next ``if`` are combined so as to eliminate the need for additional nesting levels. Note that the final ``else`` is still necessary to provide the default case if all other conditions fail.

    ```pycon
    >>> if score >= 90:
    ...     print("A")
    ... elif score >= 80:
    ...     print("B")
    ... elif score >= 70:
    ...     print("C")
    ... elif score >= 60:
    ...     print("D")
    ... else:
    ...     print("F")
    ```

    Python also has a single-way selection construct, the ``if`` statement. With this statement, if the condition is true, an action is performed. In the case where the condition is false, processing simply continues on to the next statement after the ``if``. For example, the following fragment will first check to see if the value of a variable ``n`` is negative. If it is, then it is modified by the absolute value function. Regardless, the next action is to compute the square root.

    ```python
    if n < 0:
        n = abs(n)
    print(math.sqrt(n))
    ```

    !!! info  "Self Check"

        Test your understanding of what we have covered so far by trying the following exercise.  Modify the code from Activecode 8 so that the final list only contains a single copy of each letter.

        ```python
        # the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
        ```

        <iframe width="560" height="315" src="https://www.youtube.com/embed/vJ_KDaJZ4f4" title="list unique" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

    Returning to lists, there is an alternative method for creating a list that uses iteration and selection constructs known as a **list comprehension**. A list comprehension allows you to easily create a list based on some processing or selection criteria. For example, if we would like to create a list of the first 10 perfect squares, we could use a ``for`` statement:

    ```pycon
    >>> sq_list = []
    >>> for x in range(1, 11):
    ...     sq_list.append(x * x)
    ... 
    >>> sq_list
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    ```

    Using a list comprehension, we can do this in one step as

    ```pycon
    >>> sq_list=[x * x for x in range(1, 11)]
    >>> sq_list
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    ```

    The variable ``x`` takes on the values 1 through 10 as specified by the
    ``for`` construct. The value of ``x * x`` is then computed and added to
    the list that is being constructed.

    The general syntax for a list
    comprehension also allows a selection criteria to be added so that only
    certain items get added. For example,

    ```pycon
    >>> sq_list=[x * x for x in range(1,11) if x % 2 != 0]
    >>> sq_list
    [1, 9, 25, 49, 81]
    ```

    This list comprehension constructs a list that contains the
    squares of only the odd numbers in the range from 1 to 10. Any sequence that
    supports iteration can be used within a list comprehension to construct
    a new list.

    ```pycon
    >>>[ch.upper() for ch in 'comprehension' if ch not in 'aeiou']
    ['C', 'M', 'P', 'R', 'H', 'N', 'S', 'N']
    ```

    !!! info  "Self Check"

        Test your understanding of list comprehensions by redoing Activecode 1 using list comprehensions.  For an extra challenge, see if you can figure out how to remove the duplicates.

        ```python
        # the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']
        ```

        <iframe width="560" height="315" src="https://www.youtube.com/embed/pcrcYy9UlVM" title="listcomp" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
