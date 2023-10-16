# 一个`Fraction`类

显示实现用户定义类的细节的一个非常常见的示例是构造一个类来实现抽象数据类型“Fraction”。 我们已经看到Python提供了许多数字类供我们使用。 然而，有时最合适的做法是能够创建对用户来说看起来像分数的数据对象。

诸如 $\frac {3}{5}$ 之类的分数由两部分组成。 最上面的值称为分子，可以是任何整数。 底部的值称为分母，可以是任何大于 0 的整数（负分数的分子为负）。 尽管可以为任何分数创建浮点近似值，但在这种情况下，我们希望将分数表示为精确值。

“Fraction” 类型的操作将允许“Fraction” 数据对象的行为与任何其他数值相同。 我们需要能够进行分数的加、减、乘、除运算。 我们还希望能够使用标准的“斜杠”形式显示分数，例如 3/5。 此外，所有分数方法都应以最低项返回结果，以便无论执行什么计算，我们总是会得到最常见的形式。

在Python中，我们通过提供一个名称和一组语法上与函数定义类似的方法定义来定义一个新类。 对于这个例子，

```python
    class Fraction:
       # the methods go here
```

为我们定义方法提供了框架。 所有类都应该提供的第一个方法是构造函数。 构造函数定义了创建数据对象的方式。 要创建“Fraction”对象，我们需要提供两个数据，分子和分母。 在 Python 中，构造函数方法始终称为`__init__`（“init”前后各有两个下划线），如“清单 2”所示。

**清单 2**

```python
    class Fraction:
        """Class Fraction"""
        def __init__(self, top, bottom):
            """Constructor definition"""
            self.num = top
            self.den = bottom
```

请注意，形式参数列表包含三个项目（“self”、“top”、“bottom”）。 “self” 是一个特殊参数，始终用作对象本身的引用。 它必须始终是第一个形式参数； 然而，在调用时永远不会给它一个实际的参数值。 如前所述，分数需要两个状态数据：分子和分母。 构造函数中的符号“self.num”将“Fraction”对象定义为具有一个名为“num”的内部数据对象作为其状态的一部分。 同样，“self.den”创建分母。 两个形式参数的值最初分配给状态，允许新的“Fraction”对象知道其起始值。

要创建“Fraction”类的实例，我们必须调用构造函数。 这是通过使用类的名称并传递必要状态的实际值来实现的（请注意，我们从不直接“调用(invoke) `__init__` ”）。 例如，

```python
    my_fraction = Fraction(3, 5)
```

创建一个名为 ``my_fraction`` 的对象，表示分数 $`\frac {3}{5}$ （五分之三）。 “图 5”显示了该对象现在的实现情况。

<figure markdown>
  ![Image title](./Figures/fraction1.png)
  <figcaption>图 5：“Fraction”类的实例</figcaption>
</figure>

接下来我们需要做的是实现抽象数据类型所需的行为。 首先，考虑一下当我们尝试打印“Fraction”对象时会发生什么。

```python
>>> my_fraction = Fraction(3, 5)
>>> print(my_fraction)
<__main__.Fraction object at 0x103203eb8>
```

“Fraction” 对象“my_fraction” 不知道如何响应此打印请求。 “print”函数要求对象将自身转换为字符串，以便可以将该字符串写入输出。 my_fraction 唯一的选择是显示存储在变量中的实际引用（地址本身）。 这不是我们想要的。

我们有两种方法可以解决这个问题。 一种是定义一个名为“show”的方法，该方法允许“Fraction”对象将其自身打印为字符串。 我们可以实现这个方法，如“清单 3”所示。 如果我们像以前一样创建一个“Fraction”对象，我们可以要求它显示自己（换句话说，以正确的格式打印自己）。 不幸的是，这通常不起作用。 为了使打印正常工作，我们需要告诉“Fraction”类如何将其自身转换为字符串。 这就是“print”函数完成其工作所需要的。

**清单 3**

```python
    def show(self):
            print(f"{self.num}/{self.den}")
