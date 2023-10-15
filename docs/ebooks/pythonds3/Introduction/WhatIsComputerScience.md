# 什么是计算机科学?

计算机科学很难定义。 这可能是由于名称中不幸使用了“计算机”一词。 正如您可能知道的那样，计算机科学不仅仅是对计算机的研究。 尽管计算机作为工具在该学科中发挥着重要的支持作用，但它们只是 -- 工具。

计算机科学是对问题、问题解决以及问题解决过程中产生的解决方案的研究。 给定一个问题，计算机科学家的目标是开发一种**算法**，这是解决可能出现的任何问题实例的逐步说明列表。 算法是有限的过程，如果遵循它就能解决问题。 算法就是解决方案。

计算机科学可以被认为是算法的研究。 然而，我们必须小心地承认，有些问题可能没有解决方案。 虽然证明这一说法超出了本文的范围，但有些问题无法解决这一事实对于研究计算机科学的人来说很重要。 那么，我们可以通过包括这两种类型的问题来完整地定义计算机科学，并指出计算机科学是对问题解决方案的研究以及对无解决方案的问题的研究。

在描述问题和解决方案时，包含 **可计算** 一词也很常见。 如果存在解决问题的算法，我们就说问题是可计算的。 那么，计算机科学的另一种定义是，计算机科学是对可计算和不可计算问题的研究，是对算法存在和不存在的研究。 无论如何，您会注意到 **计算机** 这个词根本没有出现。 解决方案被认为独立于机器。

计算机科学，因为它涉及问题解决过程本身，所以也是**抽象**的研究。 抽象使我们能够以分离所谓的逻辑和物理视角的方式来看待问题和解决方案。 我们在一个常见的例子中熟悉其基本思想。

考虑一下您今天可能开着的车去学校或上班。 作为驾驶员、车辆的用户，您需要进行某些交互才能将汽车用于其预期用途。 您上车，插入钥匙，启动发动机，换档，制动，加速和转向以进行驾驶。 从抽象的角度来看，我们可以说你看到的是汽车的逻辑视角。 您正在使用车辆设计者提供的功能来将您从一个地点运送到另一个地点。 这些函数有时也称为**接口**。

另一方面，必须修理你的汽车的机械师则持截然不同的观点。 他们不仅知道如何驾驶，还必须了解执行我们认为理所当然的所有功能所需的所有细节。 他们需要了解发动机如何工作、变速器如何换档、如何控制温度等等。 这被称为物理视角，即 “幕后” 发生的细节。

当我们使用电脑时也会发生同样的事情。 大多数人使用计算机编写文档、发送和接收电子邮件、上网、播放音乐、存储图像和玩游戏，但不了解这些类型的应用程序运行的详细信息。 他们从逻辑或用户的角度看待计算机。 计算机科学家、程序员、技术支持人员和系统管理员对计算机的看法截然不同。 他们必须了解操作系统如何工作、网络协议如何配置以及如何编写控制计算机功能的各种脚本的详细信息。 他们必须能够控制用户简单假设的低级细节。

这两个示例的共同点是，抽象的用户（有时也称为客户端）不需要了解细节，只要用户知道界面的工作方式即可。 这个接口是我们作为用户与实现的底层复杂性进行通信的方式。

作为抽象的另一个例子，考虑一下 Python 的 `math` 模块。 一旦我们导入模块，我们就可以执行计算，例如

```pycon
>>> import math
>>> math.sqrt(16)
4.0
```

这是 **程序抽象** 的一个例子。 我们不一定知道平方根是如何计算的，但我们知道该函数的名称以及如何使用它。 如果我们正确执行导入，我们可以假设该函数将为我们提供正确的结果。 我们知道有人实现了平方根问题的解决方案，但我们只需要知道如何使用它。 这有时被称为流程的 *黑匣子* 视图。 我们简单地描述接口：函数的名称、需要什么（参数）以及将返回什么。 细节隐藏在里面（参见“图1”）。

<figure markdown>
![Image title](./Figures/blackbox.png)
<figcaption>图1: 程序抽象</figcaption>
</figure>

