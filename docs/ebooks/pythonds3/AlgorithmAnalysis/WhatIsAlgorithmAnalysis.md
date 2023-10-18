# 什么是算法分析?

=== "中文"

    对于刚开始计算机科学专业的学生来说，相互比较他们的程序是很常见的。 您可能还注意到，计算机程序看起来非常相似是很常见的，尤其是简单的程序。 经常会出现一个有趣的问题。 当两个程序解决相同的问题但看起来不同时，一个程序比另一个更好吗？

    为了回答这个问题，我们需要记住程序和程序所代表的底层算法之间存在重要区别。 正如我们在第一章中所述，算法是用于解决问题的通用的、逐步的指令列表。 它是一种解决问题的任何实例的方法，以便给定特定输入，算法产生所需的结果。 另一方面，程序是一种已编码为某种编程语言的算法。 同一算法可能有许多程序，具体取决于程序员和所使用的编程语言。

    为了进一步探索这种差异，请考虑“ActiveCode 1”中显示的函数。 该函数解决了一个熟悉的问题，计算前 *n* 个整数的总和。 该算法使用初始化为 0 的累加器变量的思想。然后，该解决方案迭代 *n* 个整数，将每个整数添加到累加器中。


    ```python title="前 n 个整数的求和"
    def sum_of_n(n):
        the_sum = 0
        for i in range(1, n + 1):
            the_sum = the_sum + i

        return the_sum

    print(sum_of_n(10))
    ```

    现在看看“ActiveCode 2”中的函数。 乍一看，它可能看起来很奇怪，但经过进一步检查，您会发现该函数本质上与前一个函数执行相同的操作。 这不明显的原因是编码不佳。 我们没有使用好的标识符名称来提高可读性，并且我们使用了在累积步骤中并不是真正必要的额外赋值语句。

    ```python title="前 n 个整数的另一个求和"
    def foo(tom):
        fred = 0
        for bill in range(1, tom + 1):
            barney = bill
            fred = fred + barney

        return fred

    print(foo(10))
    ```

    我们之前提出的问题是一个函数是否比另一个函数更好。 答案取决于您的标准。 如果您关心可读性，函数“sum_of_n”肯定比函数“foo”更好。 事实上，您可能在入门编程课程中看到过许多这样的示例，因为其中的目标之一是帮助您编写易于阅读和理解的程序。 然而，在本课程中，我们也对算法本身的特征感兴趣。 （我们当然希望您继续努力编写可读、可理解的代码。）

    算法分析涉及根据每种算法使用的计算资源量来比较算法。 我们希望能够考虑两种算法，并说其中一种比另一种更好，因为它在使用这些资源方面更有效，或者可能只是因为它使用的资源更少。 从这个角度来看，上面两个函数看起来非常相似。 它们本质上都使用相同的算法来解决求和问题。

    此时，重要的是要更多地思考计算资源的真正含义。 有两种不同的方式来看待这个问题。 一种方法是考虑算法解决问题所需的空间或内存量。 问题解决方案所需的空间量通常由问题实例本身决定。 然而，时常有一些算法有非常具体的空间要求，在这些情况下，我们会非常小心地解释这些变化。

    作为空间要求的替代方案，我们可以根据算法所需的执行时间来分析和比较算法。 此度量有时称为算法的“执行时间(execution time)”或“运行时间(running time)”。 我们测量函数`sum_of_n`执行时间的一种方法是进行**基准分析(benchmark analysis)**。 这意味着我们将跟踪程序计算其结果所需的实际时间。 在Python中，我们可以通过记录我们正在使用的系统内的开始时间和结束时间来对函数进行基准测试。 在`time`模块中，有一个名为`time`的函数，它将返回自某个任意起点以来的当前系统时钟时间（以秒为单位）。 通过在开始和结束时调用该函数两次，然后计算差值，我们可以获得执行的精确秒数（大多数情况下是分数）。


    ```python
    import time

    def sum_of_n_2(n):
        start = time.time()

        the_sum = 0
        for i in range(1, n + 1):
            the_sum = the_sum + i

        end = time.time()

        return the_sum, end - start
    ```

    “清单 1”显示了原始的`sum_of_n`函数，其中在求和之前和之后嵌入了定时调用。 该函数返回一个由结果和计算所需的时间（以秒为单位）组成的元组。 如果我们对该函数执行五次调用，每次调用计算前 10,000 个整数的总和，我们将得到以下结果：

    ```pycon
    >>> for i in range(5):
    ...     print("Sum is %d required %10.7f seconds" % sum_of_n_2(10000))
    ... 
    Sum is 50005000 required  0.0018950 seconds
    Sum is 50005000 required  0.0018620 seconds
    Sum is 50005000 required  0.0019171 seconds
    Sum is 50005000 required  0.0019162 seconds
    Sum is 50005000 required  0.0019360 seconds
    >>>
    ```

    我们发现时间相当一致，执行该代码平均需要大约 0.0019 秒。 如果我们运行添加前 100,000 个整数的函数会怎样？

    ```pycon
    >>> for i in range(5):
    ...     print("Sum is %d required %10.7f seconds" % sum_of_n_2(100000))
    ... 
    Sum is 5000050000 required  0.0199420 seconds
    Sum is 5000050000 required  0.0180972 seconds
    Sum is 5000050000 required  0.0194821 seconds
    Sum is 5000050000 required  0.0178988 seconds
    Sum is 5000050000 required  0.0188949 seconds
    >>>
    ```

    同样，每次运行所需的时间虽然较长，但非常一致，平均大约多出 10 倍秒。 当“n”等于 1,000,000 时，我们得到：

    ```pycon
    >>> for i in range(5):
    ...     print("Sum is %d required %10.7f seconds" % sum_of_n_2(1000000))
    ...
    Sum is 500000500000 required  0.1948988 seconds
    Sum is 500000500000 required  0.1850290 seconds
    Sum is 500000500000 required  0.1809771 seconds
    Sum is 500000500000 required  0.1729250 seconds
    Sum is 500000500000 required  0.1646299 seconds
    >>>
    ```

    在这种情况下，平均值再次约为之前实验的 10 倍。

    现在考虑“ActiveCode 3”，它展示了解决求和问题的不同方法。 此函数“sum_of_n_3”利用闭方程 $\sum_{i=1}^{n} i = \frac {(n)(n+1)}{2}$ 来计算总和前“n”个整数，无需迭代。

    ```python title="不迭代求和"

    def sum_of_n_3(n):
        return (n * (n + 1)) / 2


    print(sum_of_n_3(10))
    ```

    如果我们对“sum_of_n_3”进行相同的基准测量，使用五个不同的“n”值（10,000、100,000、1,000,000、10,000,000 和 100,000,000），我们会得到以下结果：

    ```python
    Sum is 50005000 required 0.00000095 seconds
    Sum is 5000050000 required 0.00000191 seconds
    Sum is 500000500000 required 0.00000095 seconds
    Sum is 50000005000000 required 0.00000095 seconds
    Sum is 5000000050000000 required 0.00000119 seconds
    ```

    关于此输出，有两件重要的事情需要注意。 首先，上面记录的时间比前面的任何例子都短。 其次，无论“n”的值是多少，它们都非常一致。 看来“sum_of_n_3”几乎不受添加的整数数量的影响。

    但这个基准测试真正告诉我们什么？ 直观上，我们可以看到迭代解决方案似乎做了更多的工作，因为某些程序步骤正在重复。 这可能是需要更长时间的原因。 此外，随着我们增加“n”的值，迭代解决方案所需的时间似乎也会增加。 但是，如果我们在不同的计算机上运行相同的函数或使用不同的编程语言，我们可能会得到不同的结果。 如果计算机较旧，则执行“sum_of_n_3”可能需要更长的时间。

    我们需要一种更好的方法来描述这些算法在执行时间方面的特征。 基准测试技术计算实际执行时间。 它并没有真正为我们提供有用的测量，因为它依赖于特定的机器、程序、一天中的时间、编译器和编程语言。 相反，我们希望拥有独立于所使用的程序或计算机的特征。 这种测量对于单独判断算法很有用，并且可以用于比较跨实现的算法。

