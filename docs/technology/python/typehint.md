# 类型标注

参考原文: <https://docs.python.org/zh-cn/3.10/library/typing.html#special-typing-primitives>{target="_blank"}

3.5 新版功能.

源码： [Lib/typing.py](https://github.com/python/cpython/tree/3.10/Lib/typing.py){target="_blank"}

> **注解**: Python 运行时不强制执行函数和变量类型注解，但这些注解可用于类型检查器、IDE、静态检查器等第三方工具。

这个模块提供对类型提示的运行时支持。最基本的支持包括 [Any] , [Union] , [Callable] , [TypeVar] , 和 [Generic] 。关于完整的规范，请参考 [PEP 484] 。关于类型提示的简化介绍，请参考 [PEP 483] 。

下面的函数接收与返回的都是字符串，注解方式如下：

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```

`greeting` 函数中，参数 `name` 的类型是 [str]，返回类型也是 [str]。子类型也可以当作参数。

新的功能频繁地被添加到 [typing] 模块中。[typing_extensions](https://pypi.org/project/typing-extensions/) 包提供了这些新功能对旧版本 Python 的向后移植。

## 相关的 PEP

参考: <https://docs.python.org/zh-cn/3.10/library/typing.html#relevant-peps>{target="_blank"}

## 类型别名

把类型赋给别名，就可以定义类型别名。本例中，`Vector` 和 `list[float]` 相同，可互换：

```python
Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.
# 通过类型检查； 浮点数列表可以作为Vector。
new_vector = scale(2.0, [1.0, -4.2, 5.4])
```

类型别名适用于简化复杂的类型签名。例如：

```python
from collections.abc import Sequence

ConnectionOptions = dict[str, str]
Address = tuple[str, int]
Server = tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    ...

# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.
# 静态类型检查器会将前一个类型签名视为与当前类型签名完全等同。
def broadcast_message(
        message: str,
        servers: Sequence[tuple[tuple[str, int], dict[str, str]]]) -> None:
    ...
```

注意，`None` 是一种类型提示特例，已被 `type(None)` 取代。

## NewType

使用 [NewType] 助手来创建不同的类型

```python
from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)
```

静态类型检查器把新类型当作原始类型的子类，这种方式适用于捕捉逻辑错误：

```python
def get_user_name(user_id: UserId) -> str:
    ...

# passes type checking
user_a = get_user_name(UserId(42351))

# fails type checking; an int is not a UserId
user_b = get_user_name(-1)
```

`UserId` 类型的变量可执行所有 `int` 操作，但返回结果都是 `int` 类型。这种方式允许在预期 `int` 时传入 `UserId`，还能防止意外创建无效的 `UserId`：

```python
# 'output' is of type 'int', not 'UserId'
output = UserId(23413) + UserId(54341)
```

注意，这些检查只由静态类型检查器强制执行。在运行时，语句 `Derived = NewType('Derived', Base)` 将产生一个 `Derived` 可调用对象，该对象立即返回你传递给它的任何参数。 这意味着语句 `Derived(some_value)` 不会创建一个新的类，也不会引入超出常规函数调用的很多开销。

更确切地说，在运行时，`some_value is Derived(some_value)` 表达式总为`True`。

创建 `Derived` 的子类型是无效的:

```python
from typing import NewType

UserId = NewType('UserId', int)

# Fails at runtime and does not pass type checking
class AdminUserId(UserId): pass
```

然而，我们可以在 "派生的" `NewType` 的基础上创建一个 [NewType]。

```python
from typing import NewType

UserId = NewType('UserId', int)

ProUserId = NewType('ProUserId', UserId)
```

同时，`ProUserId` 的类型检查也可以按预期执行。 详见 [PEP 484]。

> **注解**: 回顾上文，类型别名声明了两种彼此 *等价* 的类型。 `Alias = Original` 时，静态类型检查器认为 `Alias` 与 `Original` 完全等价。 这种方式适用于简化复杂类型签名。
>
> 反之，`NewType` 声明把一种类型当作另一种类型的 *子类型*。`Derived = NewType('Derived', Original)` 时，静态类型检查器把 `Derived` 当作 `Original` 的 子类 `，即，Original` 类型的值不能用在预期 `Derived` 类型的位置。这种方式适用于以最小运行时成本防止逻辑错误。

*3.5.2 新版功能.*

在 *3.10 版更改*: `NewType` 现在是一个类而不是一个函数。 在调用 `NewType` 而不是普通的函数时，会有一些额外的运行时间成本。 然而，这种开销将在 `3.11.0` 中减少。

## 可调对象（Callable）

预期特定签名回调函数的框架可以用 `Callable[[Arg1Type, Arg2Type], ReturnType]` 实现类型提示。

例如：

```python
from collections.abc import Callable

def feeder(get_next_item: Callable[[], str]) -> None:
    # Body

def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:
    # Body

async def on_update(value: str) -> None:
    # Body

callback: Callable[[str], Awaitable[None]] = on_update
```

无需指定调用签名，用省略号字面量替换类型提示里的参数列表： `Callable[..., ReturnType]`，就可以声明可调对象的返回类型。

以其他可调用对象为参数的可调用对象可以使用 [ParamSpec] 来表明其参数类型是相互依赖的。此外，如果该可调用对象增加或删除了其他可调用对象的参数，可以使用 [Concatenate] 操作符。 它们分别采取`Callable[ParamSpecVariable, ReturnType]` 和 `Callable[Concatenate[Arg1Type, Arg2Type, ..., ParamSpecVariable], ReturnType]` 的形式。

在 3.10 版更改: `Callable` now supports [ParamSpec] and [Concatenate]. See [PEP 612] for more details.

## 泛型（Generic）

容器中，对象的类型信息不能以泛型方式静态推断，因此，抽象基类扩展支持下标，用于表示容器元素的预期类型。

```python
from collections.abc import Mapping, Sequence

def notify_by_email(employees: Sequence[Employee],
                    overrides: Mapping[str, str]) -> None: ...
```

[typing] 模块中推出的 [TypeVar] 工厂函数实现泛型参数化。

```python
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T')      # Declare type variable

def first(l: Sequence[T]) -> T:   # Generic function
    return l[0]
```

## 用户定义的泛型类型

用户定义的类可以定义为泛型类。

```python
from typing import TypeVar, Generic
from logging import Logger

T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)
```

`Generic[T]` 是定义类 `LoggedVar` 的基类，该类使用单类型参数 `T`。在该类体内，`T` 是有效的类型。

[Generic] 基类定义了 [**class_getitem**()] 所以 `LoggedVar[T]` 可以作为一个有效的类型注释：

```python
from collections.abc import Iterable

def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
    for var in vars:
        var.set(0)
```

一个泛型可以有任何数量的类型变量。所有种类的 [TypeVar] 都可以作为泛型的参数:

```python
from typing import TypeVar, Generic, Sequence

T = TypeVar('T', contravariant=True)
B = TypeVar('B', bound=Sequence[bytes], covariant=True)
S = TypeVar('S', int, str)

class WeirdTrio(Generic[T, B, S]):
    ...
```

[Generic] {==类型变量的参数应各不相同==}。下列代码就是无效的：

```python
from typing import TypeVar, Generic
...

T = TypeVar('T')

class Pair(Generic[T, T]):   # INVALID
    ...
```

[Generic] 支持多重继承：

```python
from collections.abc import Sized
from typing import TypeVar, Generic

T = TypeVar('T')

class LinkedList(Sized, Generic[T]):
    ...
```

继承自泛型类时，可以修正某些类型变量：

```python
from collections.abc import Mapping
from typing import TypeVar

T = TypeVar('T')

class MyDict(Mapping[str, T]):
    ...
```

比如，本例中 `MyDict` 调用的单参数，`T`。

未指定泛型类的类型参数时，每个位置的类型都预设为 [Any]。下例中，`MyIterable` 不是泛型，但却隐式继承了 `Iterable[Any]`：

```python
from collections.abc import Iterable

class MyIterable(Iterable): # Same as Iterable[Any]
```

还支持用户定义的泛型类型别名。例如：

```python
from collections.abc import Iterable
from typing import TypeVar
S = TypeVar('S')
Response = Iterable[S] | int

# Return type here is same as Iterable[str] | int
def response(query: str) -> Response[str]:
    ...

T = TypeVar('T', int, float, complex)
Vec = Iterable[tuple[T, T]]

def inproduct(v: Vec[T]) -> T: # Same as Iterable[tuple[T, T]]
    return sum(x*y for x, y in v)
```

在 3.7 版更改: [Generic] 不再支持自定义元类。

用户定义的参数表达式的泛型也通过 `Generic[P]` 形式的参数规范变量来支持。该行为与上面描述的类型变量一致，因为参数规范变量被类型化模块视为一个专门的类型变量。 这方面的一个例外是，一个类型列表可以用来替代 [ParamSpec]:

```python
>>> from typing import Generic, ParamSpec, TypeVar

>>> T = TypeVar('T')
>>> P = ParamSpec('P')

