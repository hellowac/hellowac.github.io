# 为什么要研究数据结构和抽象数据类型?

为了管理问题的复杂性和解决问题的过程，计算机科学家使用抽象来让他们专注于“大局（big picture）”，而不会迷失在细节中。 通过创建问题域的模型，我们能够利用更好、更高效的问题解决过程。 这些模型使我们能够描述我们的算法将以与问题本身更加一致的方式操作的数据。

早些时候，我们将过程抽象称为隐藏特定函数的细节以允许用户或客户端在非常高的级别上查看它的过程。 现在我们将注意力转向一个类似的想法，即**数据抽象**。 **抽象数据类型**，有时缩写为**ADT**，是我们如何查看数据和允许的操作的逻辑描述，而不考虑它们将如何实现。 这意味着我们只关心数据代表什么，而不关心它最终将如何构建。 通过提供这种抽象级别，我们正在围绕数据创建**封装**。 我们的想法是，通过封装实现的细节，我们将它们隐藏在用户的视野之外。 这称为**信息隐藏**。

“图 2”显示了抽象数据类型是什么及其操作方式的图片。 用户使用抽象数据类型指定的操作与界面交互。 抽象数据类型是用户交互的外壳。 该实现隐藏得更深一层。 用户不关心实现的细节。

<figure markdown>
![Image title](./Figures/adt.png)
<figcaption>图 2：抽象数据类型</figcaption>
</figure>

抽象数据类型（通常称为**数据结构**）的实现将要求我们使用一些编程结构和原始数据类型的集合来提供数据的物理视图。 正如我们之前讨论的，这两个视角的分离将使我们能够为我们的问题定义复杂的数据模型，而无需给出任何有关如何实际构建模型的细节的指示。 这提供了数据的**独立于实现的**视图。 由于通常有许多不同的方法来实现抽象数据类型，因此这种实现独立性允许程序员切换实现的细节，而无需更改数据用户与其交互的方式。 用户可以继续专注于解决问题的过程。

???- info "原文"

    **Why Study Data Structures and Abstract Data Types?**

    To manage the complexity of problems and the problem-solving process, computer scientists use abstractions to allow them to focus on the “big picture” without getting lost in the details. By creating models of the problem domain, we are able to utilize a better and more efficient problem-solving process. These models allow us to describe the data that our algorithms will manipulate in a much more consistent way with respect to the problem itself.

    Earlier, we referred to procedural abstraction as a process that hides the details of a particular function to allow the user or client to view it at a very high level. We now turn our attention to a similar idea, that of **data abstraction**. An **abstract data type**, sometimes abbreviated **ADT**, is a logical description of how we view the data and the operations that are allowed without regard to how they will be implemented. This means that we are concerned only with what the data is representing and not with how it will eventually be constructed. By providing this level of abstraction, we are creating an **encapsulation** around the data. The idea is that by encapsulating the details of the implementation, we are hiding them from the user’s view. This is called **information hiding**.

    `Figure 2` shows a picture of what an abstract data type is and how it operates. The user interacts with the interface, using the operations that have been specified by the abstract data type. The abstract data type is the shell that the user interacts with. The implementation is hidden one level deeper. The user is not concerned with the details of the implementation.

    <figure markdown>
    ![Image title](./Figures/adt.png)
    <figcaption>Figure 2: Abstract Data Type</figcaption>
    </figure>

    The implementation of an abstract data type, often referred to as a **data structure**, will require that we provide a physical view of the data using some collection of programming constructs and primitive data types. As we discussed earlier, the separation of these two perspectives will allow us to define the complex data models for our problems without giving any indication as to the details of how the model will actually be built. This provides an **implementation-independent** view of the data. Since there will usually be many different ways to implement an abstract data type, this implementation independence allows the programmer to switch the details of the implementation without changing the way the user of the data interacts with it. The user can remain focused on the problem-solving process.
