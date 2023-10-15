# 1.6. 为什么要研究算法?

计算机科学家通过经验学习。 我们通过看到别人解决问题和自己解决问题来学习。 接触不同的问题解决技术并了解不同算法的设计方式有助于我们应对下一个具有挑战性的问题。 通过考虑多种不同的算法，我们可以开始开发模式识别，以便下次出现类似问题时，我们能够更好地解决它。

算法之间往往存在很大差异。 考虑前面看到的 `sqrt` 示例（见图 1.1）。 完全有可能有许多不同的方法来实现计算平方根函数的细节。 一种算法使用的资源可能比另一种算法少得多。 一种算法返回结果的时间可能是另一种算法的 10 倍。 我们希望有某种方法来比较这两种解决方案。 尽管它们都有效，但其中一种可能比另一种“更好”。我们可能会建议其中一种效率更高，或者只是工作速度更快或使用更少的内存。当我们研究算法时，我们可以学习分析技术，这些技术使我们能够仅根据解决方案自身的特征，而不是用于实现它们的程序或计算机的特征来比较和对比解决方案。

在最坏的情况下，我们可能会遇到一个棘手的问题，这意味着没有算法可以在现实的时间内解决问题。 重要的是能够区分哪些有解决方案的问题、哪些没有解决方案的问题以及哪些存在解决方案但需要太多时间或其他资源才能合理工作的问题。

我们经常需要确定并做出权衡。 作为计算机科学家，除了解决问题的能力之外，我们还需要了解和理解**解决方案评估技术**。 最后，解决一个问题往往有很多种方法。 找到一个解决方案，然后决定它是否是一个好的解决方案，是我们会一遍又一遍地做的任务。

???- info "原文"

    **Why Study Algorithms?**

    Computer scientists learn by experience. We learn by seeing others solve problems and by solving problems by ourselves. Being exposed to different problem-solving techniques and seeing how different algorithms are designed helps us to take on the next challenging problem that we are given. By considering a number of different algorithms, we can begin to develop pattern recognition so that the next time a similar problem arises, we are better able to solve it.

    Algorithms are often quite different from one another. Consider the example of ``sqrt`` seen earlier (see Figure 1.1). It is entirely possible that there are many different ways to implement the details to compute the square root function. One algorithm may use many fewer resources than another. One algorithm might take 10 times as long to return the result as the other. We would like to have some way to compare these two solutions. Even though they both work, one is perhaps “better" than the other. We might suggest that one is more efficient or that one simply works faster or uses less memory. As we study algorithms, we can learn analysis techniques that allow us to compare and contrast solutions based solely on their own characteristics, not the characteristics of the program or computer used to implement them.

    In the worst-case scenario, we may have a problem that is intractable, meaning that there is no algorithm that can solve the problem in a realistic amount of time. It is important to be able to distinguish between those problems that have solutions, those that do not, and those where solutions exist but require too much time or other resources to work reasonably.

    There will often be trade-offs that we will need to identify and decide upon. As computer scientists, in addition to our ability to solve problems, we will also need to know and understand solution evaluation techniques. In the end, there are often many ways to solve a problem. Finding a solution and then deciding whether it is a good one are tasks that we will do over and over again.