>>> class Z(Generic[T, P]): ...
...
>>> Z[int, [dict, float]]
__main__.Z[int, (<class 'dict'>, <class 'float'>)]
```

此外，一个只有一个参数规范变量的泛型将接受表格 `X[[Type1, Type2, ...]]` 中的参数列表，出于美观的考虑也包括 `X[Type1, Type2, ...]` 。 在内部，后者被转换为前者，所以下面的内容是等价的:

```python
>>> class X(Generic[P]): ...
...
>>> X[int, str]
__main__.X[(<class 'int'>, <class 'str'>)]
>>> X[[int, str]]
__main__.X[(<class 'int'>, <class 'str'>)]
```

请注意，带有 [ParamSpec] 的泛型在某些情况下可能不会有正确的`__parameters__`，因为它们主要用于静态类型检查。

在 3.10 版更改: [Generic] 现在可以通过参数表达式进行参数化。参见 [ParamSpec] 和 [PEP 612] 以了解更多细节。

用户定义的泛型类可以将 `ABC` 作为基类，而不会发生元类冲突。 不支持通用元类。 参数化泛型的结果被缓存，并且类型模块中的大多数类型都是[可散列](https://docs.python.org/zh-cn/3.10/glossary.html#term-hashable)的并且可以比较相等性。

## Any 类型

[Any] 是一种特殊的类型。静态类型检查器认为所有类型均与 [Any] 兼容，同样，[Any] 也与所有类型兼容。

也就是说，可对 [Any] 类型的值执行任何操作或方法调用，并赋值给任意变量：

```python
from typing import Any

a: Any = None
a = []          # OK
a = 2           # OK

s: str = ''
s = a           # OK

def foo(item: Any) -> int:
    # Passes type checking; 'item' could be any type,
    # and that type might have a 'bar' method
    item.bar()
    ...
```

请注意，将 [Any] 类型的值分配给更精确的类型时，不会执行类型检查。 例如，静态类型检查器在将 `a` 分配给 `s` 时没有报告错误，即使 `s` 被声明为 `str` 类型并在运行时接收 `int` 值！

此外，未指定返回值与参数类型的函数，都隐式地默认使用 [Any]：

```python
def legacy_parser(text):
    ...
    return data

# A static type checker will treat the above
# as having the same signature as:
def legacy_parser(text: Any) -> Any:
    ...
    return data
```

需要混用动态与静态类型代码时，此操作把 [Any] 当作 *应急出口*。

[Any] 和 [object] 的区别。与 [Any] 相似，所有类型都是 [object] 的子类型。然而，与 [Any] 不同，[object] 不可逆：[object] *不是* 其它类型的子类型。

就是说，值的类型是 [object] 时，类型检查器几乎会拒绝所有对它的操作，并且，把它赋给更精确的类型变量（或返回值）属于类型错误。例如：

```python
def hash_a(item: object) -> int:
    # Fails type checking; an object does not have a 'magic' method.
    # 类型检查失败； 任何obje对象都没有“magic”方法。
    item.magic()
    ...

def hash_b(item: Any) -> int:
    # Passes type checking
    # 通过类型检查
    item.magic()
    ...

# Passes type checking, since ints and strs are subclasses of object
# 通过类型检查，因为 int 和 str 是object的子类
hash_a(42)
hash_a("foo")

# Passes type checking, since Any is compatible with all types
# 通过类型检查，因为 Any 与所有类型兼容
hash_b(42)
hash_b("foo")
```

{==**使用 [object]，说明值能以类型安全的方式转为任何类型。使用 [Any]，说明值是动态类型。**==}

## 名义子类型 vs 结构子类型

最初 [PEP 484] 将 Python 静态类型系统定义为使用 *名义子类型*。这意味着当且仅当类 `A` 是 `B` 的子类时，才满足有类 `B` 预期时使用类 `A` 。

此项要求以前也适用于抽象基类，例如，[Iterable] 。这种方式的问题在于，定义类时必须显式说明，既不 Pythonic，也不是动态类型式 Python 代码的惯用写法。例如，下列代码就遵从了 [PEP 484] 的规范：

```python
from collections.abc import Sized, Iterable, Iterator

class Bucket(Sized, Iterable[int]):
    ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...
```

[PEP 544] 允许用户在类定义时不显式说明基类，从而解决了这一问题，静态类型检查器隐式认为 `Bucket` 既是 `Sized` 的子类型，又是 `Iterable[int]` 的子类型。这就是 *结构子类型* （又称为静态鸭子类型）：

```python
from collections.abc import Iterator, Iterable

class Bucket:  # Note: 没有基类
    ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...

def collect(items: Iterable[int]) -> int: ...
result = collect(Bucket())  # 通过类型检查
```

此外，结构子类型的优势在于，通过继承特殊类 [Protocol] ，用户可以定义新的自定义协议（见下文中的例子）。

## 模块内容

本模块定义了下列类、函数和修饰器。

> **注解**: 本模块定义了一些类型，作为标准库中已有的类的子类，从而可以让 [Generic] 支持 [] 中的类型变量。Python 3.9 中，这些标准库的类已支持 `[]` ，因此，这些类型就变得冗余了。
>
> Python 3.9 弃用了这些冗余类型，但解释器并未提供相应的弃用警告。标记弃用类型的工作留待支持 Python 3.9 及以上版本的类型检查器实现。
>
> Python 3.9.0 发布五年后的首个 Python 发行版将从 [typing] 模块中移除这些弃用类型。详见 [PEP 585] 《标准集合的类型提示泛型》。

### 特殊类型原语

#### 特殊类型

{++这些类型可用于类型注解，但不支持 `[]`。++}

##### typing.Any

不受限的特殊类型。

- 所有类型都与 [Any] 兼容。
- [Any] 与所有类型都兼容。

##### typing.NoReturn

标记没有返回值的函数的特殊类型。例如：

```python
from typing import NoReturn

def stop() -> NoReturn:
    raise RuntimeError('no way')
```

##### typing.TypeAlias

用于显式声明 [类型别名] 的特殊标注。 例如:

```python
from typing import TypeAlias

Factors: TypeAlias = list[int]
```

关于显式类型别名的更多细节，请参见 [PEP 613]。

#### 特殊形式

{==可用于类型注解，且支持 `[]` ，每种形式都有其独特的句法。==}

##### typing.Tuple

元组类型； `Tuple[X, Y]` 是二项元组类型，第一个元素的类型是 `X`，第二个元素的类型是 `Y`。空元组的类型可写为 `Tuple[()]`。

例：`Tuple[T1, T2]` 是二项元组，类型变量分别为 `T1` 和 `T2`。`Tuple[int, float, str]` 是由整数、浮点数、字符串组成的三项元组。

可用省略号字面量指定同质变长元组，例如，`Tuple[int, ...]` 。`Tuple` 与 `Tuple[Any, ...]` 等价，也与 `tuple` 等价。

##### typing.Union

联合类型； `Union[X, Y]` 等价于 `X | Y` ，意味着满足 `X` 或 `Y` 之一。

要定义一个联合类型，可以使用类似 `Union[int, str]` 或简写 `int | str`。建议使用这种简写。细节:

- 参数必须是某种类型，且至少有一个。
- 联合类型之联合类型会被展平，例如：

    ```python
    Union[Union[int, str], float] == Union[int, str, float]
    ```

- 单参数之联合类型就是该参数自身，例如：

    ```python
    Union[int] == int  # The constructor actually returns int
    ```

- 冗余的参数会被跳过，例如：

    ```python
    Union[int, str, int] == Union[int, str] == int | str
    ```

- 比较联合类型，不涉及参数顺序，例如：

    ```python
    Union[int, str] == Union[str, int]
    ```

- `Union` 不能作为子类，也不能实例化。
- 不支持 `Union[X][Y]` 这种写法。

在 3.7 版更改: 在运行时，不要移除联合类型中的显式子类。

在 3.10 版更改: 联合类型现在可以写成 `X | Y`。 参见 [联合类型表达式]。

##### typing.Optional

可选类型。

`Optional[X]` 等价于 `X | None` （或 `Union[X, None]` ） 。

注意，可选类型与含默认值的可选参数不同。含默认值的可选参数不需要在类型注解上添加 `Optional` 限定符，因为它仅是可选的。例如：

```python
def foo(arg: int = 0) -> None:
    ...
```

另一方面，显式应用 `None` 值时，不管该参数是否可选， `Optional` 都适用。例如：

```python
def foo(arg: Optional[int] = None) -> None:
    ...