```

```pycon
    >>> my_fraction = Fraction(3, 5)
    >>> my_fraction.show()
    3/5
    >>> print(my_fraction)
    <__main__.Fraction object at 0x40bce9ac>
```

在Python中，所有类都提供了一组标准方法，但这些方法可能无法正常工作。 其中之一`__str__`是将对象转换为字符串的方法。 正如我们已经看到的，此方法的默认实现是返回实例地址字符串。 我们需要做的是为这个方法提供一个更好的实现。 我们会说这个实现**覆盖(overrides)**前一个实现，或者它重新定义了方法的行为。

为此，我们只需定义一个名为`__str__`的方法，并为其提供一个新的实现，如“清单 4”所示。 除了特殊参数“self”之外，这个定义不需要任何其他信息。 反过来，该方法将通过将每段内部状态数据转换为字符串，然后使用字符串连接在字符串之间放置“/”字符来构建字符串表示形式。 每当要求“Fraction”对象将其自身转换为字符串时，都会返回结果字符串。 请注意该函数的各种使用方式。

**清单 4**

```python
    def __str__(self):
        return f"{self.num}/{self.den}"
```

```pycon
>>> my_fraction = Fraction(3, 5)
>>> print(my_fraction)
3/5
>>> print(f"I ate {my_fraction} of pizza")
I ate 3/5 of pizza
>>> my_fraction.__str__()
'3/5'
>>> str(my_fraction)
'3/5'
```

我们可以为新的“Fraction”类重写许多其他方法。 其中最重要的一些是基本算术运算。 我们希望能够创建两个“Fraction”对象，然后使用标准“+”符号将它们加在一起。 此时，如果我们尝试将两个分数相加，我们会得到以下结果：

```pycon
    >>> f1 = Fraction(1, 4)
    >>> f2 = Fraction(1, 2)
    >>> f1 + f2
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'Fraction' and 'Fraction'
```

如果仔细观察该错误，您会发现问题在于“+”运算符不理解“Fraction”操作数。 我们可以通过为“Fraction”类提供一个覆盖加法方法的方法来解决这个问题。 在Python中，这个方法被称为``__add__``，它需要两个参数。 第一个“self”始终是必需的，第二个表示表达式中的另一个操作数。 例如，

```python
    f1.__add__(f2)
```

会要求 ``Fraction`` 对象 ``f1`` 将 ``Fraction`` 对象 ``f2`` 添加到自身。 这可以用标准符号`f1 + f2`来写。

两个分数必须具有相同的分母才能相加。 确保它们具有相同分母的最简单方法是简单地使用两个分母的乘积作为公分母，以便 $\frac {a}{b} + \frac {c}{d} = \frac {ad}{bd} + \frac {cb}{bd} = \frac{ad+cb}{bd}$。 其实现如“清单 5”所示。 加法函数返回一个新的“Fraction”对象，其中包含总和的分子和分母。 我们可以通过编写包含分数的标准算术表达式，分配加法结果，然后打印结果来使用此方法。

**清单 5**

```python
def __add__(self, other_fraction):
    new_num = self.num *other_fraction.den + \
                self.den* other_fraction.num
    new_den = self.den * other_fraction.den

    return Fraction(new_num, new_den)
```

```pycon
    >>> f1 = Fraction(1, 4)
    >>> f2 = Fraction(1, 2)
    >>> print(f1 + f2)
    6/8
