# 收益函数

## 利息以及复利计算

```python
def get_income(principal: int, apr: float, days: int) -> float:
    """ 计算按年利率持有指定天数所获得的利息

        principal:  本金
        apr: 年利率
        days: 持有天数
    
    返回: float 类型的利息值
    """
    # 计算利息

    return principal * apr * (days/365)


def cycle_income(capital: int, apr: float, days: int, cycle:int):
    """ 计算按年率持有指定天数并且复利N次所获得的利息收入。

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

        print(f"{capital} 第{i}次 共获得利息: {income}, 本息共计: {congest_capital};")
    
    return_rate = round((income_total / capital) * 100, 2)
    print(f"{capital} 元，一共占用资金: {days * cycle} 天, 共获利: {income_total}元, 收益率: {return_rate}%")



if __name__ == "__main__":
    capital = 55000  # 本金
    rate = 0.0205     # 年利率
    days = 15        # 持有天数
    cycle = 4        # 复利四次

    cycle_income(capital, rate, days, cycle)

    print("--" * 10)
```

最后输出如下:

```text
55000 按年利率 0.0205 持有天数15 复利 4 次, 计算如下:
55000 第1次 共获得利息: 46.34, 本息共计: 55046.34;
55000 第2次 共获得利息: 46.37, 本息共计: 55092.71;
55000 第3次 共获得利息: 46.41, 本息共计: 55139.12;
55000 第4次 共获得利息: 46.45, 本息共计: 55185.57;
55000 元，一共占用资金: 60 天, 共获利: 185.57元, 收益率: 0.34%
```