```

在 3.10 版更改: 可选参数现在可以写成 `X | None`。 参见 [联合类型表达式]。

##### typing.Callable

可调类型； `Callable[[int], str]` 是把`（int）`转为 `str` 的函数。

下标句法必须与参数列表和返回类型这两个值一起使用。参数列表只能是类型列表或省略号；返回类型只能是单一类型。

没有说明可选参数或关键字参数的句法；这类函数类型很少用作回调类型。`Callable[..., ReturnType]` （省略号字面量）可用于为接受任意数量参数，并返回 `ReturnType` 的可调对象提供类型提示。
纯 [Callable] 等价于 `Callable[..., Any]`，进而等价于 [collections.abc.Callable] 。

以其他可调用对象为参数的可调用对象可以使用 [ParamSpec] 来表明其参数类型是相互依赖的。此外，如果该可调用对象增加或删除了其他可调用对象的参数，可以使用 [Concatenate] 操作符。 它们分别采取`Callable[ParamSpecVariable, ReturnType]` 和 `Callable[Concatenate[Arg1Type, Arg2Type, ..., ParamSpecVariable], ReturnType]` 的形式。

3.9 版后已移除: `collections.abc.Callable` now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

在 3.10 版更改: `Callable` now supports [ParamSpec] and [Concatenate]. See [PEP 612] for more details.

> **参见** [ParamSpec] 和 [Concatenate] 的文档提供了使用 `Callable` 的例子。

##### typing.Concatenate

与 [Callable] 和 [ParamSpec] 一起使用，对一个高阶可调用对象进行类型注释，该对象可以增加、删除或转换另一个可调用对象的参数。 使用形式为`Concatenate[Arg1Type, Arg2Type, ..., ParamSpecVariable]`。 `Concatenate` 目前只在作为 [Callable] 的第一个参数时有效。Concatenate` 的最后一个参数必须是一个 [ParamSpec]。

例如，为了注释一个装饰器 `with_lock`，它为被装饰的函数提供了 [threading.Lock]，`Concatenate` 可以用来表示 `with_lock` 期望一个可调用对象，该对象接收一个 `Lock` 作为第一个参数，并返回一个具有不同类型签名的可调用对象。 在这种情况下，[ParamSpec] 表示返回的可调用对象的参数类型取决于被传入的可调用程序的参数类型:

```python
from collections.abc import Callable
from threading import Lock
from typing import Concatenate, ParamSpec, TypeVar

P = ParamSpec('P')
R = TypeVar('R')

# Use this lock to ensure that only one thread is executing a function
# at any time.
# 使用这个锁可以保证任何时候只有一个线程在执行一个函数。
my_lock = Lock()

def with_lock(f: Callable[Concatenate[Lock, P], R]) -> Callable[P, R]:
    '''A type-safe decorator which provides a lock.'''
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        # Provide the lock as the first argument.
        # 提供锁的类型安全装饰器。
        return f(my_lock, *args, **kwargs)
    return inner

@with_lock
def sum_threadsafe(lock: Lock, numbers: list[float]) -> float:
    '''Add a list of numbers together in a thread-safe manner.'''
    # 以线程安全的方式将数字列表加在一起。
    with lock:
        return sum(numbers)

# We don't need to pass in the lock ourselves thanks to the decorator.
# 多亏了装饰器，我们不需要自己传入锁。
sum_threadsafe([1.1, 2.2, 3.3])
```

3.10 新版功能.

> **参见**:
>  
> - [PEP 612] -- 参数规范变量（引入 `ParamSpec` 和 `Concatenate` 的 PEP）。
> - [ParamSpec] 和 [Callable]。

##### class typing.Type(Generic[CT_co])

用 `C` 注解的变量可以接受类型 `C` 的值。反之，用 `Type[C]` 注解的变量可以接受类自身的值 — 准确地说，是接受 `C` 的 *类对象*，例如：

```python
a = 3         # Has type 'int'
b = int       # Has type 'Type[int]'
c = type(a)   # Also has type 'Type[int]'
```

注意，`Type[C]` 为协变量：

```python
class User: ...
class BasicUser(User): ...
class ProUser(User): ...
class TeamUser(User): ...

# Accepts User, BasicUser, ProUser, TeamUser, ...
def make_new_user(user_class: Type[User]) -> User:
    # ...
    return user_class()
```

`Type[C]` 为协变量的意思是指， `C` 的所有子类都应使用与 `C` 相同的构造器签名及类方法签名。类型检查器应标记违反此项规定的内容，但也应允许符合指定基类构造器调用的子类进行构造器调用。[PEP 484] 修订版将来可能会调整类型检查器对这种特例的处理方式。

 `Type` 合法的参数仅有类、`Any` 、[类型变量] 以及上述类型的联合类型。例如：

```python
def new_non_team_user(user_class: Type[BasicUser | ProUser]): ...
```

`Type[Any]` 等价于 `Type`，进而等价于 Python 元类架构的根基，`type`。

3.5.2 新版功能.

3.9 版后已移除: [builtins.type] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

##### typing.Literal

表示类型检查器对应变量或函数参数的值等价于给定字面量（或多个字面量之一）的类型。例如：

```python
def validate_simple(data: Any) -> Literal[True]:  # always returns True
    ...

MODE = Literal['r', 'rb', 'w', 'wb']
def open_helper(file: str, mode: MODE) -> str:
    ...

open_helper('/some/path', 'r')  # Passes type check
open_helper('/other/path', 'typo')  # Error in type checker
```

`Literal[...]` 不能创建子类。在运行时，任意值均可作为 `Literal[...]` 的类型参数，但类型检查器可以对此加以限制。字面量类型详见 [PEP 586] 。

3.8 新版功能.

在 3.9.1 版更改: `Literal` 现在能去除形参的重复。 `Literal` 对象的相等性比较不再依赖顺序。 现在如果有某个参数不为 [hashable]，`Literal` 对象在相等性比较期间将引发 [TypeError]。

##### typing.ClassVar

标记类变量的特殊类型构造器。

如 [PEP 526] 所述，打包在 `ClassVar` 内的变量注解是指，给定属性应当用作类变量，而不应设置在类实例上。用法如下：

```python
class Starship:
    stats: ClassVar[dict[str, int]] = {} # class variable
    damage: int = 10                     # instance variable
```

[ClassVar] 仅接受类型，也不能使用下标。

[ClassVar] 本身不是类，不应用于 [isinstance()] 或 [issubclass()]。[ClassVar] 不改变 Python 运行时行为，但可以用于第三方类型检查器。例如，类型检查器会认为以下代码有错：

```python
enterprise_d = Starship(3000)
enterprise_d.stats = {} # Error, setting class variable on instance
Starship.stats = {}     # This is OK
```

3.5.3 新版功能.

##### typing.Final

{==**告知类型检查器某名称不能再次赋值或在子类中重写的特殊类型构造器**==}。例如：

```python
MAX_SIZE: Final = 9000
MAX_SIZE += 1  # Error reported by type checker

class Connection:
    TIMEOUT: Final[int] = 10

class FastConnector(Connection):
    TIMEOUT = 1  # Error reported by type checker
```

这些属性没有运行时检查。详见 [PEP 591]。

3.8 新版功能.

##### typing.Annotated

[PEP 593] （*灵活函数和变量注解*）里引入的类型，可以用上下文特定元数据（`Annotated` 的参数可变，也可能用它的多个组成部分）装饰现有的类型。具体来说，就是类型提示 `Annotated[T, x]` 用元数据 `x` 注解类型 `T`。
静态分析或运行时都能使用该元数据。库（或工具）处理类型提示 `Annotated[T, x]` 时，在元数据 `x` 不涉及特殊逻辑的情况下，可忽略该类型提示，仅把它当作类型 `T`。
与 `typing` 模块中现有的 `no_type_check` 功能不同，该功能完全禁用了函数或类的类型检查注解，而 `Annotated` 类型则允许对 `T` 进行静态类型检查（可安全地忽略 `x`），
也可以在特定应用程序中实现 `x` 的运行时访问。

毕竟，如何解释注解（如有）由处理 `Annotated` 类型的工具/库负责。工具/库处理 Annotated 类型时，扫描所有注解以确定是否需要进行处理（例如，使用 `isinstance()`）。

工具/库不支持注解，或遇到未知注解时，应忽略注解，并把注解类型当作底层类型。

是否允许客户端在一个类型上使用多个注解，以及如何合并这些注解，由处理注解的工具决定。

`Annotated` 类型支持把多个相同（或不同）的单个（或多个）类型注解置于任意节点。因此，使用这些注解的工具/库要负责处理潜在的重复项。例如，执行值范围分析时，应允许以下操作：

```python
T1 = Annotated[int, ValueRange(-10, 5)]
T2 = Annotated[T1, ValueRange(-20, 3)]
```

传递 `include_extras=True` 至 [get_type_hints()] ，即可在运行时访问额外的注解。

语义详情：

- `Annotated` 的第一个参数必须是有效类型。
- 支持多个类型标注（`Annotated` 支持可变参数）：

    ```python
    Annotated[int, ValueRange(3, 10), ctype("char")]
    ```

- 调用 `Annotated` 至少要有两个参数（`Annotated[int]` 是无效的）
- 注解的顺序会被保留，且影响等价检查：

    ```python
    Annotated[int, ValueRange(3, 10), ctype("char")] != Annotated[
        int, ctype("char"), ValueRange(3, 10)
    ]
    ```