```

加法方法如我们所愿，但有一点可以做得更好。 请注意，$6/8$ 是正确的结果 ($\frac {1}{4} + \frac {1}{2}$)，但它不是“最低项”表示形式。 最好的代表是 $3/4$。 为了确保我们的结果始终是最低的，我们需要一个知道如何减少分数的辅助函数。 该函数需要寻找**最大公约数**（GCD）。 然后我们可以将分子和分母除以 GCD，结果将简化为最低项。

寻找最大公约数的最著名算法是欧几里得算法，该算法将在第 8 章中详细讨论。它指出两个整数 $m$ 和 $n$ 的最大公约数是 $n$，如果 $n$ 平分$m$。 但是，如果 $n$ 不能整除 $m$，则答案是 $n$ 的最大公约数和 $m$ 除以 $n$ 的余数。 我们将在这里简单地提供一个迭代实现（参见“ActiveCode 1”）。 请注意，GCD 算法的这种实现仅在分母为正时才有效。 这对于我们的分数类是可以接受的，因为我们已经说过负分数将由负分子表示。

```python title="最大公约数函数"

    def gcd(m, n):
        while m % n != 0:
            m, n = n, m % n
        return n

    print(gcd(20, 10))
```

现在我们可以使用这个函数来帮助减少任何分数。 为了将分数转化为最简形式，我们将分子和分母除以它们的最大公约数。 因此，对于分数 $6/8$，最大公约数是 2。将顶部和底部除以 2 创建一个新分数 $3/4$（参见“清单 6”）。

**清单 6**

```python
def __add__(self, other_fraction):
    new_num = self.num * other_fraction.den + \
                    self.den * other_fraction.num
    new_den = self.den * other_fraction.den
    common = gcd(new_num, new_den)
    return Fraction(new_num // common, new_den // common)
```

我们的“Fraction”对象现在有两个非常有用的方法，如“图 6”所示。

<figure markdown>
  ![Image title](./Figures/fraction2.png)
  <figcaption>图 6：具有两个方法的“Fraction”类的实例</figcaption>
</figure>

```pycon
>>> f1 = Fraction(1, 4)
>>> f2 = Fraction(1, 2)
>>> print(f1 + f2)
3/4
```

我们需要在示例“Fraction”类中包含的另一组方法将允许两个分数相互比较。 假设我们有两个“Fraction”对象，“f1”和“f2”。 仅当它们是对同一对象的引用时，“f1==f2”才会为“True”。 在此实现下，具有相同分子和分母的两个不同对象将不相等。 这称为**浅平等**（参见“图 7”）。

<figure markdown>
  ![Image title](./Figures/fraction3.png)
  <figcaption>图 7：浅层平等与深度平等</figcaption>
</figure>

我们可以通过重写`__eq__`方法来创建**深度相等(deep equality)**——通过相同的值而不是相同的引用来相等（参见“图7”）。 `__eq__` 方法是任何类中可用的另一个标准方法。 `__eq__` 方法比较两个对象，如果它们的值相同则返回“True”，否则返回“False”。

在“Fraction”类中，我们可以通过再次将两个分数放入常用项中，然后比较分子来实现`__eq__`方法（参见“清单 7”）。 值得注意的是，还有其他可以被覆盖的关系运算符。 例如，``__le__`` 方法提供小于或等于功能。

**清单 7**

```python
def __eq__(self, other_fraction):
    first_num = self.num * other_fraction.den
    second_num = other_fraction.num * self.den

    return first_num == second_num
```

到目前为止，完整的“Fraction”类显示在“ActiveCode 2”中。 我们将剩下的算术和关系方法留作练习。

```python title="分数类"
def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den \
        + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        cmmn = gcd(new_num, new_den)
        return Fraction(new_num // cmmn, new_den // cmmn)

    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))

