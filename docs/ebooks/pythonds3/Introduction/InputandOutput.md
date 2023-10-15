# 输入和输出

我们经常需要与用户交互，要么获取数据，要么提供某种结果。 如今，大多数程序都使用对话框来要求用户提供某种类型的输入。 虽然 Python 确实有一种创建对话框的方法，但我们可以使用一个更简单的函数。 Python 为我们提供了一个函数，允许我们要求用户输入一些数据并以字符串的形式返回对数据的引用。 该函数称为`input`。

Python 的函数`input`接受一个字符串参数。 该字符串通常称为 **提示(prompt)**，因为它包含一些有用的文本，提示用户输入某些内容。 例如，您可以按如下方式调用输入：

```python
a_name = input("Please enter your name: ")
```

现在，无论用户在提示后输入什么内容，都将存储在`a_name`变量中。 使用`input`函数，我们可以轻松编写指令，提示用户输入数据，然后将该数据合并到进一步处理中。 例如，在以下两个语句中，第一个语句询问用户的姓名，第二个语句根据提供的字符串打印一些简单处理的结果。

```python title="The input Function Returns a String"
a_name = input("Please enter your name: ")
print("Your name in all capitals is", a_name.upper(),
        "and has length", len(a_name))
```

值得注意的是，从`input`函数返回的值将是一个字符串，表示在提示后输入的确切字符。 如果您希望将此字符串解释为另一种类型，则必须显式提供类型转换。 在下面的语句中，用户输入的字符串被转换为浮点数，以便可以用于进一步的算术处理。

```pycon
>>> s_radius = input("Please enter the radius of the circle ")
Please enter the radius of the circle 10
>>> s_radius
'10'
>>> radius = float(s_radius)
>>> radius
10.0
>>> diameter = 2 * radius
>>> diameter
20.0
```

???- info "原文"

    **Input and Output**

    We often have a need to interact with users, either to get data or to provide some sort of result. Most programs today use a dialog box as a way of asking the user to provide some type of input. While Python does have a way to create dialog boxes, there is a much simpler function that we can use. Python provides us with a function that allows us to ask a user to enter some data and returns a reference to the data in the form of a string. The function is called ``input``.

    Python’s function ``input`` takes a single parameter that is a string. This string is often called the **prompt** because it contains some helpful text prompting the user to enter something. For example, you might call input as follows:

    ```python
    a_name = input("Please enter your name: ")
    ```

    Now whatever the user types after the prompt will be stored in the ``a_name`` variable. Using the ``input`` function, we can easily write instructions that will prompt the user to enter data and then incorporate that data into further processing. For example, in the following two statements, the first asks the user for their name and the second prints the result of some simple processing based on the string that is provided.

    ```python title="The input Function Returns a String"
    a_name = input("Please enter your name: ")
    print("Your name in all capitals is", a_name.upper(),
            "and has length", len(a_name))
    ```

    It is important to note that the value returned from the ``input`` function will be a string representing the exact characters that were entered after the prompt. If you want this string interpreted as another type, you must provide the type conversion explicitly. In the statements below, the string that is entered by the user is converted to a float so that it can be used in further arithmetic processing.

    ```pycon
    >>> s_radius = input("Please enter the radius of the circle ")
    Please enter the radius of the circle 10
    >>> s_radius
    '10'
    >>> radius = float(s_radius)
    >>> radius
    10.0
    >>> diameter = 2 * radius
    >>> diameter
    20.0
    ```
