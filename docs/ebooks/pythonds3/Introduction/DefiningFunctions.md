# 定义函数

前面的过程抽象示例调用数学模块中名为`sqrt`的 Python 函数来计算平方根。 一般来说，我们可以通过定义函数来隐藏任何计算的细节。 函数定义需要一个名称、一组参数和一个函数体。 它还可以显式返回一个值。 例如，下面定义的简单函数返回传递给它的值的平方。

```pycon
>>> def square(n):
...    return n ** 2
...
>>> square(3)
9
>>> square(square(3))
81
```

该函数定义的语法包括名称`square`和带括号的形式参数列表。 对于这个函数，`n`是唯一的形式参数，这表明`square`只需要一个数据来完成它的工作。 隐藏在“盒子内(inside the box)”的细节只是简单地计算`n**2`的结果并返回它。 我们可以通过要求 Python 环境评估它并传递实际参数值（在本例中为`3`）来调用`square`函数。 请注意，对`square`的调用返回一个整数，该整数可以传递给另一个调用。

我们可以通过使用一种名为牛顿法或牛顿-拉夫森法（以艾萨克·牛顿和约瑟夫·拉夫森命名）的众所周知的技术来实现我们自己的平方根函数。 用于近似平方根的牛顿-拉夫森方法执行迭代计算，收敛于正确值。 方程 $newguess = \frac {1}{2} * (oldguess + \frac {n}{oldguess})$ 取值 $n$ 并通过将每个 $newguess$ 设为 $oldguess$ 来重复猜测平方根 随后的迭代。 这里使用的初始猜测是$\frac {n}{2}$。 “Listing 1”显示了一个函数定义，它接受值 $n$ 并在进行 20 次猜测后返回 $n$ 的平方根。 同样，牛顿-拉夫森方法的细节隐藏在函数定义中，用户无需了解有关实现的任何信息即可使用该函数达到其预期目的。 “Listing 1”还显示了使用`#`字符作为注释标记。 一行中`#`后面的任何字符都将被忽略。

**Listing 1**

```python
def square_root(n):
    root = n / 2  # initial guess will be 1/2 of n
    for k in range(20):
        root = (1 / 2) * (root + (n / root))

    return root
```

```pycon
>>> square_root(9)
3.0
>>> square_root(4563)
67.54998149518622
```

!!! info "自检"

    这是一个自我检查，真正涵盖了迄今为止的所有内容。 你可能听说过无限猴子定理？ 该定理指出，一只猴子在打字机键盘上随机敲击按键无限长的时间，几乎肯定会键入给定的文本，例如威廉·莎士比亚的全集。 好吧，假设我们用 Python 函数替换猴子。 你认为一个 Python 函数生成莎士比亚的一句话需要多长时间？ 我们要命中的句子是：“我认为它就像一只黄鼠狼(methinks it is like a weasel)”

    您不会想在浏览器中运行这个，所以启动您最喜欢的 Python IDE。 我们模拟这个的方法是编写一个函数，通过从字母表中的 26 个字母加上空格中选择随机字母来生成 28 个字符长的字符串。 我们将编写另一个函数，通过将随机生成的字符串与目标进行比较来对每个生成的字符串进行评分。

    第三个函数将重复调用生成和评分，然后如果 100% 的字母正确，我们就完成了。 如果字母不正确，那么我们将生成一个全新的字符串。为了更容易地跟踪程序的进度，第三个函数应该打印出迄今为止生成的最佳字符串及其每 1000 次尝试的分数。

!!! info "自检挑战"

    看看是否可以通过保留正确的字母并仅修改迄今为止最佳字符串中的一个字符来改进自检中的程序。 这是“爬山(hill climbing)”算法中的一种算法，即我们仅保留比前一个更好的结果。

<iframe width="560" height="315" src="https://www.youtube.com/embed/yZS_vb549cc" title="monkeys" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

???- info "原文"

    **Defining Functions**

    The earlier example of procedural abstraction called upon a Python function called ``sqrt`` from the math module to compute the square root. In general, we can hide the details of any computation by defining a function. A function definition requires a name, a group of parameters, and a body. It may also explicitly return a value. For example, the simple function defined below returns the square of the value you pass into it.

    ```pycon
    >>> def square(n):
    ...    return n ** 2
    ...
    >>> square(3)
    9
    >>> square(square(3))
    81
    ```

    The syntax for this function definition includes the name, ``square``, and a parenthesized list of formal parameters. For this function, ``n`` is the only formal parameter, which suggests that ``square`` needs only one piece of data to do its work. The details, hidden “inside the box,” simply compute the result of ``n**2`` and return it. We can invoke or call the ``square`` function by asking the Python environment to evaluate it, passing an actual parameter value, in this case, ``3``. Note that the call to ``square`` returns an integer that can in turn be passed to another invocation.

    We could implement our own square root function by using a well-known technique called Newton's method or the Newton–Raphson method, named after Isaac Newton and Joseph Raphson. The Newton–Raphson method for approximating square roots performs an iterative computation that converges on the correct value. The equation $newguess = \frac {1}{2} * (oldguess + \frac {n}{oldguess})$ takes a value $n$ and repeatedly guesses the square root by making each $newguess$ the $oldguess$ in the subsequent iteration. The initial guess used here is $\frac {n}{2}$. `Listing 1` shows a function definition that accepts a value $n$ and returns the square root of $n$ after making 20 guesses. Again, the details of the Newton–Raphson method are hidden inside the function definition and the user does not have to know anything about the implementation to use the function for its intended purpose. `Listing 1` also shows the use of the ``#`` character as a comment marker. Any characters that follow the ``#`` on a line are ignored.

    **Listing 1**

    ```python
    def square_root(n):
        root = n / 2  # initial guess will be 1/2 of n
        for k in range(20):
            root = (1 / 2) * (root + (n / root))

        return root
    ```

    ```pycon
    >>> square_root(9)
    3.0
    >>> square_root(4563)
    67.54998149518622
    ```

    !!! info "Self Check"

        Here's a self check that really covers everything so far.  You may have heard of the infinite monkey theorem?  The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare.  Well, suppose we replace a monkey with a Python function.  How long do you think it would take for a Python function to generate just one sentence of Shakespeare?  The sentence we'll shoot for is:  "methinks it is like a weasel"

        You're not going to want to run this one in the browser, so fire up your favorite Python IDE.  The way we'll simulate this is to write a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet plus the space.  We'll write another function that will score each generated string by comparing the randomly generated string to the goal.

        A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done.  If the letters are not correct then we will generate a whole new string.To make it easier to follow your program's progress this third function should print out the best string generated so far and its score every 1000 tries.

    !!! info "Self Check Challenge"

        See if you can improve upon the program in the self check by keeping letters that are correct and only modifying one character in the best string so far.  This is a type of algorithm in the class of 'hill climbing' algorithms, that is we only keep the result if it is better than the previous one.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/yZS_vb549cc" title="monkeys" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