- 嵌套 `Annotated` 类型会被展平，元数据从最内层注解依序展开：

    ```python
    Annotated[Annotated[int, ValueRange(3, 10)], ctype("char")] == Annotated[
        int, ValueRange(3, 10), ctype("char")
    ]
    ```

- 不移除注解重复项：

    ```python
    Annotated[int, ValueRange(3, 10)] != Annotated[
        int, ValueRange(3, 10), ValueRange(3, 10)
    ]
    ```

- `Annotated` 可用于嵌套或泛型别名：

    ```python
    T = TypeVar('T')
    Vec = Annotated[list[tuple[T, T]], MaxLen(10)]
    V = Vec[int]
    
    V == Annotated[list[tuple[int, int]], MaxLen(10)]
    ```

3.9 新版功能.

##### typing.TypeGuard

用于注释用户定义的类型保护函数的返回类型的特殊类型化形式。 `TypeGuard` 只接受一个单一的类型参数。 在运行时，以这种方式标记的函数应该返回一个布尔值。

PX旨在使 *类型缩小* 受益--这是静态类型检查器用来确定程序代码流中表达式的更精确类型的一种技术。通常，类型缩小是通过分析条件性代码流并将缩小的结果应用于一个代码块来完成的。 这里的条件表达式有时被称为 "类型保护":

```python
def is_str(val: str | float):
    # "isinstance" type guard
    if isinstance(val, str):
        # Type of ``val`` is narrowed to ``str``
        ...
    else:
        # Else, type of ``val`` is narrowed to ``float``.
        ...
```

有时，使用一个用户定义的布尔函数作为类型保护会很方便。 这样的函数应该使用 `TypeGuard[...]` 作为其返回类型，以提醒静态类型检查器注意这一意图。

对于一个给定的函数，使用 `-> TypeGuard` 告诉静态类型检查器:

1. 返回值是一个布尔值。
2. 如果返回值是 `True`，其参数的类型是 `TypeGuard` 里面的类型。

例如：

```python
def is_str_list(val: List[object]) -> TypeGuard[List[str]]:
    '''Determines whether all objects in the list are strings'''
    return all(isinstance(x, str) for x in val)

def func1(val: List[object]):
    if is_str_list(val):
        # Type of ``val`` is narrowed to ``List[str]``.
        print(" ".join(val))
    else:
        # Type of ``val`` remains as ``List[object]``.
        print("Not a list of strings!")
```

如果 `is_str_list` 是一个类或实例方法，那么 `TypeGuard` 中的类型映射到 `cls` 或 `self` 之后的第二个参数的类型。

简而言之，`def foo(arg: TypeA) -> TypeGuard[TypeB]: ...` 形式的意思是：如果 `foo(arg)` 返回 `True`，那么 `arg` 将把 `TypeA` 缩小为 `TypeB`。

> **注解**:
>
> `TypeB` 不必是 `TypeA` 的缩小形式，它甚至可以是扩大形式。 主要原因是允许像把 `List[object]` 缩小到 `List[str]` 这样的事情，即使后者不是前者的一个子类型，因为 `List` 是不变的。 编写类型安全的类型防护的责任留给了用户。

`TypeGuard` also works with type variables. See [PEP 647] for more details.

3.10 新版功能.

#### 构建泛型类型

以下内容是创建泛型类型的基石，但不在注解内使用。

##### class typing.Generic

用于泛型类型的抽象基类。

泛型类型一般通过继承含一个或多个类型变量的类实例进行声明。例如，泛型映射类型定义如下：

```python
class Mapping(Generic[KT, VT]):
    def __getitem__(self, key: KT) -> VT:
        ...
        # Etc.
```

该类的用法如下：

```python
X = TypeVar('X')
Y = TypeVar('Y')

def lookup_name(mapping: Mapping[X, Y], key: X, default: Y) -> Y:
    try:
        return mapping[key]
    except KeyError:
        return default
```

##### class typing.TypeVar

类型变量。

用法：

```python
T = TypeVar('T')  # Can be anything
S = TypeVar('S', bound=str)  # Can be any subtype of str
A = TypeVar('A', str, bytes)  # Must be exactly str or bytes
```

类型变量主要是为静态类型检查器提供支持，用于泛型类型与泛型函数定义的参数。有关泛型类型，详见 [Generic]。泛型函数的写法如下：

```python
def repeat(x: T, n: int) -> Sequence[T]:
    """Return a list containing n references to x."""
    return [x]*n


def print_capitalized(x: S) -> S:
    """Print x capitalized, and return x."""
    print(x.capitalize())
    return x


def concatenate(x: A, y: A) -> A:
    """Add two strings or bytes objects together."""
    return x + y
```

请注意，类型变量可以是 *被绑定的* ， *被约束的* ，或者两者都不是，但不能既是被绑定的 *又是* 被约束的。

约束类型变量和绑定类型变量在几个重要方面具有不同的语义。使用 *约束* 类型变量意味着它只能被解析为正好是所给的约束之一:

```python
a = concatenate('one', 'two')  # Ok, variable 'a' has type 'str'
b = concatenate(StringSubclass('one'), StringSubclass('two'))  # Inferred type of variable 'b' is 'str',
                                                               # despite 'StringSubclass' being passed in
c = concatenate('one', b'two')  # error: type variable 'A' can be either 'str' or 'bytes' in a function call, but not both
```

然而，使用一个 *绑定* 类型变量，意味着将使用最具体的类型来解析 `TypeVar`

```python
print_capitalized('a string')  # Ok, output has type 'str'

class StringSubclass(str):
    pass

print_capitalized(StringSubclass('another string'))  # Ok, output has type 'StringSubclass'
print_capitalized(45)  # error: int is not a subtype of str
```

类型变量可以被绑定到具体类型、抽象类型（ `ABC` 或 `protocol` ），甚至是类型的联合:

```python
U = TypeVar('U', bound=str|bytes)  # Can be any subtype of the union str|bytes
V = TypeVar('V', bound=SupportsAbs)  # Can be anything with an __abs__ method
```

绑定类型变量对于注释用作替代构造函数的[类方法]特别有用。
在以下示例中（由 [Raymond Hettinger] 编写），类型变量 `C` 通过使用前向引用绑定到 `Circle` 类。
使用此类型变量来注释 `with_circumference` 类方法，而不是将返回类型硬编码为 `Circle`，这意味着即使在子类上调用该方法，类型检查器也可以正确推断返回类型：

```python
import math

C = TypeVar('C', bound='Circle')

class Circle:
    """An abstract circle"""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    # Use a type variable to show that the return type
    # will always be an instance of whatever ``cls`` is
    @classmethod
    def with_circumference(cls: type[C], circumference: float) -> C:
        """Create a circle with the specified circumference"""
        radius = circumference / (math.pi * 2)
        return cls(radius)


class Tire(Circle):
    """A specialised circle (made out of rubber)"""

    MATERIAL = 'rubber'


c = Circle.with_circumference(3)  # Ok, variable 'c' has type 'Circle'
t = Tire.with_circumference(4)  # Ok, variable 't' has type 'Tire' (not 'Circle')
```

在运行时，`isinstance(x, T)` 会触发 `TypeError` 异常。一般而言，`isinstance()` 和 `issubclass()` 不应与类型搭配使用。

类型变量可以通过传递 `covariant=True` 或 `contravariant=True` 来标记协变或反变。 更多细节请参见 [PEP 484] 。 默认情况下，类型变量是不变的。

##### class typing.ParamSpec

**class typing.ParamSpec(name, *, bound=None, covariant=False, contravariant=False)**

参数规范变量。 [类型变量] 的一个专门版本。

用法：

```python
P = ParamSpec('P')
```

参数规范变量的存在主要是为了使静态类型检查器受益。 它们被用来将一个可调用对象的参数类型转发给另一个可调用对象的参数类型——这种模式通常出现在高阶函数和装饰器中。
它们只有在 `Concatenate` 中使用时才有效，或者作为 `Callable` 的第一个参数，或者作为用户定义的泛型的参数。 参见 [Generic] 以了解更多关于泛型的信息。

例如，为了给一个函数添加基本的日志记录，我们可以创建一个装饰器 `add_logging` 来记录函数调用。 参数规范变量告诉类型检查器，传入装饰器的可调用对象和由其返回的新可调用对象有相互依赖的类型参数:

```python
from collections.abc import Callable
from typing import TypeVar, ParamSpec
import logging

T = TypeVar('T')
P = ParamSpec('P')

def add_logging(f: Callable[P, T]) -> Callable[P, T]:
    '''A type-safe decorator to add logging to a function.'''
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        logging.info(f'{f.__name__} was called')
        return f(*args, **kwargs)
    return inner

@add_logging
def add_two(x: float, y: float) -> float:
    '''Add two numbers together.'''
    return x + y
```

如果没有 [ParamSpec]，以前注释这个的最简单的方法是使用一个 [TypeVar] 与绑定 `Callable[..., Any]`。