???- info "原文"

    **What Is Computer Science?**

    Computer science is difficult to define. This is probably due to
    the unfortunate use of the word *computer* in the name. As you are
    perhaps aware, computer science is not simply the study of computers.
    Although computers play an important supporting role as a tool in the
    discipline, they are just that–--tools.

    Computer science is the study of problems, problem-solving, and the
    solutions that come out of the problem-solving process. Given a problem,
    a computer scientist’s goal is to develop an **algorithm**, a
    step-by-step list of instructions for solving any instance of the
    problem that might arise. Algorithms are finite processes that if
    followed will solve the problem. Algorithms are solutions.

    Computer science can be thought of as the study of algorithms. However,
    we must be careful to include the fact that some problems may not have a
    solution. Although proving this statement is beyond the scope of this
    text, the fact that some problems cannot be solved is important for
    those who study computer science. We can fully define computer science,
    then, by including both types of problems and stating that computer
    science is the study of solutions to problems as well as the study of
    problems with no solutions.

    It is also very common to include the word **computable** when
    describing problems and solutions. We say that a problem is computable
    if an algorithm exists for solving it. An alternative definition for
    computer science, then, is to say that computer science is the study of
    problems that are and that are not computable, the study of the
    existence and the nonexistence of algorithms. In any case, you will note
    that the word *computer* did not come up at all. Solutions are
    considered independent from the machine.

    Computer science, as it pertains to the problem-solving process itself,
    is also the study of **abstraction**. Abstraction allows us to view the
    problem and solution in such a way as to separate the so-called logical
    and physical perspectives. The basic idea is familiar to us in a common
    example.

    Consider the car that you may have driven to school or work
    today. As a driver, a user of the vehicle, you have certain interactions
    that take place in order to use the car for its intended purpose.
    You get in, insert the key, start the engine, shift, brake, accelerate, and
    steer in order to drive. From an abstraction point of view, we can say
    that you are seeing the logical perspective of the car. You are
    using the functions provided by the vehicle designers for the purpose of
    transporting you from one location to another. These functions are
    sometimes also referred to as the **interface**.

    On the other hand, the mechanic who must repair your car takes a
    very different point of view. They not only know how to drive but must
    know all of the details necessary to carry out all the functions that we
    take for granted. They need to understand how the engine works, how the
    transmission shifts gears, how temperature is controlled, and so on.
    This is known as the physical perspective, the details that take place
    “under the hood.”

    The same thing happens when we use computers. Most people use computers
    to write documents, send and receive email, surf the web, play music,
    store images, and play games without any knowledge of the details that
    take place to allow those types of applications to work. They view
    computers from a logical or user perspective. Computer scientists,
    programmers, technology support staff, and system administrators take a
    very different view of the computer. They must know the details of how
    operating systems work, how network protocols are configured, and how to
    code various scripts that control computer functionality. They must be able to control
    the low-level details that a user simply assumes.

    The common point for both of these examples is that the user of the
    abstraction, sometimes also called the client, does not need to know the
    details as long as the user is aware of the way the interface works.
    This interface is the way we as users communicate with the underlying
    complexities of the implementation.

    As another example of abstraction,
    consider the Python ``math`` module. Once we import the module, we can
    perform computations such as

    ```pycon
    >>> import math
    >>> math.sqrt(16)
    4.0
    ```

    This is an example of **procedural abstraction**. We do not necessarily
    know how the square root is being calculated, but we know what the
    function is called and how to use it. If we perform the import
    correctly, we can assume that the function will provide us with the
    correct results. We know that someone implemented a solution to the
    square root problem, but we only need to know how to use it. This is
    sometimes referred to as a *black box* view of a process. We simply
    describe the interface: the name of the function, what is needed (the
    parameters), and what will be returned. The details are hidden inside
    (see `Figure 1`).

    <figure markdown>
    ![Image title](./Figures/blackbox.png)
    <figcaption>Figure 1: Procedural Abstraction</figcaption>
    </figure>
