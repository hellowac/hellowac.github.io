# 常用的函数

## 为何要用sys.exit()退出？

原文: [为何要用sys.exit()退出？](https://www.pynote.net/archives/1036)

Python有4个不同的退出程序的函数，`exit()`，`quit()`，`os._exit()`和本文要介绍的`sys.exit()`。

`exit()`和`quit()`是一样的，它俩的功能基本上与`sys.exit()`一样，只有`os._exit()`有些简单粗暴。

**exit和quit函数**

这两个函数的作用，就是直接退出程序，可以带一个参数作为程序的返回码，如果不带参数，默认就是返回0.

```python
xinlin@ubuntu:~/test$ python3 -q
>>> exit(111)
xinlin@ubuntu:~/test$ echo $?
111
xinlin@ubuntu:~/test$ python3 -q
>>> quit(222)
xinlin@ubuntu:~/test$ echo $?
222
xinlin@ubuntu:~/test$ python3 -q
>>> exit()
xinlin@ubuntu:~/test$ echo $?
0
xinlin@ubuntu:~/test$ python3 -q
>>> quit()
xinlin@ubuntu:~/test$ echo $?
0
```

这两个函数一般在交互式的python解释器中使用。其实它俩也会抛出`SystemExit异常`，因此说跟`sys.exit()`一样。

**sys.exit()函数**

`sys模块`的`exit`函数，通过抛出一个`SystemExit异常`来尝试结束程序，Python代码可以捕获这个异常来进行一些程序退出前的清理工作，也可以不退出程序。

`sys.exit`函数同样可以带一个参数来作为程序的退出码，默认是`0`.

```python
>>> import sys
>>> try:
...     sys.exit(101)
... except SystemExit as e:
...     print(repr(e))
...     print(str(e))
...
SystemExit(101)
101
>>>
```

看起来使用`str()`函数在`except`分支获取返回码，比较判断不同的返回码，并做响应的清理动作，是比较方便的。另外一个细节，上面这段代码在Python解释器中执行，因为异常被捕获，所以不会导致解释器退出！

捕获了`sys.exit()`函数抛出的异常，处理之后，还要程序继续退出，就需要直接使用`exit`或`quit`函数。实践中，完整的使用`sys.exit`函数的逻辑应该是如下这样的代码：

```python
import sys

def main():
    sys.exit(123)
    return

if __name__ == '__main__':
    try:
        main()
    except SystemExit as e:
        if str(e) == '123':
            print('---123---')
            exit(123)
```

一般在`python`脚本中都选择使用`sys.exit`函数退出程序，可以有个异常捕获机制来做清理扫尾的工作，程序会更加灵活健壮。

**os._exit()函数**

这个函数简单粗暴，就是直接退出python解释器，后面的代码都不执行了！一般程序不推荐使用这种退出方式。

补充一个细节：

**在python线程中，使用`sys.exit`（包括`exit`和`quit`），都只能实现退出子线程，而不能退出主线程；**

**如果在子线程中调用`os._exit`，可以实现整个程序的退出。**

## 驼峰命名法和骆驼命名法互转

原文: <https://blog.csdn.net/mouday/article/details/90079956>

```python
# -*- coding: utf-8 -*-


def get_lower_case_name(text):
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)

    return "".join(lst).lower()


if __name__ == '__main__':
    print(get_lower_case_name("StudentNameModel"))

# student_name_model
```

另一种实现方式:

```python
# -*- coding: utf-8 -*-
import re


def pascal_case_to_snake_case(camel_case: str):
    """大驼峰（帕斯卡）转蛇形"""
    snake_case = re.sub(r"(?P<key>[A-Z])", r"_\g<key>", camel_case)
    return snake_case.lower().strip('_')


def snake_case_to_pascal_case(snake_case: str):
    """蛇形转大驼峰（帕斯卡）"""
    words = snake_case.split('_')
    return ''.join(word.title() for word in words)

```

## 利息以及复利计算

```python
from typing import Dict, NoReturn
from enum import Enum


class UnitType(Enum):
    BY_DAY = "day"
    BY_YEAR = "year"


class Income(object):
    def __init__(
        self,
        principal: int,
        apr: float,
        *,
        cycle: int = 0,
        replace_unit: int = 1,
        echo: bool = True,
        by: UnitType = UnitType.BY_DAY,
    ) -> None:
        """计算收益的类

        principal: 本金； 例如: 10000, 单位 元
        apr: 利率,收益率, 一个持有周期的利率；例如: 0.0051
        cycle: 持有周期，例如: 2 代表2个周期，并且复利计算
        replace_unit: 一个周期代表的天/年数， 具体根据by的类型确定，例如: 60
        by: 周期替换时的单位, 例如: days 代表xxx天
        echo: 代表是否打印详细, 例如: true 代表打印
        """
        self.principal = principal
        self.apr = apr
        self.cycle = cycle
        self.replace_unit = replace_unit
        self.echo = echo
        self.by = by
        self.income_type = "按天" if self.by == UnitType.BY_DAY else "按年"
        self.income_type_unit = "天" if self.by == UnitType.BY_DAY else "年"

        # 累计收益
        self.income_total: float = 0  # 累计利息
        self.income_dict: Dict[str, float] = {}  # 各个周期利息
        self.income_rate: float = 0  # 累计收益率, 百分比
        self.income_rate_dict: Dict[str, float] = {}  # 各个周期收益率, 百分比

    def get_income(self, principal: int) -> float:
        """计算单周期的利息

        principal: 本金； 例如: 10000, 单位 元
        """

        return principal * (self.apr / 100)

    def cycle_income(self) -> None:
        """计算复利"""

        # 初始本金
        congest_capital = self.principal
        # 上一次本金
        prev_captial = self.principal
        # 上一次累计收益率
        prev_income_rate = 0
        # 初始利息
        income_total = 0
        # 累计收益率
        income_rate = 0

        for i in range(1, cycle + 1):

            income = self.get_income(congest_capital)
            income = round(income, 2)
            income_total += income  # 累计利息
            # 上一次累计收益率
            prev_income_rate = income_rate
            # 本次累计收益率, 用本金计算累计的收益率
            income_rate = round((income_total / self.principal) * 100, 2)

            self.income_dict[str(i)] = income
            self.income_rate_dict[str(i)] = income_rate

            # 上次本金
            prev_captial = congest_capital

            # 累计本金
            congest_capital += income
            congest_capital = round(congest_capital, 2)

            # 累计收益率差额, 减去初始的收益率
            diff_income_rate = round(income_rate - prev_income_rate - self.apr, 2)

            if self.echo:
                msgs = [
                    f"初始本金: {self.principal}",
                    f"复利: 第{i}次",
                    f"计算本金: {prev_captial}",
                    f"本次利息: {income}",
                    f"累计本息: {congest_capital}",
                    f"总收益率: {income_rate}%",
                    f"收益率增长额: {diff_income_rate}%;",
                ]
                print(" - ".join(msgs))

        # 百分比,  用本金计算累计的收益率
        self.income_total = round(income_total, 2)
        self.income_rate = income_rate

    def calculate_income(self):
        """计算收益"""
        append_years = None

        if self.by == UnitType.BY_DAY:
            append_years = round((self.replace_unit * self.cycle) / 365, 2)

        msgs = []
        msgs.append(f"本金: {self.principal}元")
        # msgs.append(f"计息方式: {self.income_type}")
        msgs.append(f"按{self.replace_unit}{self.income_type_unit}为一个周期计息")
        msgs.append(f"共计息:{self.cycle}个周期")
        msgs.append(f"共占用资金: {self.replace_unit * self.cycle}{self.income_type_unit}")
        msgs.append(f"约占用资金: {append_years}年") if self.by == UnitType.BY_DAY else None
        msgs.append(f"周期利率: {self.apr}%")

        if self.echo:
            msgs.append(f"详细如下: ")

        print(f'利益演示摘要: {", ".join(msgs)}')

        self.cycle_income()

        print("-" * 100)
        msgs.clear()

        msgs.append(f"本金: {self.principal}元")
        msgs.append(f"共获利息: {self.income_total}元")
        msgs.append(f"本息合计: {self.income_total + self.principal}元")
        msgs.append(f"收益率: {self.income_rate}%")
        msgs.append(f"占用资金: {self.replace_unit * self.cycle}{self.income_type_unit}")
        msgs.append(f"约占用资金: {append_years}年") if self.by == UnitType.BY_DAY else None

        print(" - ".join(msgs))


def get_income(principal: int, apr: float, days: int) -> float:
    """计算按年利率持有指定天数所获得的利息

        principal:  本金
        apr: 年利率
        days: 持有天数

    返回: float 类型的利息值
    """
    # 计算利息

    return principal * apr * (days / 365)


def cycle_income(capital: int, apr: float, days: int, cycle: int):
    """计算按年率持有指定天数并且复利N次所获得的利息收入。

    principal:  本金
    apr: 年利率
    days: 持有天数
    cycle: 复利几次
    """

    print(f"{capital} 按年利率 {apr} 持有天数{days} 复利 {cycle} 次, 计算如下:")

    # 累计本金
    congest_capital = capital
    income_total = 0

    for i in range(1, cycle + 1):

        income = get_income(congest_capital, apr, days)
        income = round(income, 2)
        income_total += income

        congest_capital += income
        congest_capital = round(congest_capital, 2)

        msgs = [
            f"本金: {capital}",
            f"复利次数: 第{i}次",
            f"本次获得利息: {income}",
            f"积累本息共计: {congest_capital};",
        ]
        print(" - ".join(msgs))

    return_rate = round((income_total / capital) * 100, 2)
    print(
        f"{capital} 元，一共占用资金: {days * cycle} 天, 共获利: {income_total}元, 收益率: {return_rate}%"
    )


if __name__ == "__main__":
    principal = 1000 * 100  # 本金
    echo = True

    # 按周期利率计算
    by = UnitType.BY_DAY
    replace_unit = 60
    apr = 0.51  # 周期利率, 0.51%
    cycle = 6 * 30  # 60天一个周期, 一年6个周期， 30年持有期
    # cycle = 6 * 10  # 60天一个周期, 一年6个周期， 10年持有期
    # cycle = 6 * 10  # 60天一个周期, 一年6个周期， 5年持有期

    # 按年利率计算
    by = UnitType.BY_YEAR
    replace_unit = 1
    apr = 3  # 年利率, 3%
    cycle = 5  # 30年持有期

    income = Income(
        principal=principal,
        apr=apr,
        cycle=cycle,
        replace_unit=replace_unit,
        echo=echo,
        by=by,
    )
    income.calculate_income()
```

最后输出如下:

```text
利益演示摘要: 本金: 100000元, 按1年为一个周期计息, 共计息:5个周期, 共占用资金: 5年, 周期利率: 3%, 详细如下: 
初始本金: 100000 - 复利: 第1次 - 计算本金: 100000 - 本次利息: 3000.0 - 累计本息: 103000.0 - 总收益率: 3.0% - 收益率增长额: 0.0%;
初始本金: 100000 - 复利: 第2次 - 计算本金: 103000.0 - 本次利息: 3090.0 - 累计本息: 106090.0 - 总收益率: 6.09% - 收益率增长额: 0.09%;
初始本金: 100000 - 复利: 第3次 - 计算本金: 106090.0 - 本次利息: 3182.7 - 累计本息: 109272.7 - 总收益率: 9.27% - 收益率增长额: 0.18%;
初始本金: 100000 - 复利: 第4次 - 计算本金: 109272.7 - 本次利息: 3278.18 - 累计本息: 112550.88 - 总收益率: 12.55% - 收益率增长额: 0.28%;
初始本金: 100000 - 复利: 第5次 - 计算本金: 112550.88 - 本次利息: 3376.53 - 累计本息: 115927.41 - 总收益率: 15.93% - 收益率增长额: 0.38%;
----------------------------------------------------------------------------------------------------
本金: 100000元 - 共获利息: 15927.41元 - 本息合计: 115927.41元 - 收益率: 15.93% - 占用资金: 5年
```