1. 类型检查器不能对 `inner` 函数进行类型检查，因为 `*args` 和 `**kwargs` 的类型必须是 [Any]。
2. [cast()] 在返回 `inner` 函数时，可能需要在 `add_logging` 装饰器的主体中进行，或者必须告诉静态类型检查器忽略 `return inner`。

###### args
###### Kwargs

    由于 `ParamSpec` 同时捕获了位置参数和关键字参数，`P.args` 和 `P.kwargs` 可以用来将 `ParamSpec` 分割成其组成部分。 `P.args` 代表给定调用中的位置参数的元组，只能用于注释 `*args`。 `P.kwargs` 代表给定调用中的关键字参数到其值的映射，只能用于注释 `**kwargs`。在运行时，`P.args` 和 `P.kwargs` 分别是 [ParamSpecArgs] 和 [ParamSpecKwargs] 的实例。

用 `covariant=True` 或 `contravariant=True` 创建的参数规范变量可以用来声明协变或禁变的通用类型。 参数 `bound` 也被接受，类似于 `TypeVar`。 然而这些关键字的实际语义还有待决定。

3.10 新版功能.

> 注解: 只有在全局范围内定义的参数规范变量可以被 pickle。

> 参见
>
> - [PEP 612] -- 参数规范变量（引入 `ParamSpec` 和 `Concatenate` 的 PEP）。
> - [Callable] 和 [Concatenate]。

##### typing.ParamSpecArgs
##### typing.ParamSpecKwargs

`ParamSpec`的参数和关键字参数属性。`ParamSpec` 的 `P.args` 属性是 `ParamSpecArgs` 的一个实例，`P.kwargs` 是 `ParamSpecKwargs` 的一个实例。 它们的目的是用于运行时内部检查的，对静态类型检查器没有特殊意义。

在这些对象中的任何一个上调用 `get_origin()`，都会返回原始的 `ParamSpec`:

```python
P = ParamSpec("P")
get_origin(P.args)  # returns P
get_origin(P.kwargs)  # returns P
```

3.10 新版功能.

##### typing.AnyStr

`AnyStr` 定义为 `AnyStr = TypeVar('AnyStr', str, bytes)` 的 [约束类型变量] 。

这里指的是，它可以接受任意同类字符串，但不支持混用不同类别的字符串。例如：

```python
def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b

concat(u"foo", u"bar")  # Ok, output has type 'unicode'
concat(b"foo", b"bar")  # Ok, output has type 'bytes'
concat(u"foo", b"bar")  # Error, cannot mix unicode and bytes
```

##### class typing.Protocol(Generic)

`Protocol` 类的基类。`Protocol` 类的定义如下：

```python
class Proto(Protocol):
    def meth(self) -> int:
        ...
```

这些类主要与静态类型检查器搭配使用，用来识别结构子类型（静态鸭子类型），例如：

```python
class C:
    def meth(self) -> int:
        return 0

def func(x: Proto) -> int:
    return x.meth()

func(C())  # Passes static type check
```

有关详细信息，请参阅 [PEP 544]。 用 [runtime_checkable()] 装饰的协议类（稍后描述）充当头脑简单的运行时协议，只检查给定属性的存在，忽略它们的类型签名。

`Protocol` 类可以是泛型，例如：

```python
class GenProto(Protocol[T]):
    def meth(self) -> T:
        ...
```

3.8 新版功能.

##### @typing.runtime_checkable

用于把 `Protocol` 类标记为运行时协议。

该协议可以与 `isinstance()` 和 `issubclass()` 一起使用。应用于非协议的类时，会触发 `TypeError`。该指令支持简易结构检查，与 `collections.abc` 的 `Iterable` 非常类似，只擅长做一件事。 例如：

```python
@runtime_checkable
class Closable(Protocol):
    def close(self): ...

assert isinstance(open('/some/file'), Closable)

@runtime_checkable
class Named(Protocol):
    name: str

import threading
assert isinstance(threading.Thread(name='Bob'), Named)
```

> 注解: `runtime_checkable()` 将只检查所需方法或属性的存在，而不是它们的类型签名或类型。 例如，[ssl.SSLObject] 是一个类，因此它通过了针对 [Callable] 的 [issubclass()] 检查。 但是，`ssl.SSLObject.__init__` 方法的存在只是为了引发 [TypeError] 并提供更多信息，因此无法调用（实例化）[ssl.SSLObject]。
>
>
> 注解: 与针对非协议类的 `isinstance()` 检查相比，针对运行时可检查协议的 `isinstance()` 检查可能出奇地慢。 考虑使用替代习惯用法，例如 `hasattr()` 调用以在性能敏感代码中进行结构检查。

3.8 新版功能.

#### 其他特殊指令

这些特殊指令是声明类型的基石，但不在注解内使用。

##### class typing.NamedTuple

[collections.namedtuple()] 的类型版本。

用法：

```python
class Employee(NamedTuple):
    name: str
    id: int
```

这相当于：

```python
Employee = collections.namedtuple('Employee', ['name', 'id'])
```

为字段提供默认值，要在类体内赋值：

```python
class Employee(NamedTuple):
    name: str
    id: int = 3  # 带默认值的字段必须在不带默认值的字段后面。

employee = Employee('Guido')
assert employee.id == 3
```

带默认值的字段必须在不带默认值的字段后面。

由此产生的类有一个额外的属性 `__annotations__` ，给出一个 dict ，将字段名映射到字段类型。（字段名在 `_fields` 属性中，默认值在 `_field_defaults` 属性中，这两者都是 [namedtuple()] API 的一部分。）

`NamedTuple` 子类也支持文档字符串与方法：

```python
class Employee(NamedTuple):
    """Represents an employee."""
    name: str
    id: int = 3

    def __repr__(self) -> str:
        return f'<Employee {self.name}, id={self.id}>'
```

反向兼容法:

```python
Employee = NamedTuple('Employee', [('name', str), ('id', int)])
```

在 3.6 版更改: 添加了对 [PEP 526] 中变量注解句法的支持。

在 3.6.1 版更改: 添加了对默认值、方法、文档字符串的支持。

在 3.8 版更改: `_field_types` 和 `__annotations__` 属性现已使用常规字典，不再使用 `OrderedDict` 实例。

在 3.9 版更改: 移除了 `_field_types` 属性， 改用具有相同信息，但更标准的 `__annotations__` 属性。

##### class typing.NewType(name, tp)

一个辅助类，用于向类型检查器指示一个不同的类型，见 [NewType]。在运行时，它返回一个对象，在调用时返回其参数。用法:

```python
UserId = NewType('UserId', int)
first_user = UserId(1)
```

3.5.2 新版功能.

在 3.10 版更改: `NewType` 现在是一个类而不是函数。

##### class typing.TypedDict(dict)

把类型提示添加至字典的特殊构造器。在运行时，它是纯 [dict]。

`TypedDict` 声明一个字典类型，该类型预期所有实例都具有一组键集，其中，每个键都与对应类型的值关联。运行时不检查此预期，而是由类型检查器强制执行。用法如下：

```python
class Point2D(TypedDict):
    x: int
    y: int
    label: str

a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check

assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')
```

为了允许在不支持 [PEP 526] 的旧版本的 Python 中使用这个特性， `TypedDict` 支持另外两种等价的语法形式:

```python
Point2D = TypedDict('Point2D', x=int, y=int, label=str)
Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str})
```

当任何一个键不是有效的 [标识符] 时，例如因为它们是关键字或包含连字符，也应该使用函数式语法。例子:

```python
# raises SyntaxError
class Point2D(TypedDict):
    in: int  # 'in' is a keyword
    x-y: int  # name with hyphens

# OK, functional syntax
Point2D = TypedDict('Point2D', {'in': int, 'x-y': int})
```

默认情况下，所有的键都必须出现在一个 `TypedDict` 中。 可以通过指定总数来重写这一点。用法:

```python
class Point2D(TypedDict, total=False):
    x: int
    y: int
```

这意味着一个 `Point2D` `TypedDict` 可以省略任何一个键。 类型检查器只需要支持一个字面的 `False` 或 `True` 作为 `total` 参数的值。 `True` 是默认的，它使类主体中定义的所有项目都是必需的。

一个 `TypedDict` 类型有可能使用基于类的语法从一个或多个其他 `TypedDict` 类型继承。用法:

```python
class Point3D(Point2D):
    z: int
```

`Point3D` 有三个项目 : `x` , `y` 和 `z` 。 其等价于定义:

```python
class Point3D(TypedDict):
    x: int
    y: int
    z: int
```

`TypedDict` 不能继承于一个非 `TypedDict` 类，其中特别包括 [Generic] 。例如：

```python
class X(TypedDict):
    x: int

class Y(TypedDict):
    y: int

class Z(object): pass  # A non-TypedDict class

class XY(X, Y): pass  # OK

class XZ(X, Z): pass  # raises TypeError

T = TypeVar('T')
class XT(X, Generic[T]): pass  # raises TypeError
```

