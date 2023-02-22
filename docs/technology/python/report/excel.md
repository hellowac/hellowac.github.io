# Excel

Python读写Excel格式的数据参考：<https://www.python-excel.org/>

以及 github 组织: [python-excel](https://github.com/python-excel)

## 在 Python 中处理 Excel 文件

[openpyxl]: https://openpyxl.readthedocs.org/
[xlsxwriter]: https://xlsxwriter.readthedocs.org/
[pyxlsb]: https://github.com/willtrnr/pyxlsb
[pylightxl]: https://pylightxl.readthedocs.io/en/latest/
[xlrd]: https://xlrd.readthedocs.io/en/latest/
[xlwt]: https://xlwt.readthedocs.io/en/latest/
[xlutils]: https://xlutils.readthedocs.io/en/latest/
[xlwings]: https://www.xlwings.org/

- [openpyxl]: 用于读写 Excel 2010 文件的推荐包
- [xlsxwriter]: 用于写入数据, 格式化信息，特别是 Excel 2010 格式（即：.xlsx）的图表的替代包
- [pyxlsb]: 读取xlsb格式的 Excel 文件.
- [pylightxl]: 读取 xlsx 和 xlsm 格式的文件，以及写入 xlsx 格式文件。
- [xlrd]: 从旧 Excel 文件（即：.xls）中读取数据和格式信息
- [xlwt]: 将数据和格式信息写入旧版 Excel 文件（即：.xls）
- [xlutils]: 收集了需要xlrd和的实用程序xlwt，包括复制和修改或过滤现有 Excel 文件的能力。
- [xlwings]: xlwings 是一个BSD 许可的Python 库，可以轻松地从 Excel 调用 Python，反之亦然:
  - **脚本**：使用接近 VBA 的语法从 Python 自动/与 Excel 交互。
  - **宏**：用干净而强大的 Python 代码替换你凌乱的 VBA 宏。
  - **UDF**：在 Python 中编写用户定义函数 (UDF)（仅限 Windows）。

## 常见问题

1. 转换Excel的float类型的时间

    参考：<https://stackoverflow.com/questions/32430679/how-to-read-dates-using-xlrd>

    ```python
    import datetime
    import xlrd

    book = xlrd.open_workbook("myexcelfile.xls")
    sh = book.sheet_by_index(0)
    a1 = sh.cell_value(rowx=0, colx=0)
    a1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(a1, book.datemode))
    
    print 'datetime: %s' % a1_as_datetime
    ```