x = Fraction(1, 2)
x.show()
y = Fraction(2, 3)
print(y)
print(x + y)
print(x == y)
```

!!! info "Self  Check"

   为了确保您了解如何在 Python 类中实现运算符以及如何正确编写方法，请编写一些方法来实现 ``*, /,`` 和 ``-`` 。 还实现比较运算符 `>` 和 `<`

<iframe width="560" height="315" src="https://www.youtube.com/embed/gFb9tvJZHXo" title="fraction" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

???- info "原文"

    **A ``Fraction`` Class**

    A very common example to show the details of implementing a user-defined class is to construct a class to implement the abstract data type ``Fraction``. We have already seen that Python provides a number of numeric classes for our use. There are times, however, that it would be most appropriate to be able to create data objects that look like fractions to the user.

    A fraction such as $\frac {3}{5}$ consists of two parts. The top value, known as the numerator, can be any integer. The bottom value, called the denominator, can be any integer greater than 0 (negative fractions have a negative numerator). Although it is possible to create a floating point approximation for any fraction, in this case we would like to represent the fraction as an exact value.

    The operations for the ``Fraction`` type will allow a ``Fraction`` data object to behave like any other numeric value. We need to be able to add, subtract, multiply, and divide fractions. We also want to be able to show fractions using the standard “slash” form, for example 3/5. In addition, all fraction methods should return results in their lowest terms so that no matter what computation is performed, we always end up with the most common form.

    In Python, we define a new class by providing a name and a set of method definitions that are syntactically similar to function definitions. For this example,

    ```python
        class Fraction:
        # the methods go here
    ```

    provides the framework for us to define the methods. The first method that all classes should provide is the constructor. The constructor defines the way in which data objects are created. To create a ``Fraction`` object, we will need to provide two pieces of data, the numerator and the denominator. In Python, the constructor method is always called __init__ (two underscores before and after ``init``), as shown in `Listing 2`.

    .. _lst_pyconstructor:

    **Listing 2**

    ```python
        class Fraction:
            """Class Fraction"""
            def __init__(self, top, bottom):
                """Constructor definition"""
                self.num = top
                self.den = bottom
    ```

    Notice that the formal parameter list contains three items (``self``, ``top``, ``bottom``). ``self`` is a special parameter that will always be used as a reference back to the object itself. It must always be the first formal parameter; however, it will never be given an actual parameter value upon invocation. As described earlier, fractions require two pieces of state data, the numerator and the denominator. The notation ``self.num`` in the constructor defines the ``Fraction`` object to have an internal data object called ``num`` as part of its state. Likewise, ``self.den`` creates the denominator. The values of the two formal parameters are initially assigned to the state, allowing the new ``Fraction`` object to know its starting value.

    To create an instance of the ``Fraction`` class, we must invoke the constructor. This happens by using the name of the class and passing actual values for the necessary state (note that we never directly ``invoke __init__``). For example,

    ```python
        my_fraction = Fraction(3, 5)
    ```

    creates an object called ``my_fraction`` representing the fraction $`\frac {3}{5}$ (three-fifths). `Figure 5` shows this object as it is now implemented.

    <figure markdown>
    ![Image title](./Figures/fraction1.png)
    <figcaption>Figure 5: An Instance of the ``Fraction`` Class</figcaption>
    </figure>

    The next thing we need to do is implement the behavior that the abstract data type requires. To begin, consider what happens when we try to print a ``Fraction`` object.

    ```python
    >>> my_fraction = Fraction(3, 5)
    >>> print(my_fraction)
    <__main__.Fraction object at 0x103203eb8>
    ```

    The ``Fraction`` object, ``my_fraction``, does not know how to respond to this request to print. The ``print`` function requires that the object convert itself into a string so that the string can be written to the output. The only choice ``my_fraction`` has is to show the actual reference that is stored in the variable (the address itself). This is not what we want.

    There are two ways we can solve this problem. One is to define a method called ``show`` that will allow the ``Fraction`` object to print itself as a string. We can implement this method as shown in `Listing 3`. If we create a ``Fraction`` object as before we can ask it to show itself (in other words, print itself  in the proper format). Unfortunately, this does not work in general. In order to make printing work properly, we need to tell the ``Fraction`` class how to convert itself into a string. This is what the ``print`` function needs in order to do its job.

    **Listing 3**

    ```python
        def show(self):
                print(f"{self.num}/{self.den}")
    ```

    ```pycon
        >>> my_fraction = Fraction(3, 5)
        >>> my_fraction.show()
        3/5
        >>> print(my_fraction)
        <__main__.Fraction object at 0x40bce9ac>
    ```

    In Python, all classes have a set of standard methods that are provided but may not work properly. One of these, ``__str__``, is the method to convert an object into a string. The default implementation for this method is to return the instance address string as we have already seen. What we need to do is provide a better implementation for this method. We will say that this implementation __overrides__ the previous one, or that it redefines the method’s behavior.

    To do this, we simply define a method with the name ``__str__`` and give it a new implementation as shown in `Listing 4`. This definition does not need any other information except the special parameter ``self``. In turn, the method will build a string representation by converting each piece of internal state data to a string and then placing a ``/`` character in between the strings using string concatenation. The resulting string will be returned any time a ``Fraction`` object is asked to convert itself to a string. Notice the various ways that this function is used.

    **Listing 4**

    ```python
        def __str__(self):
            return f"{self.num}/{self.den}"
    ```

    ```pycon
    >>> my_fraction = Fraction(3, 5)
    >>> print(my_fraction)
    3/5
    >>> print(f"I ate {my_fraction} of pizza")
    I ate 3/5 of pizza
    >>> my_fraction.__str__()
    '3/5'
    >>> str(my_fraction)
    '3/5'
    ```

    We can override many other methods for our new ``Fraction`` class. Some of the most important of these are the basic arithmetic operations. We would like to be able to create two ``Fraction`` objects and then add them together using the standard ``+`` notation. At this point, if we try to add two fractions, we get the following:

    ```pycon
        >>> f1 = Fraction(1, 4)
        >>> f2 = Fraction(1, 2)
        >>> f1 + f2
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: unsupported operand type(s) for +: 'Fraction' and 'Fraction'
    ```

    If you look closely at the error, you see that the problem is that the ``+`` operator does not understand the ``Fraction`` operands. We can fix this by providing the ``Fraction`` class with a method that overrides the addition method. In Python, this method is called ``__add__`` and it requires two parameters. The first, ``self``, is always needed, and the second represents the other operand in the expression. For example,

    ```python
        f1.__add__(f2)
    ```

    would ask the ``Fraction`` object ``f1`` to add the ``Fraction`` object
    ``f2`` to itself. This can be written in the standard notation,
    ``f1 + f2``.

    Two fractions must have the same denominator to be added. The easiest way to make sure they have the same denominator is to simply use the product of the two denominators as a common denominator so that $\frac {a}{b} + \frac {c}{d} = \frac {ad}{bd} + \frac {cb}{bd} = \frac{ad+cb}{bd}$. The implementation is shown in `Listing 5`. The addition function returns a new ``Fraction`` object with the numerator and denominator of the sum. We can use this method by writing a standard arithmetic expression involving fractions, assigning the result of the addition, and then printing our result.

    .. _lst_addmethod:

    **Listing 5**

    ```python
    def __add__(self, other_fraction):
        new_num = self.num *other_fraction.den + \
                    self.den* other_fraction.num
        new_den = self.den * other_fraction.den

        return Fraction(new_num, new_den)
    ```

    ```pycon
        >>> f1 = Fraction(1, 4)
        >>> f2 = Fraction(1, 2)
        >>> print(f1 + f2)
        6/8
    ```

    The addition method works as we desire, but one thing could be better. Note that $6/8$ is the correct result ($\frac {1}{4} + \frac {1}{2}$) but that it is not in the “lowest terms” representation. The best representation would be $3/4$. In order to be sure that our results are always in the lowest terms, we need a helper function that knows how to reduce fractions. This function will need to look for the greatest common divisor, or GCD. We can then divide the numerator and the denominator by the GCD and the result will be reduced to lowest terms.

    The best-known algorithm for finding the greatest common divisor is Euclid’s algorithm, which will be discussed in detail in Chapter 8. It states that the greatest common divisor of two integers $m$ and $n$ is $n$ if $n$ divides $m$ evenly. However, if $n$ does not divide $m$ evenly, then the answer is the greatest common divisor of $n$ and the remainder of $m$ divided by $n$. We will simply provide an iterative implementation here (see `ActiveCode 1`). Note that this implementation of the GCD algorithm works only when the denominator is positive. This is acceptable for our fraction class because we have said that a negative fraction will be represented by a negative numerator.

    ```python title="The Greatest Common Divisor Function"

        def gcd(m, n):
            while m % n != 0:
                m, n = n, m % n
            return n

        print(gcd(20, 10))
    ```

    Now we can use this function to help reduce any fraction. To put a fraction in lowest terms, we will divide the numerator and the denominator by their greatest common divisor. So, for the fraction $6/8$, the greatest common divisor is 2. Dividing the top and the bottom by 2 creates a new fraction, $3/4$ (see `Listing 6`).

    **Listing 6**

    ```python
    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + \
                        self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
    ```

    Our ``Fraction`` object now has two very useful methods as depicted in `Figure 6`.

    <figure markdown>
    ![Image title](./Figures/fraction2.png)
    <figcaption>Figure 6: An Instance of the ``Fraction`` Class with Two Methods</figcaption>
    </figure>

    ```pycon
    >>> f1 = Fraction(1, 4)
    >>> f2 = Fraction(1, 2)
    >>> print(f1 + f2)
    3/4
    ```

    An additional group of methods that we need to include in our example ``Fraction`` class will allow two fractions to compare themselves to one another. Assume we have two ``Fraction`` objects, ``f1`` and ``f2``. ``f1==f2`` will only be ``True`` if they are references to the same object. Two different objects with the same numerators and denominators would not be equal under this implementation. This is called __shallow equality__ (see `Figure 7`).

    <figure markdown>
    ![Image title](./Figures/fraction3.png)
    <figcaption>Figure 7: Shallow Equality Versus Deep Equality</figcaption>
    </figure>

    We can create __deep equality__–equality by the same value, not the same reference–by overriding the ``__eq__`` method (see `Figure 7`). The ``__eq__`` method is another standard method available in any class. The ``__eq__`` method compares two objects and returns ``True`` if their values are the same, ``False`` otherwise.

    In the ``Fraction`` class, we can implement the ``__eq__`` method by again putting the two fractions in common terms and then comparing the numerators (see `Listing 7`). It is important to note that there are other relational operators that can be overridden. For example, the ``__le__`` method provides the less than or equal functionality.

    **Listing 7**

    ```python
    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num
    ```

    The complete ``Fraction`` class, up to this point, is shown in `ActiveCode 2`. We leave the remaining arithmetic and relational methods as exercises.

    ```python title="The Fraction Class"
    def gcd(m, n):
        while m % n != 0:
            m, n = n, m % n
        return n

    class Fraction:
        def __init__(self, top, bottom):
            self.num = top
            self.den = bottom

        def __str__(self):
            return "{:d}/{:d}".format(self.num, self.den)

        def __eq__(self, other_fraction):
            first_num = self.num * other_fraction.den
            second_num = other_fraction.num * self.den

            return first_num == second_num

        def __add__(self, other_fraction):
            new_num = self.num * other_fraction.den \
            + self.den * other_fraction.num
            new_den = self.den * other_fraction.den
            cmmn = gcd(new_num, new_den)
            return Fraction(new_num // cmmn, new_den // cmmn)

        def show(self):
            print("{:d}/{:d}".format(self.num, self.den))

    x = Fraction(1, 2)
    x.show()
    y = Fraction(2, 3)
    print(y)
    print(x + y)
    print(x == y)
    ```

    !!! info "Self  Check"

    To make sure you understand how operators are implemented in Python classes, and how to properly write methods, write some methods to implement ``*, /,`` and ``-`` .  Also implement comparison operators > and <

    <iframe width="560" height="315" src="https://www.youtube.com/embed/gFb9tvJZHXo" title="fraction" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