`TypedDict` 可以通过注解字典（参见 [对象注解属性的最佳实践] 了解更多关于注解的最佳实践）、 [**total**] 、 [**required_keys**] 和 [**optional_keys**] 进行内省。

###### \_\_total\_\_

`Point2D.__total__` 给出总参数的值。 例子：

```python
>>> from typing import TypedDict
>>> class Point2D(TypedDict): pass
>>> Point2D.__total__
True
>>> class Point2D(TypedDict, total=False): pass
>>> Point2D.__total__
False
>>> class Point3D(Point2D): pass
>>> Point3D.__total__
True
```

###### \_\_required_keys\_\_

3.9 新版功能.

###### \_\_optional_keys\_\_

`Point2D.__required_keys__` 和 `Point2D.__optional_keys__` 分别返回 [frozenset] 对象，其中包含必需和非必需键。目前，在同一个 中声明必需和非必需键的唯一方法是混合继承，用一个 `total` 参数值声明一个 `TypedDict` ，然后从另一个 `total` 参数值不同的 `TypedDict` 中继承它。用法：

```python
>>> class Point2D(TypedDict, total=False):
...     x: int
...     y: int
...
>>> class Point3D(Point2D):
...     z: int
...
>>> Point3D.__required_keys__ == frozenset({'z'})
True
>>> Point3D.__optional_keys__ == frozenset({'x', 'y'})
True
```

3.9 新版功能.

更多示例与 `TypedDict` 的详细规则，详见 [PEP 589]。

3.8 新版功能.

### 泛型具象容器

#### 对应的内置类型

##### class typing.Dict(dict, MutableMapping[KT, VT])

[dict] 的泛型版本。适用于注解返回类型。注解参数时，最好使用 [Mapping] 等抽象容器类型。

该类型用法如下：

```python
def count_words(text: str) -> Dict[str, int]:
    ...
```

3.9 版后已移除: [builtins.dict] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

##### class typing.List(list, MutableSequence[T])

[list] 的泛型版本。适用于注解返回类型。注解参数时，最好使用 [Sequence] 或 [Iterable] 等抽象容器类型。

该类型用法如下：

```python
T = TypeVar('T', int, float)

def vec2(x: T, y: T) -> List[T]:
    return [x, y]

def keep_positives(vector: Sequence[T]) -> List[T]:
    return [item for item in vector if item > 0]
```

3.9 版后已移除: [builtins.list] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

##### class typing.Set(set, MutableSet[T])

[builtins.set] 的泛型版本。适用于注解返回类型。注解参数时，最好使用 [AbstractSet] 等抽象容器类型。

3.9 版后已移除: [builtins.set] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

##### class typing.FrozenSet(frozenset, AbstractSet[T_co])

[builtins.frozenset] 的泛型版本。

3.9 版后已移除: [builtins.frozenset] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

> **注解** [Tuple] 是一种特殊形式。

#### [collections] 对应类型

##### class typing.DefaultDict(collections.defaultdict, MutableMapping[KT, VT])

[collections.defaultdict] 的泛型版本。

3.5.2 新版功能.

3.9 版后已移除: [collections.defaultdict] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

##### class typing.OrderedDict(collections.OrderedDict, MutableMapping[KT, VT])

[collections.OrderedDict] 的泛型版本。

3.7.2 新版功能.

3.9 版后已移除: [collections.OrderedDict] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

##### class typing.ChainMap(collections.ChainMap, MutableMapping[KT, VT])

[collections.ChainMap] 的泛型版本。

3.5.4 新版功能.

3.6.1 新版功能.

3.9 版后已移除: [collections.ChainMap] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

##### class typing.Counter(collections.Counter, Dict[T, int])

[collections.Counter] 的泛型版本。

3.5.4 新版功能.

3.6.1 新版功能.

3.9 版后已移除: [collections.Counter] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

##### class typing.Deque(deque, MutableSequence[T])

[collections.deque] 的泛型版本。

3.5.4 新版功能.

3.6.1 新版功能.

3.9 版后已移除: [collections.deque] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

#### 其他具象类型

##### class typing.IO
##### class typing.TextIO
##### calss typing.BinaryIO

泛型类型 `IO[AnyStr]` 及其子类 `TextIO(IO[str])` 与 `BinaryIO(IO[bytes])` 表示 I/O 流的类型，例如 [open()] 所返回的对象。

从版本 3.8 开始标记为过时，将在版本 3.13 中移除。 `typing.io` 命名空间已被废弃并将被删除。这些类型应该被直接从 `typing` 导入。

##### class typing.Pattern
##### class typing.Match

这些类型对应的是从 [re.compile()] 和 [re.match()] 返回的类型。 这些类型（及相应的函数）是 `AnyStr` 中的泛型并可通过编写 `Pattern[str]`, `Pattern[bytes]`, `Match[str]` 或 `Match[bytes]` 来具体指定。

从版本 3.8 开始标记为过时，将在版本 3.13 中移除。 `typing.re` 命名空间已被废弃并将被删除。这些类型应该被直接从 `typing` 导入。

3.9 版后已移除: [re] 模块中的 `Pattern` 与 `Match` 类现已支持 `[]`。详见 [PEP 585] 与 [GenericAlias 类型]。

##### class typing.Text

`Text` 是 `str` 的别名。提供了对 Python 2 代码的向下兼容Python 2 中，`Text` 是 unicode 的别名。

使用 `Text` 时，值中必须包含 `unicode` 字符串，以兼容 Python 2 和 Python 3：

```python
def add_unicode_checkmark(text: Text) -> Text:
    return text + u' \u2713'
```

3.5.2 新版功能.

### 抽象基类

#### [collections.abc] 对应的容器

##### class typing.AbstractSet(Collection[T_co])

[collections.abc.Set] 的泛型版本。

3.9 版后已移除: [collections.abc.Set] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

##### class typing.ByteString(Sequence[int])

[collections.abc.ByteString] 的泛型版本。

该类型代表了 [bytes]、[bytearray]、[memoryview] 等字节序列类型。

作为该类型的简称，[bytes] 可用于标注上述任意类型的参数。

3.9 版后已移除: [collections.abc.ByteString] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

##### class typing.Collection(Sized, Iterable[T_co], Container[T_co])

[collections.abc.Collection] 的泛型版本。

3.6.0 新版功能.

3.9 版后已移除: [collections.abc.Collection] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

##### class typing.Container(Generic[T_co])

[collections.abc.Container] 的泛型版本。

3.9 版后已移除: [collections.abc.Container] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.ItemsView(MappingView, AbstractSet[tuple[KT_co, VT_co]])

[collections.abc.ItemsView] 的泛型版本。

3.9 版后已移除: [collections.abc.ItemsView] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.KeysView(MappingView, AbstractSet[KT_co])

[collections.abc.KeysView] 的泛型版本。

3.9 版后已移除: [collections.abc.KeysView] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.Mapping(Collection[KT], Generic[KT, VT_co])

[collections.abc.Mapping] 的泛型版本。用法如下：

```python
def get_position_in_index(word_list: Mapping[str, int], word: str) -> int:
    return word_list[word]
```

3.9 版后已移除: [collections.abc.Mapping] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.MappingView(Sized)

[collections.abc.MappingView] 的泛型版本。

3.9 版后已移除: [collections.abc.MappingView] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.MutableMapping(Mapping[KT, VT])

[collections.abc.MutableMapping] 的泛型版本。

3.9 版后已移除: [collections.abc.MutableMapping] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.MutableSequence(Sequence[T])

[collections.abc.MutableSequence] 的泛型版本。

3.9 版后已移除: [collections.abc.MutableSequence] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.MutableSet(AbstractSet[T])

[collections.abc.MutableSet] 的泛型版本。

3.9 版后已移除: [collections.abc.MutableSet] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.Sequence(Reversible[T_co], Collection[T_co])

[collections.abc.Sequence] 的泛型版本。

3.9 版后已移除: [collections.abc.Sequence] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.ValuesView(MappingView, Collection[_VT_co])

[collections.abc.ValuesView] 的泛型版本。

3.9 版后已移除: [collections.abc.ValuesView] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

#### collections.abc 对应的其他类型

##### class typing.Iterable(Generic[T_co])

[collections.abc.Iterable] 的泛型版本。

3.9 版后已移除: [collections.abc.Iterable] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.Iterator(Iterable[T_co])

[collections.abc.Iterator] 的泛型版本。

3.9 版后已移除: [collections.abc.Iterator] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.Generator(Iterator[T_co], Generic[T_co, T_contra, V_co])

生成器可以由泛型类型 `Generator[YieldType, SendType, ReturnType]` 注解。例如：

```python
def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'
```

注意，与 `typing` 模块里的其他泛型不同， [Generator] 的 `SendType` 属于逆变行为，不是协变行为，也是不变行为。

如果生成器只产生值，可将 `SendType` 与 `ReturnType` 设为 `None`：

```python
def infinite_stream(start: int) -> Generator[int, None, None]:
    while True:
        yield start
        start += 1
```

