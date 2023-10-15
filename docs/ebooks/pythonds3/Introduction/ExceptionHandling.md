# 异常处理

编写程序时通常会出现两种类型的错误。 第一个被称为 *语法错误(syntax error)* ，仅仅意味着程序员在语句或表达式的结构中犯了错误。 例如，编写 for 语句而忘记冒号是不正确的。

```pycon
>>> for i in range(10)
File "<stdin>", line 1
    for i in range(10)
                    ^
SyntaxError: invalid syntax
```

在这种情况下，Python解释器发现它无法完成这条指令的处理，因为它不符合语言的规则。 当您第一次学习语言时，语法错误通常会更频繁。

另一种类型的错误称为*逻辑错误(logic error)*，表示程序执行但给出错误结果的情况。 这可能是由于底层算法中的错误或该算法的翻译中的错误造成的。 在某些情况下，逻辑错误会导致非常糟糕的情况，例如尝试除以零或尝试访问列表中的项目，但该项目的索引超出了列表的边界。 在这种情况下，逻辑错误会导致运行时错误，从而导致程序终止。 这些类型的运行时错误通常称为**异常**。

大多数时候，初级程序员只是将异常视为导致执行结束的致命运行时错误。 然而，大多数编程语言都提供了一种处理这些错误的方法，允许程序员进行某种类型的干预（如果他们愿意的话）。 此外，如果程序员在程序执行中检测到有必要的情况，则可以创建自己的异常。

当异常发生时，我们说它已被*引发(raised)*。 您可以使用`try`语句*处理(handle)*引发的异常。 例如，考虑以下会话，该会话要求用户提供一个整数，然后调用数学库中的平方根函数。 如果用户输入大于或等于0的值，则打印将显示平方根。 但是，如果用户输入负值，平方根函数将报告`ValueError`异常。

```pycon
>>> import math
>>> a_number = int(input("Please enter an integer "))
Please enter an integer -23
>>> print(math.sqrt(a_number))
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ValueError: math domain error
```

我们可以通过从`try`块中调用`print`函数来处理此异常。 相应的`except`块 *捕获(catches)* 异常，并在发生异常时向用户打印一条消息。 例如：

```pycon
>>> try:
...   print(math.sqrt(a_number))
... except:
...   print("Bad value for the square root function")
...   print("Using the absolute value instead")
...   print(math.sqrt(abs(a_number)))
... 
Bad value for the square root function
Using the absolute value instead
4.795831523312719
```

将捕获`sqrt`引发异常的事实，并将消息打印回用户并使用绝对值来确保我们正在取非负数的平方根。 这意味着程序不会终止，而是继续执行下一条语句。

程序员也有可能通过使用`raise`语句引起运行时异常。 例如，我们可以先检查该值，然后引发自己的异常，而不是使用负数调用平方根函数。 下面的代码片段显示了创建新的`RuntimeError`异常的结果。 请注意，程序仍然会终止，但现在导致终止的异常是由程序员显式创建的。

```pycon
>>> if a_number < 0:
...   raise RuntimeError("You can't use a negative number")
... else:
...   print(math.sqrt(a_number))
... 
Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
RuntimeError: You can't use a negative number
```

除了上面显示的`RuntimeError`之外，还可以引发多种异常。 有关所有可用异常类型的列表以及如何创建自己的异常类型，请参阅 Python 参考手册。

???- info "原文"

    **Exception Handling**

    There are two types of errors that typically occur when writing programs. The first, known as a *syntax error*, simply means that the programmer has made a mistake in the structure of a statement or expression. For example, it is incorrect to write a for statement and forget the colon.

    ```pycon
    >>> for i in range(10)
    File "<stdin>", line 1
        for i in range(10)
                        ^
    SyntaxError: invalid syntax
    ```

    In this case, the Python interpreter has found that it cannot complete the processing of this instruction since it does not conform to the rules of the language. Syntax errors are usually more frequent when you are first learning a language.

    The other type of error, known as a *logic error*, denotes a situation where the program executes but gives the wrong result. This can be due to an error in the underlying algorithm or an error in your translation of that algorithm. In some cases, logic errors lead to very bad situations such as trying to divide by zero or trying to access an item in a list where the index of the item is outside the bounds of the list. In this case, the logic error leads to a runtime error that causes the program to terminate. These types of runtime errors are typically called **exceptions**.

    Most of the time, beginning programmers simply think of exceptions as fatal runtime errors that cause the end of execution. However, most programming languages provide a way to deal with these errors that will allow the programmer to have some type of intervention if they so choose. In addition, programmers can create their own exceptions if they detect a situation in the program execution that warrants it.

    When an exception occurs, we say that it has been *raised*. You can *handle* the exception that has been raised by using a ``try`` statement. For example, consider the following session that asks the user for an integer and then calls the square root function from the math library. If the user enters a value that is greater than or equal to 0, the print will show the square root. However, if the user enters a negative value, the square root function will report a ``ValueError`` exception.

    ```pycon
    >>> import math
    >>> a_number = int(input("Please enter an integer "))
    Please enter an integer -23
    >>> print(math.sqrt(a_number))
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    ValueError: math domain error
    ```

    We can handle this exception by calling the ``print`` function from within a ``try`` block. A corresponding ``except`` block “catches” the exception and prints a message back to the user in the event that an exception occurs. For example:

    ```pycon
    >>> try:
    ...   print(math.sqrt(a_number))
    ... except:
    ...   print("Bad value for the square root function")
    ...   print("Using the absolute value instead")
    ...   print(math.sqrt(abs(a_number)))
    ... 
    Bad value for the square root function
    Using the absolute value instead
    4.795831523312719
    ```

    will catch the fact that an exception is raised by ``sqrt`` and will instead print the messages back to the user and use the absolute value to be sure that we are taking the square root of a non-negative number. This means that the program will not terminate but instead will continue on to the next statements.

    It is also possible for a programmer to cause a runtime exception by using the ``raise`` statement. For example, instead of calling the square root function with a negative number, we could have checked the value first and then raised our own exception. The code fragment below shows the result of creating a new ``RuntimeError`` exception. Note that the program would still terminate, but now the exception that caused the termination is something explicitly created by the programmer.

    ```pycon
    >>> if a_number < 0:
    ...   raise RuntimeError("You can't use a negative number")
    ... else:
    ...   print(math.sqrt(a_number))
    ... 
    Traceback (most recent call last):
        File "<stdin>", line 2, in <module>
    RuntimeError: You can't use a negative number
    ```

    There are many kinds of exceptions that can be raised in addition to the ``RuntimeError`` shown above. See the Python reference manual for a list of all the available exception types and for how to create your own.
