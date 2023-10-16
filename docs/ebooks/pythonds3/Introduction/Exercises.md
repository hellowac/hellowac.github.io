# 练习

   1. 为大学校园里的人们构建一个阶级层次结构。 包括教师、职员和学生。 他们有什么共同点？ 它们有何不同？
   2. 构建银行帐户的类层次结构。
   3. 为不同类型的计算机构建类层次结构。
   4. 使用本章中提供的类，交互式地构建电路并对其进行测试。
   5. 实现简单的方法“get_num”和“get_den”，它们将返回分数的分子和分母。
   6. 从很多方面来说，如果所有分数从一开始就保持最低的水平会更好。 修改“Fraction”类的构造函数，以便使用“GCD”立即减少分数。 请注意，这意味着 `__add__` 函数不再需要归约。 进行必要的修改。
   7. 实现剩余的简单算术运算符（``__sub__``、``__mul__`` 和``__truediv__``）。
   8. 实现剩余的关系运算符（``__gt__``、``__ge__``、``__lt__``、``__le__`` 和 ``__ne__``）。
   9. 修改分数类的构造函数，以便它检查以确保分子和分母都是整数。 如果其中一个不是整数，构造函数应该引发异常。
   10. 在分数的定义中，我们假设负分数具有负分子和正分母。 使用负分母会导致某些关系运算符给出不正确的结果。 一般来说，这是一个不必要的限制。 修改构造函数以允许用户传递负分母，以便所有运算符继续正常工作。
   11. 研究`__radd__`方法。 它与 `__add__` 有何不同？ 什么时候使用？ 实现`__radd__`。
   12. 重复上一个问题，但这次考虑`__iadd__`方法。
   13. 研究``__repr__``方法。 它与 `__str__` 有何不同？ 什么时候使用？ 实现``__repr__``。
   14. 研究现有的其他类型的门（例如 NAND、NOR 和 XOR）。 将它们添加到电路层次结构中。 您需要做多少额外的编码？
   15. 最简单的算术电路称为半加器。 研究简单的半加器电路。 实现该电路。
   16. 现在扩展该电路并实现一个 8 位全加器。
   17. 本章所示的电路仿真是反向工作的。 换句话说，给定一个电路，输出是通过输入值进行反向处理而产生的，这反过来又导致其他输出被查询。 这一直持续到找到外部输入线为止，此时系统会要求用户输入值。 修改实现，使动作朝着正向方向进行； 接收输入后，电路产生输出。
   18. 设计一个类来代表一张扑克牌，另一个类来代表一副纸牌。 使用这两个类，实现您最喜欢的纸牌游戏。
   19. 在线或在当地报纸上查找数独谜题。 编写一个程序来解决这个难题。

???- info "原文"

   **Exercises**

   1. Construct a class hierarchy for people on a college campus. Include faculty, staff, and students. What do they have in common? What distinguishes them from one another?
   2. Construct a class hierarchy for bank accounts.
   3. Construct a class hierarchy for different types of computers.
   4. Using the classes provided in the chapter, interactively construct a circuit and test it.
   5. Implement the simple methods ``get_num`` and ``get_den`` that will return the numerator and denominator of a fraction.
   6. In many ways it would be better if all fractions were maintained in lowest terms right from the start. Modify the constructor for the ``Fraction`` class so that ``GCD`` is used to reduce fractions immediately. Notice that this means the ``__add__`` function no longer needs to reduce. Make the necessary modifications.
   7. Implement the remaining simple arithmetic operators (``__sub__``, ``__mul__``, and ``__truediv__``).
   8. Implement the remaining relational operators (``__gt__``, ``__ge__``, ``__lt__``, ``__le__``, and ``__ne__``).
   9. Modify the constructor for the fraction class so that it checks to make sure that the numerator and denominator are both integers. If either is not an integer, the constructor should raise an exception.
   10. In the definition of fractions we assumed that negative fractions have a negative numerator and a positive denominator. Using a negative denominator would cause some of the relational operators to give incorrect results. In general, this is an unnecessary constraint. Modify the constructor to allow the user to pass a negative denominator so that all of the operators continue to work properly.
   11. Research the ``__radd__`` method. How does it differ from ``__add__``? When is it used? Implement ``__radd__``.
   12. Repeat the last question but this time consider the ``__iadd__`` method.
   13. Research the ``__repr__`` method. How does it differ from ``__str__``? When is it used? Implement ``__repr__``.
   14. Research other types of gates that exist (such as NAND, NOR, and XOR). Add them to the circuit hierarchy. How much additional coding did you need to do?
   15. The most simple arithmetic circuit is known as the half adder. Research the simple half-adder circuit. Implement this circuit.
   16. Now extend that circuit and implement an 8-bit full adder.
   17. The circuit simulation shown in this chapter works in a backward direction. In other words, given a circuit, the output is produced by working back through the input values, which in turn cause other outputs to be queried. This continues until external input lines are found, at which point the user is asked for values. Modify the implementation so that the action is in the forward direction; upon receiving inputs the circuit produces an output.
   18. Design a class to represent a playing card and another one to represent a deck of cards. Using these two classes, implement your favorite card game.
   19. Find a Sudoku puzzle online or in the local newspaper. Write a program to solve the puzzle.