此外，还可以把生成器的返回类型注解为 `Iterable[YieldType]` 或 `Iterator[YieldType]`：

```python
def infinite_stream(start: int) -> Iterator[int]:
    while True:
        yield start
        start += 1
```

3.9 版后已移除: [collections.abc.Generator] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.Hashable

[collections.abc.Hashable] 的别名。

##### class typing.Reversible(Iterable[T_co])

[collections.abc.Reversible] 的泛型版本。

3.9 版后已移除: [collections.abc.Reversible] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.Sized

[collections.abc.Sized] 的别名。

#### 异步编程

##### class typing.Coroutine(Awaitable[V_co], Generic[T_co, T_contra, V_co])

[collections.abc.Coroutine] 的泛型版本。类型变量的差异和顺序与 Generator 的内容相对应，例如：

```python
from collections.abc import Coroutine

c: Coroutine[list[str], str, int]  # Some coroutine defined elsewhere
x = c.send('hi')                   # Inferred type of 'x' is list[str]

async def bar() -> None:
    y = await c                    # Inferred type of 'y' is int
```

3.5.3 新版功能.

3.9 版后已移除: [collections.abc.Coroutine] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.AsyncGenerator(AsyncIterator[T_co], Generic[T_co, T_contra])

异步生成器可由泛型类型 `AsyncGenerator[YieldType, SendType]` 注解。例如：

```python
async def echo_round() -> AsyncGenerator[int, float]:
    sent = yield 0
    while sent >= 0.0:
        rounded = await round(sent)
        sent = yield rounded
```

与常规生成器不同，异步生成器不能返回值，因此没有 `ReturnType` 类型参数。 与 [Generator] 类似，SendType 也属于逆变行为。

如果生成器只产生值，可将 `SendType` 设置为 `None`：

```python
async def infinite_stream(start: int) -> AsyncGenerator[int, None]:
    while True:
        yield start
        start = await increment(start)
```

此外，可用 `AsyncIterable[YieldType]` 或 `AsyncIterator[YieldType]` 注解生成器的返回类型：

```python
async def infinite_stream(start: int) -> AsyncIterator[int]:
    while True:
        yield start
        start = await increment(start)
```

3.6.1 新版功能.

3.9 版后已移除: [collections.abc.AsyncGenerator] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.AsyncIterable(Generic[T_co])

[collections.abc.AsyncIterable] 的泛型版本。

3.5.2 新版功能.

3.9 版后已移除: [collections.abc.AsyncIterable] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.AsyncIterator(AsyncIterable[T_co])

[collections.abc.AsyncIterator] 的泛型版本。

3.5.2 新版功能.

3.9 版后已移除: [collections.abc.AsyncIterator] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

##### class typing.Awaitable(Generic[T_co])

[collections.abc.Awaitable] 的泛型版本。

3.5.2 新版功能.

3.9 版后已移除: [collections.abc.Awaitable] now supports subscripting ([]).     See [PEP 585] and [GenericAlias 类型].

#### 上下文管理器类型

##### class typing.ContextManager(Generic[T_co])

[contextlib.AbstractContextManager] 的泛型版本。

3.5.4 新版功能.

3.6.0 新版功能.

3.9 版后已移除: [contextlib.AbstractContextManager] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

##### class typing.AsyncContextManager(Generic[T_co])

[contextlib.AbstractAsyncContextManager] 的泛型版本。

3.5.4 新版功能.

3.6.2 新版功能.

3.9 版后已移除: [contextlib.AbstractAsyncContextManager] now supports subscripting ([]). See [PEP 585] and [GenericAlias 类型].

### 协议

这些协议由 [runtime_checkable()] 装饰。

**class typing.SupportsAbs**

    含抽象方法 `__abs__` 的抽象基类，是其返回类型里的协变量。

**class typing.SupportsBytes**

    含抽象方法 `__bytes__` 的抽象基类。

**class typing.SupportsComplex**

    含抽象方法 `__complex__` 的抽象基类。

**class typing.SupportsFloat**

    含抽象方法 `__float__` 的抽象基类。

**class typing.SupportsIndex**

    含抽象方法 `__index__` 的抽象基类。

    3.8 新版功能.

**class typing.SupportsInt**

    含抽象方法 `__int__` 的抽象基类。

**class typing.SupportsRound**

    含抽象方法 `__round__` 的抽象基类，是其返回类型的协变量。

### 函数与装饰器

#### typing.cast(typ, val)

把值强制转换为类型。

不变更返回值。对类型检查器而言，代表了返回值具有指定的类型，但运行时故意不做任何检查（以便让检查速度尽量快）。

#### @typing.overload

`@overload` 装饰器可以修饰支持多个不同参数类型组合的函数或方法。`@overload` - 装饰定义的系列必须紧跟一个非 `@overload`-装饰定义（用于同一个函数/方法）。
`@overload`-装饰定义仅是为了协助类型检查器， 因为该装饰器会被非 `@overload`-装饰定义覆盖，后者用于运行时，而且会被类型检查器忽略。
在运行时直接调用 `@overload` 装饰的函数会触发 [NotImplementedError]。下面的重载示例给出了比联合类型或类型变量更精准的类型：

```python
@overload
def process(response: None) -> None:
    ...

@overload
def process(response: int) -> tuple[int, str]:
    ...

@overload
def process(response: bytes) -> str:
    ...

def process(response):
    <actual implementation>
```

See [PEP 484] for more details and comparison with other typing semantics.

#### @typing.final

告知类型检查器被装饰的方法不能被覆盖，且被装饰的类不能作为子类的装饰器，例如：

```python
class Base:
    @final
    def done(self) -> None:
        ...
class Sub(Base):
    def done(self) -> None:  # Error reported by type checker
        ...

@final
class Leaf:
    ...
class Other(Leaf):  # Error reported by type checker
    ...
```

这些属性没有运行时检查。详见 [PEP 591]。

3.8 新版功能.

#### @typing.no_type_check

标明注解不是类型提示的装饰器。

用作类或函数的 [decorator]。用于类时，递归地应用于该类中定义的所有方法，（但不影响超类或子类中定义的方法）。

本方法可直接修改函数。

#### @typing.no_type_check_decorator

让其他装饰器具有 [no_type_check()] 效果的装饰器。

本装饰器用 [no_type_check()] 里的装饰函数打包其他装饰器。
#### @typing.type_check_only

标记类或函数内不可用于运行时的装饰器。

在运行时，该装饰器本身不可用。实现返回的是私有类实例时，它主要是用于标记在类型存根文件中定义的类。

```python
@type_check_only
class Response:  # private or not available at runtime
    code: int
    def get_header(self, name: str) -> str: ...

def fetch_response() -> Response: ...
```

注意，建议不要返回私有类实例，最好将之设为公共类。

### 内省辅助器

#### typing.get_type_hints(obj, globalns=None, localns=None, include_extras=False)

返回函数、方法、模块、类对象的类型提示的字典。

一般情况下，与 `obj.__annotations__` 相同。此外，可通过在 `globals` 与 `locals` 命名空间里进行评估，以此来处理编码为字符串字面量的前向引用。如有需要，在默认值设置为 `None` 时，可为函数或方法注解添加 `Optional[t]`。对于类 `C`，则返回由所有 `__annotations__` 与 `C.__mro__` 逆序合并而成的字典。

本函数以递归地方式用 `T` 替换所有 `Annotated[T, ...]`， 除非将 `include_extras` 的值设置为 `True` （详见 [Annotated]）。例如：

```python
class Student(NamedTuple):
    name: Annotated[str, 'some marker']

get_type_hints(Student) == {'name': str}
get_type_hints(Student, include_extras=False) == {'name': str}
get_type_hints(Student, include_extras=True) == {
    'name': Annotated[str, 'some marker']
}
```

> **注解** [get_type_hints()] 在导入的 [类型别名] 中不工作，包括前向引用。启用注解的延迟评估（ [PEP 563] ）可能会消除对大多数前向引用的需要。

在 3.9 版更改: [PEP 593] 的组成部分，添加了 `include_extras` 参数。

#### typing.get_args(tp)
#### typing.get_origin(tp)

为泛型类型与特殊类型形式提供了基本的内省功能。

对于 `X[Y, Z, ...]` 形式的类型对象，这些函数返回 `X` 与 `(Y, Z, ...)`。如果 X 是内置对象或 [collections] `class` 的泛型别名， 会将其标准化为原始类。如果 `X` 是包含在其他泛型类型中的联合类型或 [Literal]，`(Y, Z, ...)` 的顺序会因类型缓存，而与原始参数 `[Y, Z, ...]` 的顺序不同。对于不支持的对象会相应地返回 `None` 或 `()`。例如：

```python
assert get_origin(Dict[str, int]) is dict
assert get_args(Dict[int, str]) == (int, str)

assert get_origin(Union[int, str]) is Union
assert get_args(Union[int, str]) == (int, str)
```

3.8 新版功能.

#### typing.is_typeddict(tp)

检查一个类型是否为 [TypedDict]。

例如：