=== "英文"

    **What Is Algorithm Analysis?**

    It is very common for beginning computer science students to compare their programs with one another. You may also have noticed that it is common for computer programs to look very similar, especially the simple ones. An interesting question often arises. When two programs solve the same problem but look different, is one program better than the other?

    In order to answer this question, we need to remember that there is an important difference between a program and the underlying algorithm that the program is representing. As we stated in Chapter 1, an algorithm is a generic, step-by-step list of instructions for solving a problem. It is a method for solving any instance of the problem so that given a particular input, the algorithm produces the desired result. A program, on the other hand, is an algorithm that has been encoded into some programming language. There may be many programs for the same algorithm, depending on the programmer and the programming language being used.

    To explore this difference further, consider the function shown in `ActiveCode 1`. This function solves a familiar problem, computing the sum of the first *n* integers. The algorithm uses the idea of an accumulator variable that is initialized to 0. The solution then iterates through the *n* integers, adding each to the accumulator.


    ```python title="Summation of the First n Integers"
    def sum_of_n(n):
        the_sum = 0
        for i in range(1, n + 1):
            the_sum = the_sum + i

        return the_sum

    print(sum_of_n(10))
    ```

    Now look at the function in `ActiveCode 2`. At first glance it may look strange, but upon further inspection you can see that this function is essentially doing the same thing as the previous one. The reason this is not obvious is poor coding. We did not use good identifier names to assist with readability, and we used an extra assignment statement that was not really necessary during the accumulation step.

    ```python title="Another Summation of the First n Integers"
    def foo(tom):
        fred = 0
        for bill in range(1, tom + 1):
            barney = bill
            fred = fred + barney

        return fred

    print(foo(10))
    ```

    The question we raised earlier asked whether one function is better than another. The answer depends on your criteria. The function ``sum_of_n`` is certainly better than the function ``foo`` if you are concerned with readability. In fact, you have probably seen many examples of this in your introductory programming course since one of the goals there is to help you write programs that are easy to read and easy to understand. In this course, however, we are also interested in characterizing the algorithm itself. (We certainly hope that you will continue to strive to write readable, understandable code.)

    Algorithm analysis is concerned with comparing algorithms based upon the amount of computing resources that each algorithm uses. We want to be able to consider two algorithms and say that one is better than the other because it is more efficient in its use of those resources or perhaps because it simply uses fewer. From this perspective, the two functions above seem very similar. They both use essentially the same algorithm to solve the summation problem.

    At this point, it is important to think more about what we really mean by computing resources. There are two different ways to look at this. One way is to consider the amount of space or memory an algorithm requires to solve the problem. The amount of space required by a problem solution is typically dictated by the problem instance itself. Every so often, however, there are algorithms that have very specific space requirements, and in those cases we will be very careful to explain the variations.

    As an alternative to space requirements, we can analyze and compare algorithms based on the amount of time they require to execute. This measure is sometimes referred to as the *execution time* or *running time* of the algorithm. One way we can measure the execution time for the function ``sum_of_n`` is to do a **benchmark analysis**. This means that we will track the actual time required for the program to compute its result. In Python, we can benchmark a function by noting the starting time and ending time within the system we are using. In the ``time`` module there is a function called ``time`` that will return the current system clock time in seconds since some arbitrary starting point. By calling this function twice, at the beginning and at the end, and then computing the difference, we can get an exact number of seconds (fractions in most cases) for execution.


    ```python
    import time

    def sum_of_n_2(n):
        start = time.time()

        the_sum = 0
        for i in range(1, n + 1):
            the_sum = the_sum + i

        end = time.time()

        return the_sum, end - start
    ```

    `Listing 1` shows the original ``sum_of_n`` function with the timing calls embedded before and after the summation. The function returns a tuple consisting of the result and the amount of time (in seconds) required for the calculation. If we perform five invocations of the function, each computing the sum of the first 10,000 integers, we get the following:

    ```pycon
    >>> for i in range(5):
    ...     print("Sum is %d required %10.7f seconds" % sum_of_n_2(10000))
    ... 
    Sum is 50005000 required  0.0018950 seconds
    Sum is 50005000 required  0.0018620 seconds
    Sum is 50005000 required  0.0019171 seconds
    Sum is 50005000 required  0.0019162 seconds
    Sum is 50005000 required  0.0019360 seconds
    >>>
    ```

    We discover that the time is fairly consistent and it takes on average about 0.0019 seconds to execute that code. What if we run the function adding the first 100,000 integers?

    ```pycon
    >>> for i in range(5):
    ...     print("Sum is %d required %10.7f seconds" % sum_of_n_2(100000))
    ... 
    Sum is 5000050000 required  0.0199420 seconds
    Sum is 5000050000 required  0.0180972 seconds
    Sum is 5000050000 required  0.0194821 seconds
    Sum is 5000050000 required  0.0178988 seconds
    Sum is 5000050000 required  0.0188949 seconds
    >>>
    ```

    Again, the time required for each run, although longer, is very consistent, averaging about 10 times more seconds. For ``n`` equal to 1,000,000 we get:

    ```pycon
    >>> for i in range(5):
    ...     print("Sum is %d required %10.7f seconds" % sum_of_n_2(1000000))
    ...
    Sum is 500000500000 required  0.1948988 seconds
    Sum is 500000500000 required  0.1850290 seconds
    Sum is 500000500000 required  0.1809771 seconds
    Sum is 500000500000 required  0.1729250 seconds
    Sum is 500000500000 required  0.1646299 seconds
    >>>
    ```

    In this case, the average again turns out to be about 10 times the previous experiment.

    Now consider `ActiveCode 3`, which shows a different means of solving the summation problem. This function, ``sum_of_n_3``, takes advantage of a closed equation $`\sum_{i=1}^{n} i = \frac {(n)(n+1)}{2}$ to compute the sum of the first ``n`` integers without iterating.

    ```python title="Summation Without Iteration"

    def sum_of_n_3(n):
        return (n * (n + 1)) / 2


    print(sum_of_n_3(10))
    ```

    If we do the same benchmark measurement for ``sum_of_n_3``, using five different values for ``n`` (10,000, 100,000, 1,000,000, 10,000,000, and 100,000,000), we get the following results:

    ```python
    Sum is 50005000 required 0.00000095 seconds
    Sum is 5000050000 required 0.00000191 seconds
    Sum is 500000500000 required 0.00000095 seconds
    Sum is 50000005000000 required 0.00000095 seconds
    Sum is 5000000050000000 required 0.00000119 seconds
    ```

    There are two important things to notice about this output. First, the times recorded above are shorter than any of the previous examples. Second, they are very consistent no matter what the value of ``n``. It appears that ``sum_of_n_3`` is hardly impacted by the number of integers being added.

    But what does this benchmark really tell us? Intuitively, we can see that the iterative solutions seem to be doing more work since some program steps are being repeated. This is likely the reason it is taking longer. Also, the time required for the iterative solution seems to increase as we increase the value of ``n``. However, if we ran the same function on a different computer or used a different programming language, we would likely get different results. It could take even longer to perform ``sum_of_n_3`` if the computer were older.

    We need a better way to characterize these algorithms with respect to execution time. The benchmark technique computes the actual time to execute. It does not really provide us with a useful measurement because it is dependent on a particular machine, program, time of day, compiler, and programming language. Instead, we would like to have a characterization that is independent of the program or computer being used. This measure would then be useful for judging the algorithm alone and could be used to compare algorithms across implementations.