```python
class Film(TypedDict):
    title: str
    year: int

is_typeddict(Film)  # => True
is_typeddict(list | str)  # => False
```

3.10 新版功能.

#### class typing.ForwardRef

用于字符串前向引用的内部类型表示的类。 例如，`List["SomeClass"]` 会被隐式转换为 `List[ForwardRef("SomeClass")]`。 这个类不应由用户来实例化，但可以由内省工具使用。

> **注解** [PEP 585] 泛型类型例如 `list["SomeClass"]` 将不会被隐式地转换为 `list[ForwardRef("SomeClass")]` 因而将不会自动解析为 `list[SomeClass]`。

3.7.4 新版功能.

### 常量

#### typing.TYPE_CHECKING

被第三方静态类型检查器假定为 `True` 的特殊常量。 在运行时为 `False`。 用法如下:

```python
if TYPE_CHECKING:
    import expensive_mod

def fun(arg: 'expensive_mod.SomeType') -> None:
    local_var: expensive_mod.AnotherType = other_fun()
```

第一个类型注解必须用引号标注，才能把它当作“前向引用”，从而在解释器运行时中隐藏 `expensive_mod` 引用。局部变量的类型注释不会被评估，因此，第二个注解不需要用引号引起来。

> **注解** 使用 `from __future__ import` 时，函数定义时不处理注解， 而是把注解当作字符串存在 `__annotations__` 里，这样就不必为注解使用引号。（详见 [PEP 563]）。

3.5.2 新版功能.

[标识符]: https://docs.python.org/zh-cn/3.10/reference/lexical_analysis.html#identifiers
[类型别名]: #_2
[类型变量]: #generic
[类方法]: https://docs.python.org/zh-cn/3.10/library/functions.html#classmethod
[联合类型表达式]: https://docs.python.org/zh-cn/3.10/library/stdtypes.html#types-union
[对象注解属性的最佳实践]: https://docs.python.org/zh-cn/3.10/howto/annotations.html#annotations-howto
[约束类型变量]: #class-typingtypevar
[__total__]: https://docs.python.org/zh-cn/3.10/library/typing.html#typing.TypedDict.__total__
[__required_keys__]: https://docs.python.org/zh-cn/3.10/library/typing.html#typing.TypedDict.__required_keys__
[__optional_keys__]: https://docs.python.org/zh-cn/3.10/library/typing.html#typing.TypedDict.__optional_keys__
[NewType]: #newtype
[Tuple]: #typingtuple
[collections]: https://docs.python.org/zh-cn/3.10/library/collections.html#module-collections
[frozenset]: https://docs.python.org/zh-cn/3.10/library/stdtypes.html#frozenset
[typing]: https://docs.python.org/zh-cn/3.10/library/typing.html#module-typing
[str]: https://docs.python.org/zh-cn/3.10/library/stdtypes.html#str
[dict]: https://docs.python.org/zh-cn/3.10/library/stdtypes.html#dict
[list]: https://docs.python.org/zh-cn/3.10/library/stdtypes.html#list
[builtins.list]: https://docs.python.org/zh-cn/3.10/library/stdtypes.html#list
[set]: https://docs.python.org/zh-cn/3.10/library/stdtypes.html#set
[builtins.set]: https://docs.python.org/zh-cn/3.10/library/stdtypes.html#set
[frozenset]: https://docs.python.org/zh-cn/3.10/library/stdtypes.html#frozenset
[builtins.frozenset]: https://docs.python.org/zh-cn/3.10/library/stdtypes.html#frozenset
[open()]: https://docs.python.org/zh-cn/3.10/library/functions.html#open
[TypedDict]: #class-typingtypeddictdict
[Literal]: #typingliteral
[runtime_checkable()]: #typingruntime_checkable
[NotImplementedError]: https://docs.python.org/zh-cn/3.10/library/exceptions.html#NotImplementedError
[Any]: #typingany
[Union]: #typingunion
[Sequence]: #class-typingsequence
[AbstractSet]: #class-typingabstractset
[Mapping]: #class-typingmapping
[Callable]: #typingcallable
[TypeVar]: #typingtypevar
[Generic]: #class-typinggeneric
[ParamSpec]: #typingparamspec
[Concatenate]: #typingconcatenate
[ParamSpecArgs]: #typingparamspecargs
[ParamSpecKwargs]: #typingspeckwargs
[hashable]: https://docs.python.org/zh-cn/3.10/glossary.html#term-hashable
[TypeError]: https://docs.python.org/zh-cn/3.10/library/exceptions.html#TypeError
[builtins.type]: https://docs.python.org/zh-cn/3.10/library/functions.html#type
[threading.Lock]: https://docs.python.org/zh-cn/3.10/library/threading.html#threading.Lock
[GenericAlias 类型]: https://docs.python.org/zh-cn/3.10/library/stdtypes.html#types-genericalias
[collections.abc.Callable]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Callable
[Iterable]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Iterable
[object]: https://docs.python.org/zh-cn/3.10/library/functions.html#object
[__class_getitem__()]: https://docs.python.org/zh-cn/3.10/reference/datamodel.html#object.__class_getitem__
[cast()]: #typingcast
[no_type_check()]: #typingno_type_check
[Generator]: #class-typinggeneratoriteratort_co-generict_co-t_contra-v_co
[decorator]: https://docs.python.org/zh-cn/3.10/glossary.html#term-decorator
[get_type_hints()]: https://docs.python.org/zh-cn/3.10/library/typing.html#typing.get_type_hints
[ssl.SSLObject]: https://docs.python.org/zh-cn/3.10/library/ssl.html#ssl.SSLObject
[namedtuple()]: https://docs.python.org/zh-cn/3.10/library/collections.html#collections.namedtuple
[collections.namedtuple()]: https://docs.python.org/zh-cn/3.10/library/collections.html#collections.namedtuple
[bytes]: https://docs.python.org/zh-cn/3.10/library/stdtypes.html#bytes
[bytearray]: https://docs.python.org/zh-cn/3.10/library/stdtypes.html#bytearray
[memoryview]: https://docs.python.org/zh-cn/3.10/library/stdtypes.html#memoryview
[collections.defaultdict]: https://docs.python.org/zh-cn/3.10/library/collections.html#collections.defaultdict
[collections.OrderedDict]: https://docs.python.org/zh-cn/3.10/library/collections.html#collections.OrderedDict
[collections.ChainMap]: https://docs.python.org/zh-cn/3.10/library/collections.html#collections.ChainMap
[collections.Counter]: https://docs.python.org/zh-cn/3.10/library/collections.html#collections.Counter
[collections.deque]: https://docs.python.org/zh-cn/3.10/library/collections.html#collections.deque
[collections.abc]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#module-collections.abc
[collections.abc.Set]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Set
[collections.abc.ByteString]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.ByteString
[collections.abc.Collection]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Collection
[collections.abc.Container]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Container
[collections.abc.ItemsView]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.ItemsView
[collections.abc.KeysView]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.KeysView
[collections.abc.MappingView]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.MappingView
[collections.abc.Mapping]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Mapping
[collections.abc.MutableMapping]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.MutableMapping
[collections.abc.MutableSequence]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.MutableSequence
[collections.abc.MutableSet]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.MutableSet
[collections.abc.Sequence]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Sequence
[collections.abc.ValuesView]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.ValuesView
[collections.abc.Iterable]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Iterable
[collections.abc.Iterator]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Iterator
[collections.abc.Generator]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Generator
[collections.abc.Hashable]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Hashable
[collections.abc.Reversible]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Reversible
[collections.abc.Coroutine]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Coroutine
[collections.abc.Sized]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Sized
[collections.abc.AsyncIterable]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.AsyncGenerator
[collections.abc.AsyncIterator]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.AsyncIterator
[collections.abc.Awaitable]: https://docs.python.org/zh-cn/3.10/library/collections.abc.html#collections.abc.Awaitable
[contextlib.AbstractContextManager]: https://docs.python.org/zh-cn/3.10/library/contextlib.html#contextlib.AbstractContextManager
[contextlib.AbstractAsyncContextManager]: https://docs.python.org/zh-cn/3.10/library/contextlib.html#contextlib.AbstractAsyncContextManager
[PEP 483]: https://www.python.org/dev/peps/pep-0483
[PEP 484]: https://www.python.org/dev/peps/pep-0484
[PEP 544]: https://www.python.org/dev/peps/pep-0544
[PEP 526]: https://www.python.org/dev/peps/pep-0526
[PEP 563]: https://www.python.org/dev/peps/pep-0563
[PEP 585]: https://www.python.org/dev/peps/pep-0585
[PEP 589]: https://www.python.org/dev/peps/pep-0589
[PEP 591]: https://www.python.org/dev/peps/pep-0591
[PEP 593]: https://www.python.org/dev/peps/pep-0593
[PEP 612]: https://www.python.org/dev/peps/pep-0612
[PEP 613]: https://www.python.org/dev/peps/pep-0613
[PEP 647]: https://www.python.org/dev/peps/pep-0647
