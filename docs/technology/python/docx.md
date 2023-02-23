# docx文档

[docx_doc]: https://hellowac.github.io/docx_doc/
[pyton-docx]: https://python-docx.readthedocs.io/en/latest/

参考 [docx_doc]{target="_blank"} 的文档.

官网: [pyton-docx]{target="_blank"}

* 参考原文: <https://python-docx.readthedocs.io/en/latest/index.html>{target="_blank"} - 官网
* 参考翻译: <https://www.zybuluo.com/belia/note/1303813>{target="_blank"} - 参考1
* 参考翻译2: <https://www.osgeo.cn/python-docx/index.html>{target="_blank"} - 参考2

openxml参考: <https://zhuanlan.zhihu.com/p/353332428>{target="_blank"}

<!--more-->

设置中文字体参考:

* [python-docx中设置中文字体](http://www.jhanmath.com/?p=130){target="_blank"} - 个人博客
* [python-docx设置中文字体](http://baijiahao.baidu.com/s?id=1663508248875988550){target="_blank"} - 百度文章

【小梁学编程】:

* [Python-docx添加段落](https://baijiahao.baidu.com/s?id=1663222381110715081){target="_blank"}
* [python-docx段落设置](https://baijiahao.baidu.com/s?id=1663325988716544457)
* [python-docx设置中文字体](https://baijiahao.baidu.com/s?id=1663508248875988550)
* [python-docx字体设置](https://baijiahao.baidu.com/s?id=1663765175326104525)
* [python-docx表格（一）：添加表格](https://baijiahao.baidu.com/s?id=1664116924629415335)
* [python-docx添加和删除表格行、列](https://baijiahao.baidu.com/s?id=1664194316556491797)
* [python-docx表格添加和删除数据](https://baijiahao.baidu.com/s?id=1664296985354372040)
* [python-docx设置表格对齐方式](https://baijiahao.baidu.com/s?id=1664476132973597291)
* [python-docx图像的添加与删除](https://baijiahao.baidu.com/s?id=1664569240606934226)
* [python-docx设置图片大小和对齐方式](https://baijiahao.baidu.com/s?id=1664759569158414865)
* [python-docx节的添加、定位和分节符的设置](https://baijiahao.baidu.com/s?id=1664860838370171501)
* [python-docx页面设置](https://baijiahao.baidu.com/s?id=1664903484937508104)
* [python-docx指定页面设置成横向](https://baijiahao.baidu.com/s?id=1665028380582245274)
* [python-docx设置页眉和页脚](https://baijiahao.baidu.com/s?id=1665454009794833226)

## 说明

python-docx是一个用于创建和更新Microsoft Word（.docx）文件的Python库。

## 他能做什么

```python
from docx import Document
from docx.shared import Inches

document = Document()

document.add_heading('Document Title', 0)

p = document.add_paragraph('A plain paragraph having some ')
p.add_run('bold').bold = True
p.add_run(' and some ')
p.add_run('italic.').italic = True

document.add_heading('Heading, level 1', level=1)
document.add_paragraph('Intense quote', style='Intense Quote')

document.add_paragraph(
    'first item in unordered list', style='List Bullet'
)
document.add_paragraph(
    'first item in ordered list', style='List Number'
)

document.add_picture('monty-truth.png', width=Inches(1.25))

records = (
    (3, '101', 'Spam'),
    (7, '422', 'Eggs'),
    (4, '631', 'Spam, spam, eggs, and spam')
)

table = document.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Qty'
hdr_cells[1].text = 'Id'
hdr_cells[2].text = 'Desc'
for qty, id, desc in records:
    row_cells = table.add_row().cells
    row_cells[0].text = str(qty)
    row_cells[1].text = id
    row_cells[2].text = desc

document.add_page_break()

document.save('demo.docx')
```

![example](./imgs/2021-12-09-python-docx-example.png)

## 用户指南

### 安装

> **注意**：python-docx版本0.3.0及更高版本与先前版本API不兼容。

python-docx 托管在PyPI上，因此安装相对简单，只取决于您安装的应用程序。

1. 如果在pip工具可用的情况下你可以直接安装python-docx,如果还没有安装 可以自行搜索怎样安装。其在代码如下：
  `pip install python-docx`
2. 当然你也可以用easy_install来安装python-docx，但是方法不如上面一 种好。其安装代码如下：
  `easy_install python-docx`
3. 然而，如果你的pip和你的easy_install都不可用的时候，那么此时你可以手动的通过PyPI下载,然后解压包、运行setup.py.

  ```shell
  tar xvzf python-docx-{version}.tar.gz
  cd python-docx-{version}
  python setup.py install
  ```

#### 环境支持

python2.6、2.7，or 3.4
lxml >= 2.3.2

### 快速开始

使用python-docx是非常容易的，让我们一点一点学习这些！

#### 打开一个文档

首先，如果你需要操作一篇文档，下面是最容易的方法：

```python
from docx import Document
document = Document()
```

这是基于默认模板打开一个空白文档，这几乎是你从word打开一个新文档的内置默认值。你也可以打开并基于一个现有的文档来使用python-docx，但是我们现在想保持这么简单的做法。

#### 添加一个段落

段落是word结构的基础，他们用于正文，也标题和列表项目。这是添加一个段落的示例方法：

```python
paragraph = document.add_paragraph('Lorem ipsum dolor sit amet.')
```

这个方法返回对一个段落的引用，在文章的结尾加上一个新段落。这种情况下，这个新段落引用将会被分配给`paragraph`，但是，除非我需要这个引用，否则我会忽视掉它，在你的代码中通常不会要做任何事情在你添加了一个新段落之后。因此，保持对它的引用没有多大意义。

它还可以当作一个“光标”，用来插入一个新段落。

```python
prior_paragraph = paragraph.insert_paragraph_before('Lorem ipsum')
```

这就使得我们可以在文档中间插入文档，这对于我们修改一篇而不是从零开始创建一篇文档来说重要的多。

#### 添加一个标题

在一些除了一些很短的文章中，正文一般分为几部分，每部分都是一个从一个标题开始，下面是如何添加一个标题的示例：

```python
document.add_heading('The REAL meaning of the universe')
```

在默认情况，此代码是添加一个最高级别的标题，在word中通常显示为“标题1”，当你想要添加一个子节标题时，你可以将你需要的级别指定为一个0-9之间的整数。就像这样：

```python
document.add_heading('The role of dolphins', level=2)
```

如果你指定的级别为0，则会添加一个标题段落，这可以很方便的开始一个没有单独标题的相对较短的文章。

#### 添加一个分页符

每隔一段时间你就想要接下来的内容放到下一页面上，即使这个页面还没有满，而一个强制分页则可以完成这些操作：

```python
document.add_page_break()
```

#### 添加一个表

一个人经常会遇到一些内容，它们与表格类似，整齐的排列在一行或者一列中。Word在这个方面做的很好，下面是如何添加一个表格的示例：

```python
table = document.add_table(rows=2, cols=2)
```

表格有几种方法和属性，您可以通过他们来填充表格。通过访问一个单元格来学习是一个很好的开始，作为基础，你可以通过列或者行的一些信息来访问他们：

```python
cell = table.cell(0, 1)
```

这是我们刚刚创建的的单元格中最右边的单元格，注意他的行列起始值是0，就像通过List访问。
如果你选中了一个单元格，你可以把一些文字放入里面：

```python
cell.text = 'parrot, possibly dead'
```

通常，一次访问一个表会更加容易，例如当从一个数据源填充一个可变长度的表格时，在每一个含有.cells属性的表格中我们均可以通过.rows属性来访问每一行。这个.cells可同时支持Row和Colum的索引访问，就像一个List:

```python
row = table.rows[1]
row.cells[0].text = 'Foo bar to you.'
row.cells[1].text = 'And a hearty foo bar to you too sir!
```

在表格中.rows和.columns集合是可迭代的，你可以直接在for循环里面使用它们，与此相同的，.cells上行或列成序列：

```python
for row in table.rows:
    for cell in row.cells:
        print(cell.text)
```

如果你想要得到行或列的的数目，那么你可以使用len():

```python
row_count = len(table.rows)
col_count = len(table.columns)
```

你也可以以递增方式向表中添加行：

```python
row = table.add_row()
```

这对于我们上面提到的可变长度表来说是十分方便的：

```python

# 获取表格数据
items = (
    (7, '1024', 'Plush kittens'),
    (3, '2042', 'Furbees'),
    (1, '1288', 'French Poodle Collars, Deluxe'),
)

# 添加表格
table = document.add_table(1, 3)

# 添加表头
heading_cells = table.rows[0].cells
heading_cells[0].text = 'Qty'
heading_cells[1].text = 'SKU'
heading_cells[2].text = 'Description'

# 给每项添加行数据
for item in items:
    cells = table.add_row().cells
    cells[0].text = str(item.qty)
    cells[1].text = item.sku
    cells[2].text = item.desc
```

同样对添加列来说也是一样的。
Word具有一组预先已经格式化好的表格样式，你可以从它的表格样式库中选择，你可以将其中一个应用于表格，如下所示：

```python
table.style = 'LightShading-Accent1'
```

从表样式名称中删除所有空格可以形成样式名称，你可以通过将鼠标悬停在Word的表样式库中的缩略图上，可以找到表样式名称。

#### 添加图片

在Word中，你可以通过【插入】--> 【图像】--> 【来自文件】菜单来添加图片，而在这里，你则可以这么添加：

```python
document.add_picture('image-filename.png')
```

此例子使用了从本地加载图片路径，你也可以使用一个类文件对象，本质上就像打开任何一个文件对象。如果你从网络或者数据库而不想从本地获取数据，这会很方便。

##### 照片大小

默认情况下，添加的的图片大小等于您本地图片大小，但这通常会比您想象的更大。本地图片大小的计算方法是像素/dpi(每英寸像素点数)，因此，一个300dpi的300x300像素的图片通常大小是1英寸，但是问题是现在大多数图片的默认72dpi,这实际上使得同样的图片在这样的情况下会在一半的页面上一边显示大小为4.167英寸。
在这里，要获得你想要的图像大小，你可以指定其高度和宽度，如inches或cm:

```python
from docx.shared import Inches
document.add_picture('image-filename.png', width=Inches(1.0))
```

你可以自由的指定高度和宽度，但是你通常情况下不想要这样。如果你指想要其中要给参数，python-docx通常可以帮你计算出另外一个参数，这样可以保持你照片的长宽比，使他看上去不是被拉伸的。
你可以使用英寸或者厘米这两个方便的单位来指定你的测量单位。在`python-docx`内部，我们默认使用英国公制单位，914400英寸（这里没查到，只查到914400um=1码），因此你如果忘记了而只是指定了宽度为2的话你就得到一个很小的图像。此时你需要导入`docx.shared`子包，你可以就像一个整数一样的在算术中使用它们，当然，他们事实上也是，因此，像一个表达式`width = Inches(3) /thing_count`就被利用的很好。

#### 应用段落格式

如果你不知道Word的段落格式，你应该检查下它。基本上，它允许你能一次性应用一整套样式，如果你了解CSS的话，它和CSS非常类似。
你可以在创建段落时应用段落样式：

```python
document.add_paragraph('Lorem ipsum dolor sit amet.', style='ListBullet')
```

这种特殊的样式会使得段落以一个符号的样式出现，一个非常方便的东西。之后你依然还可以应用样式，这下面的两行相当于上面的一行：

```python
paragraph = document.add_paragraph('Lorem ipsum dolor sit amet.')
paragraph.style = 'List Bullet'
```

这个样式被指定用他的样式名，如上所示的List Bullet。通常，样式名出现在Word的用户界面中，但是，请注意，如果您使用的是本地化版本的Word，则样式ID可能来自英语样式名称，并且可能不会完全对应于其在Word UI中的样式名称。

#### 应用粗体以及斜体

为了能够理解黑体和斜体是怎么回事，你需要理解一点段落内部的事情，简短来说就是这样：

1. 一个段落包含所有块级格式，例如缩进、行高、Tab等等。
2. 字符级别的格式，例如黑体和斜体，都是被应用于run级别的。所有段落里面的内容都必须在一个run里面但是也不仅仅一个更新。因此一个含有粗体的段落可能会需要三个run，一个是普通的，一个是包括了粗体的，以及后面另外一个普通的。

当你利用`.add_paragraph()`方法向一个段落中添加一段文字的时候，它被放入一个单独的run中，你可以使用.add_run()在段落中添加更多的内容:

```python
paragraph = document.add_paragraph('Lorem ipsum ')
paragraph.add_run('dolor sit amet.')
```

这样产生一个像一个单独字符串产生的段落。除非你看xml，否则你不会看不来这些内容是分开的。注意第一个字符串末尾的尾随空格，你需要明确说明空格在开头和结尾之间出现的位置，他们不会自动的在runs之间插入。你总能遇到你几次这个问题。

`Run`这个对象有`.bold`和`.italic`两个属性值供你去设置：

```python
paragraph = document.add_paragraph('Lorem ipsum ')
run = paragraph.add_run('dolor')
run.bold = True
paragraph.add_run(' sit amet.')
```

上述例子的结果像这样： `‘Lorem ipsum dolor sit amet.’`
如果你不需要其它的设置你也可以直接对`.add_run()`的`.bold`和`italic`值结果设置为`True`：

```python
paragraph.add_run('dolor').bold = True

# 它同时也等于
run = paragraph.add_run('dolor')
run.bold = True

# 你不需要'run'之后再次设置引用
```

利用`.add_paragraph`构建内容不是必须的，如果你是从`runs`中构建内容的话这会使你的代码变得更加简单：

```python
paragraph = document.add_paragraph()
paragraph.add_run('Lorem ipsum ')
paragraph.add_run('dolor').bold = True
paragraph.add_run(' sit amet.')
```

#### 应用字符格式

除了指定一组段落级别的段落样式外，Word还可以指定一组run级别的字符样式，通常你可以认为这些字符样式包括字符、字体、字号、颜色、粗体、斜体等等。
和段落样式一样，字符样式必须定义在你已经用Document()打开的文档中。（见理解样式）。
字符样式可以在添加一个run中定义:

```python
paragraph = document.add_paragraph('Normal text, ')
paragraph.add_run('text with emphasis.', 'Emphasis')
```

你也可以在字符已经创建好了之后再去应用样式，这段代码与撒谎上面的代码效果相同：

```python
paragraph = document.add_paragraph('Normal text, ')
run = paragraph.add_run('text with emphasis.')
run.style = 'Emphasis'
```

如同段落样式一样，这些样式名称可以再Word界面内看见。

### 处理文件

python-docx允许你创建一个新文件或者在一个已经存在的文件上做些修改。事实上，它只允许你从一个已经存在的文档上进行修改。如果你需要从一篇没有任何内容的文档开始，你会感觉从头开始一篇文档一样。

这个特点是强大的。决定许多文档看上去怎么样子的部分是你删除所有内容后留下的。这些样式如页眉、也叫是与你的主要内容无关的，因此，你可以从文档的开头就放置这些个性化的内容而之后他们会在文档中出现。

让我们逐步的创建一个文档示例，并开始做两件事：打开并保存它。

#### 打开一个文档

最简单的入门方法是打开一个新文档，而不是指定一个文档打开：

```python
from docx import Document

document = Document()
document.save('test.docx')
```

这个示例是基于内置的默认模板创建一个文档并把它保存成一个没有改变的文件名：`test.docx`。这个默认模板实质上是一个没有任何内容的新文档，保存在你已经安装好的python-docx包里。选择Word Doucument模板与你在Word中选择【文件】-【新模板】菜单选项选择的Word Document（Word文件选项里面好像没有这个选项(￣▽￣)"，感觉应该是文件-->新建里面选择的模板）大致相同。

#### “真正”打开一个文档

如果说你想要更多的改变最终文档，或者说更改已经存在的一个文档，这个时候你则需要打开一个存在着文件名的一个文档：

```python
document = Document('存在的文档.docx')
document.save('重命名的文档.docx')
```

**注意事项**：

* 你可以用这个方法打开任何`Word 2007`及以后的版本(`Word 2003`及更早期的.doc文件我们无法使用)。虽然也许你不能很好的编辑内容，但是你可以很好的加载和保存。它现在还在完善中，因此你现在还不能进行添加或者改变标题或者脚注之类的东西，但是Python-docx会很“客气的”把这些内容单独放在一边并足够聪明的保存它们不用实际理解他们到底是什么。
* 如果你在打开文件和保存文件的时候使用了同一个文件名，python-docx将会按照你的意思覆盖原始文件而不用其它提醒。你要确定那就是你想要的。

#### 打开一个“类文件”文档

python-docx可以打开一个文档从要一个“类文件”对象中，当然也可以同样保存一个“类文件”对象。这当你想要从网络或者数据库中获取源或文档而不想（不允许）与本地文件系统交互的时候是非常方便的。实际上，这意味着你可以通过打开文件或者StringIO/BytesIO流中对象来打开或者保存一个文档：

```python
f = open('foobar.docx', 'rb')
document = Document(f)
f.close()
# or
with open('foobar.docx', 'rb') as f:
    source_stream = StringIO(f.read())
document = Document(source_stream)
source_stream.close()
...
target_stream = StringIO()
document.save(target_stream)
```

不是所有的操作系统都要求这个'rb'打开文件模式的参数，在某些操作系统里面'r'就足够了，但是在Windows或者要给Linux一些系统中是需要'b'(选择二进制模式)这个参数去允许打开zip文件格式的文件的。
好了，你已经打开了一个文档并且确信它可以稍后保存在某一个地方。下一步则是获取一些内容.....

### 处理文本

为更有效的处理文本，理解一些块级元素比如段落和内联级别比如run是非常重要的。

#### 块级和内联文本对象

段落是Word中的主要块级对象。

块级项中的文本主要包含在它左右边沿之间。当文本的内容超过了它的右边界时，这些超出的文本则就会添加到下一行。对于段落而言，边界通常是页边距，但是如果段落在列中展开的话，边界也可以是列边界，如果在在表格里面的单元格中发生的话，它也是单元格的边界
表格通常是一个块级对象。

一个内联对象通常是一个块级项内容发生的一部分，一个例子便是在Word中的一个粗体的单词和一个全部为大写的句子。而最主要的内联对象便是运行。所有块容器中的内容里面都在内联对象里面，一个段落包含一个或者多个run，他们每个都是段落文本的一部分。

块级项的属性指定其在页面上的位置，例如缩进和段前段后的空格。内联项通常指定显示内容的字体、字号、粗体、斜体等。

#### 段落属性

一个段落有许多属性，他们通常指定在容器中的位置（通常在页面中）以及将行分成不同行的方法。
通常情况下，应该将段落格式的属性集成到一个组中，然后应用到段落中，而不是每次都重复的将他们属性添加到段落中。这类似于CSS与HTML如何一起工作。这里所有的段落属性都可使用样式设置，也可直接应用于段落。

段落的格式属性是用通过`ParagraphFormat对象`访问的，该对象使用段落的`Paragraph_Format属性`。

##### 水平对齐

也称为对齐，通过使用枚举WD_PARAGRAPH_ALIGNMENT可以将段落的水平对齐设置为左、中、右或两端对齐(在左和右对齐)：

```python
>>> from docx.enum.text import WD_ALIGN_PARAGRAPH
>>> document = Document()
>>> paragraph = document.add_paragraph()
>>> paragraph_format = paragraph.paragraph_format
>>> paragraph_format.alignment
None  # indicating alignment is inherited from the style hierarchy
>>> paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
>>> paragraph_format.alignment
CENTER (1)
```

##### 缩进

缩进是段落于容器边缘之间的水平空间，通常我们叫做页边距。段落我们可以在左边和右边分别缩进，段落第一行也可以拥有和其他行不一样的缩进量。第一行相较于其他行缩进来说成为首行缩进，而其他行相较于首行的缩进我们则称之为悬挂缩进。

缩进使用的长度值（例如英寸、磅、厘米）指定的。负值有效但这将导致段落重叠。空值则表示缩进是直接继承的层次结构值。将`None`赋值给缩进属性则会移除直接应用的缩进属性设置并且从层次结构中还原继承。

```python
>>> from docx.shared import Inches
>>> paragraph = document.add_paragraph()
>>> paragraph_format = paragraph.paragraph_format
>>> paragraph_format.left_indent
None  # indicating indentation is inherited from the style hierarchy
>>> paragraph_format.left_indent = Inches(0.5)
>>> paragraph_format.left_indent
457200
>>> paragraph_format.left_indent.inches
0.5
```

右边的缩进也类似：

```python
>>> from docx.shared import Pt
>>> paragraph_format.right_indent
None
>>> paragraph_format.right_indent = Pt(24)
>>> paragraph_format.right_indent
304800
>>> paragraph_format.right_indent.pt
24.0
```

首行行缩进是使用`first_line_indent`属性指定的，并且是相对于左缩进行来说的。负值表示悬挂缩进：

```python
>>> paragraph_format.first_line_indent
None
>>> paragraph_format.first_line_indent = Inches(-0.25)
>>> paragraph_format.first_line_indent
-228600
>>> paragraph_format.first_line_indent.inches
-0.25
```

##### 制表位

制表位停止了制表符的呈现，特别的是，他可以指定制表符后面文本开始的位置，以及将如何对齐到该位置，以及一个可选的leader字符，它将填充选项卡所跨越的水平空间。可以通过tab填满的可选主要字符。

段落或样式的制表符包含在一个`TabStops`对象中，该对象使用`ParagrapFormat`上的`tab_stops`属性访问：

```python
>>> tab_stops = paragraph_format.tab_stops
>>> tab_stops
<docx.text.tabstops.TabStops object at 0x106b802d8>
```

使用`add_tab-stop()`方法添加一个新的制表位：

```python
>>> tab_stop = tab_stops.add_tab_stop(Inches(1.5))
>>> tab_stop.position
1371600
>>> tab_stop.position.inches
1.5
```

默认是左对齐，但是可以通过提供`WD_TAB_ALIGNMENT`枚举成员来指定。 前导符默认是空格，但我们可以通过提供`WD_TAB_LEADER`来指定：

```python
>>> from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
>>> tab_stop = tab_stops.add_tab_stop(Inches(1.5), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
>>> print(tab_stop.alignment)
RIGHT (2)
>>> print(tab_stop.leader)
DOTS (1)
```

使用TabStops上的序列语义访问现有的制表符：

```python
>>> tab_stops[0]
<docx.text.tabstops.TabStop object at 0x1105427e8>
```

更多信息请见`TabStops`和`TabStop API`文档

##### 段落间距

space_before和space_after属性控制着段间距，控制着段前段后的距离。

段间距在页面布局内被折叠，这意味着两段之间的间距是第一段的空格后和第二段空格前的最大值。段间距被指定为一个长度值，通常使用Pt:

```python
>>> paragraph_format.space_before, paragraph_format.space_after
(None, None)  # inherited by default
>>> paragraph_format.space_before = Pt(18)
>>> paragraph_format.space_before.pt
18.0
>>> paragraph_format.space_after = Pt(12)
>>> paragraph_format.space_after.pt
12.0
```

##### 行距

行间距是指段落中行基线之间的距离。行间距可以指定为绝对距离，也可以指定相对于行高度(基本上是所用字体的点大小)。一个典型的绝对衡量标准是18磅。一个典型的相对测量值将是两个空格(2.0倍行距)。默认的行距是一个空格(1.0倍行距).

行距是由line_spacing和line_spacing_rule属性的相互作用控制。line_spacing 是一个Length，是(小数)float，或者是零。Length表示绝对距离。浮点数表示多个float。None表示继承了行距。line_space_Rule是wd_line_space枚举或者None的成员：

```python
>>> from docx.shared import Length
>>> paragraph_format.line_spacing
None
>>> paragraph_format.line_spacing_rule
None
>>> paragraph_format.line_spacing = Pt(18)
>>> isinstance(paragraph_format.line_spacing, Length)
True
>>> paragraph_format.line_spacing.pt
18.0
>>> paragraph_format.line_spacing_rule
EXACTLY (4)
>>> paragraph_format.line_spacing = 1.75
>>> paragraph_format.line_spacing
1.75
>>> paragraph_format.line_spacing_rule
MULTIPLE (5)
```

##### 分页

四个段落属性kepp_together,keep_with_next、page_break_before、widow_control控制着段落在页面附近的显示。kepp_together会导致整个断过出现在同一个页面上，如果不这么做的就会在段落之前存在分页符。

`keep_with_next`会使后面的段落与当前段落出现在同一张页面内。举例来说，这将会被用在使节标题和小节内的段落保持在同一个页面。

`page_break_before`使得一个段落可以放置在一个新页面的顶部。这将会使得章节标题总是会从新页面开头出现。

`widow_control`会断开一个页面，以避免将段落的第一行或最后一行放在与段落其余部分分开的页面上。

所有的这四种属性都是有三种状态的，即他们可以取值`True`、`False`或者`None`.`None`表示这些属性值将会继承层次结构，`True`表示打开，`Flase`表示关闭：

```python
>>> paragraph_format.keep_together
None  # all four inherit by default
>>> paragraph_format.keep_with_next = True
>>> paragraph_format.keep_with_next
True
>>> paragraph_format.page_break_before = False
>>> paragraph_format.page_break_before
False
```

#### 应用字符格式

字符格式通常被应用在Run级，举例来说它通常包含字号、字体、粗体、斜体、下划线。

`Run对象`的只读`Font属性`提供对`font对象`的访问。run的Font对象提供了获取和设置该运行的字符格式的属性。

这里提供了几个例子，有关可用属性的完整集合，请参阅`Font API`文档。

`run`中的`font`可通过如下方式访问：

```python
>>> from docx import Document
>>> document = Document()
>>> run = document.add_paragraph().add_run()
>>> font = run.font
```

字体和字号通常像这样设置：

```python
>>> from docx.shared import Pt
>>> font.name = 'Calibri'
>>> font.size = Pt(12)
```

许多字体属性是三态的，即也可以取值`True`,`False`以及`None`.`True`意味着属性是可以用，而`False`则与之相反。而`None`从概念上讲则意味着"继承”。运行存在于继承层次结构的样式中，默认情况下从该层次结构继承其字符格式。使用`Font对象`直接应用的任何字符格式都会覆盖继承的值。
加粗和斜体是三态属性，全大写、删除线、上标等等也是。有关完整列表，请参阅`FontAPI`文档:

```python
>>> font.bold, font.italic
(None, None)
>>> font.italic = True
>>> font.italic
True
>>> font.italic = False
>>> font.italic
False
>>> font.italic = None
>>> font.italic
None
```

`Underline`是一个特例。它是三态属性和枚举值属性的混合。`True`表示单下划线，这是目前最常见的。`False`表示不需要下划线，但通常情况下，如果s属性值为None，则也代表不需要下划线。其他形式的下划线，如双划线或虚线，都是由`WD_UNDERLINE`枚举成员指定的:

```python
>>> font.underline
None
>>> font.underline = True
>>> # or perhaps
>>> font.underline = WD_UNDERLINE.DOT_DASH
```

##### 字体颜色

每个`Font对象`都有一个`ColorFormat对象`，该对象提供对其颜色的访问，可通过其只读`color属性`访问。

给字体指定一个`RGB`颜色：

```python
>>> from docx.shared import RGBColor
>>> font.color.rgb = RGBColor(0x42, 0x24, 0xE9)
```

字体的颜色可以恢复到它的默认值(继承)，通过分配`None`给`rgb`或`theme_color属性`的`ColorFormat`:

```python
>>> font.color.rgb = None
```

确定字体的颜色首先要确定字体的颜色类型:

```python
>>> font.color.type
RGB (1)
```

颜色类型属性的值可以是`MSO_COLOR_TYPE`枚举的成员或None。`MSO_COLOR_TYPE.RGB`表示它是`RGB`颜色。`MSO_COLOR_TYPE.THEME`表示主题颜色.`MSO_COLOR_TYPE.AUTO`表示其值由应用程序自动确定，通常设置为黑色。(这个值比较罕见).`None`表示没有应用颜色，颜色是从样式层次结构继承而来的;这是最常见的情况。
当颜色类型是`MSO_COLOR_TYPE.RGB`时，rgb属性为`RGBColor`值，表示RGB颜色:

```python
>>> font.color.rgb
RGBColor(0x42, 0x24, 0xe9)
```

当颜色类型为`MSO_COLOR_TYPE.THEME`,`theme_color属性`将是`MSO_THEME_COLOR_INDEX`的成员，表示主题颜色:

```python
>>> font.color.theme_color
ACCENT_1 (5)
```

### 处理章节

`Word`支持`section`的概念，`section`是文档中具有相同页面布局设置(如页边距和页面方向)的部分。例如，这就是文档如何在纵向布局中包含一些页面，在横向布局中包含一些页面的方法。

大多数`Word文档`只有默认出现的一个部分，而且大多数文档没有理由更改默认的页边距或其他页面布局。但是，当您确实需要更改页面布局时，您需要了解各个部分才能完成。

#### 访问sections

对文档部分的访问由Document对象上的sections属性提供:

```python
>>> document = Document()
>>> sections = document.sections
>>> sections
<docx.parts.document.Sections object at 0x1deadbeef>
>>> len(sections)
3
>>> section = sections[0]
>>> section
<docx.section.Section object at 0x1deadbeef>
>>> for section in sections:
...     print(section.start_type)
...
NEW_PAGE (2)
EVEN_PAGE (3)
ODD_PAGE (4)
```

从理论上讲，文档没有标明`sections`是可能的，尽管我还没有看到这种情况在发生。如果您正在访问不可预知的`.docx`文件，您可能希望使用`len()`检查或`try语句`来避免未捕获的`IndexError异常`阻止您的程序。

#### 添加一个新的

`sectionsadd_section()`方法允许在文档末尾添加一个新的`section`。调用此方法后添加的段落和表将出现在新的`section`中:

```python
>>> current_section = document.sections[-1]  # last section in document
>>> current_section.start_type
NEW_PAGE (2)
>>> new_section = document.add_section(WD_SECTION.ODD_PAGE)
>>> new_section.start_type
ODD_PAGE (4)
```

#### Section 属性

`Section对象`有允许发现和指定页面布局设置的11个属性。

##### Section开始类型

`Section.start_type`描述的是section之前的隔断类型：

```python
>>> section.start_type
NEW_PAGE (2)
>>> section.start_type = WD_SECTION.ODD_PAGE
>>> section.start_type
ODD_PAGE (4)
```

`start_type`值是枚举变量`WD_SECTION_START`的成员

##### 页面尺寸和方向

`Section`中的三个属性描述了页面的尺寸和方向。这些可以一起使用，例如，将`Section`的方向由纵向到横向:

```python
>>> section.orientation, section.page_width, section.page_height
(PORTRAIT (0), 7772400, 10058400)  # (Inches(8.5), Inches(11))
>>> new_width, new_height = section.page_height, section.page_width
>>> section.orientation = WD_ORIENT.LANDSCAPE
>>> section.page_width = new_width
>>> section.page_height = new_height
>>> section.orientation, section.page_width, section.page_height
(LANDSCAPE (1), 10058400, 7772400)
```

##### 页边距

Section的7个属性一起指定了决定文本出现在页面上的不同页边距:

```python
>>> from docx.shared import Inches
>>> section.left_margin, section.right_margin
(1143000, 1143000)  # (Inches(1.25), Inches(1.25))
>>> section.top_margin, section.bottom_margin
(914400, 914400)  # (Inches(1), Inches(1))
>>> section.gutter
0
>>> section.header_distance, section.footer_distance
(457200, 457200)  # (Inches(0.5), Inches(0.5))
>>> section.left_margin = Inches(1.5)
>>> section.right_margin = Inches(1)
>>> section.left_margin, section.right_margin
(1371600, 914400)
```

### API基础

`python-docx`的`API`旨在使简单的事情变得简单，同时允许通过适度和增强的理解来实现更复杂的结果。

仅使用一个对象`docx.api.Document`就可以创建基本文档是可能的，即打开文件时返回文档对象。`docx.api.Document`上的方法,文档允许将`块级对象`添加到文档末尾。`块级对象`包括`段落`、`内联图片`和`表`。`标题`、`项目符号`和`编号列表`只是应用了特定样式的`段落`。

通过这种方式,我们可以从上到下“写”出一篇文章,几乎像一个人如果他们知道他们想要什么会说这个的基本用例,在内容总是添加到文档的最后,预计可能会占80%的实际使用情况下,这是一个优先的前提下尽可能地让它尽可能简单的力量整个`API`。

#### 内联对象

`docx.api.Document`上的每个块级方法。例如`add_paragraph()`，返回创建的块级对象,通常不需要引用;但是，当必须单独创建内联对象时，您需要使用块引用来完成。

...还有更多的示例...

### 了解样式

```text
Grasshopper：
“师傅，为什么我的段落不符合我指定的风格？”

师傅：
“那是因为你还需要把这篇文章阅读下去，Grasshopper”
```

#### 在Wrod中什么是样式？

当文档的的元素格式一致的时候，处理文档就会变得很容易。为了达到这种效果，文档专业设计者开发了样式表，样式表定义了文档元素类型以及指定了每种元素的格式。例如，段落主题被设置为：`字号`: 9pt，`字体`：Times Roman，`行间距`为11pt,`左端对齐`，`加粗`。当这些指定的内容被添加到每个文档的元素上面时，一个整体美观的外观是可以实现的。

`Word`中的样式是一组可以一次性应用于文档的规范。`Word`有`段落样式`、`字符样式`、`表格样式`和`数字定义`。他们被应用于`段落`、`文本`、`表格`、`列表`等等。

有经验的程序员会将样式定位为间接`Level`,关于它的好处其中之一便是允许你定义一次，利用多次，这样定义节省了很多相同的工作，但更重要的是它允许你改变定义并将改变反应在你应用的所有位置上面。

#### 为什么我应用的样式不显示？

这其中可能发生的事情可能会相当多, 直到我可以添加一些更高级的功能来解决它，这里先放一些。

1. 当你使用`Word`的时候，所有这些样式都可以被应用于文中，好看的可以变得更加好看，而且你不需要为自己再重新做，大多数自己的并不会比内置的更漂亮。
2. 虽然这些样式显示在你的UI里面，但它并不在你创建的文档里面，至少在你第一次使用他们之前。这种事非常好的，他们会占用相当大的空间，而且很多。如果文件包含所有你可以使用但没有使用的样式，这会
3. 如果你使用了`python-docx`未在文件中使用的样式来应用样式(如果你好奇的话，可以到`styles.xml`去查看)，`Word`就会忽视它。他不会抱怨，但是他同样改变不了文件的格式。我确定那是个好理由，但如果你不能理解`Word`的话，那你则可以把它当做一个谜题了。
4.你如你应用了样式，`Word`就会把样式保存在文件中，一旦在文件中了，它就会一直在那儿。应该有办法将它删掉，但是你得努力。如果你使用了样式，删除了样式，但是当你保存文件时，它还是在那儿。

添加这些就是希望注意: 如果你使用`python-docx`要在创建的文档中使用样式,则以文档的开头就必须包含样式定义。否则就不会工作，它不会引发异常, 它只是不起作用。
如果你使用 "默认" 模板文档, 它包含下面列出的样式, 大多数你可能是你想要的,如果你不设计自己的。如果您使用的是自己的起始文档, 则需要在其中至少使用一次所需的样式。您不必保留内容, 但您需要在保存文档之前至少将该样式应用于某种方式。写上一个字或一个词语, 连续应用五种样式,然后删除段落这样工作就可以了。这就是我如何把下面的那些放入默认模板:)。

#### Glossary

**样式定义**: 文档样式部分中的元素`<w:style>`，它显式地定义了样式的属性。

**定义样式**:

* **文档**: 已经在文档中明确定义的文档隐藏样式相区别。
* **内置样式**: `Word`中含有276个预设风格的预设样式在`Word`中，例如像“**Heading 1**”。内置样式可以是`显式的`也可以是`隐式的`。而尚未定义的样式称为`隐式样式`。但是不管显式定义还是隐式定义的都可以在`Word`的样式面板或者样式选项中出现。

* **自定义格式**: 可以被称为用户样式，即所有不是预设样式的样式，注意下自定义样式不能为隐藏样式。

* **隐式样式**: 在特定文档中没有定义的内置样式称为该文档中的隐式样式。根据文档中的LatentStyles对象中的设置，隐式样式可以作为UI中的选项出现。

* **推荐列表样式**: 从样式列表下拉框中选择【推荐】时，样式工具箱或面板中出现的样式列表。

* **样式库**: 出现在`Word UI`中的示例样式的选择，可以通过单击其中之一来应用。 (The selection of example styles that appear in the ribbon of the Word UI and which may be applied by clicking on one of them.)

#### 识别样式

一个样式有三个识别属性，`name`,`style_id`和`type`。

每个样式的`name属性`都是稳定的，是用于访问的`唯一标识符`。

样式的`style_id`在内部用于将内容对象(如段落)设为其样式。然而，这个值是由Word自动生成的，不能保证在整个保存过程中都是稳定的。通常, `style_id`只是通过从本地化样式名称中删除空格形成的，但是也有例外。`python-docx`的用户通常应该避免使用样式id，除非他们对所涉及的内部内容有信心。

样式的`type`是在创建时设置的，不能更改。

#### 内置样式

`Word`有近300种所谓的内置样式，比如`Normal`、`Heading 1`和`List Bullet`。样式定义存储在`styles.xml`是`docx包`的一部分，但是内置的样式定义存储在`Word应用程序`本身中，不写入`styles.xml`。直到真正使用`xml`。这是一种明智的策略，因为它们占用了大量空间，否则将在每个`.docx`文件中产生大量冗余和无用的开销。

内置样式直到使用后才写入`python.docx`包，这一事实引起了对隐式样式的需求。

#### 样式行为

除了收集一组格式化属性外，样式还有五个属性指定其`behavior`。这种行为相对简单，基本上等同于样式出现在`Word`或`LibreOffice UI`中的时间和位置。

理解样式行为的关键概念是`推荐列表`。在`Word`中的“样式”窗格中，用户可以选择要查看的样式列表。其中一个被命名为“`推荐列表`”，称为“`推荐列表`”。所有五种行为属性都会影响样式在这个列表和样式库中的外观的某些方面。

简而言之，如果一个样式的隐藏属性为`False`(默认)，那么它就会出现在推荐列表中。如果一个样式没有隐藏，并且它的`quick_style属性`为`True`，那么它也会出现在样式库中。如果`隐藏样式`的`unhide_when_used属性`为`True`，那么它的隐藏属性在第一次使用时就设置为`False`。`样式列表`和`样式库中`的样式按照优先级排序，然后按照字母顺序排序相同优先级的样式。如果样式的`locked属性`为`True`，并且文档的格式限制被打开，那么样式将不会出现在任何列表或样式库中，并且不能应用于内容。

#### 隐式样式

需要指定没有在`style.sxml`中定义的`内置样式`的`UI`行为。就需要隐式样式定义。隐式样式定义基本上是`根样式定义`，除了样式名称之外，它最多有五个行为属性。通过为每个行为属性定义默认值来节省额外的空间，因此只需要定义那些与默认值不同的属性，并且匹配所有默认值的样式不需要隐式的样式定义。

潜在的样式定义使用`w:latentStyles`和`w:lsdException`元素指定，这些元素出现在`styles.xml`中。

内建样式只需要隐式样式定义，因为只有内建样式可以出现在UI中，而不需要在`styles.xml`中定义样式。

#### 样式继承

样式可以从另一种样式继承属性，有点类似于级联样式表(`CSS`)的工作方式。使用`base_style属性`指定继承。通过将一种样式建立在另一种样式的基础上，就可以形成任意深度的继承层次结构。没有`基本样式`的`样式`从`默认文档`继承属性。

#### 默认模板中的段落样式

1. Normal
2. Body Text
3. Body Text 2
4. Body Text 3
5. Caption
6. Heading 1
7. Heading 2
8. Heading 3
9. Heading 4
10. Heading 5
11. Heading 6
12. Heading 7
13. Heading 8
14. Heading 9
15. Intense Quote
16. List
17. List 2
18. List 3
19. List Bullet
20. List Bullet 2
21. List Bullet 3
22. List Continue
23. List Continue 2
24. List Continue 3
25. List Number
26. List Number 2
27. List Number 3
28. List Paragraph
29. Macro Text
30. No Spacing
31. Quote
32. Subtitle
33. TOCHeading
34. Title

#### 默认模板中的表格样式

1. Table Normal
2. Colorful Grid
3. Colorful Grid Accent 1
4. Colorful Grid Accent 2
5. Colorful Grid Accent 3
6. Colorful Grid Accent 4
7. Colorful Grid Accent 5
8. Colorful Grid Accent 6
9. Colorful List
10. Colorful List Accent 1
11. Colorful List Accent 2
12. Colorful List Accent 3
13. Colorful List Accent 4
14. Colorful List Accent 5
15. Colorful List Accent 6
16. Colorful Shading
17. Colorful Shading Accent 1
18. Colorful Shading Accent 2
19. Colorful Shading Accent 3
20. Colorful Shading Accent 4
21. Colorful Shading Accent 5
22. Colorful Shading Accent 6
23. Dark List
24. Dark List Accent 1
25. Dark List Accent 2
26. Dark List Accent 3
27. Dark List Accent 4
28. Dark List Accent 5
29. Dark List Accent 6
30. Light Grid
31. Light Grid Accent 1
32. Light Grid Accent 2
33. Light Grid Accent 3
34. Light Grid Accent 4
35. Light Grid Accent 5
36. Light Grid Accent 6
37. Light List
38. Light List Accent 1
39. Light List Accent 2
40. Light List Accent 3
41. Light List Accent 4
42. Light List Accent 5
43. Light List Accent 6
44. Light Shading
45. Light Shading Accent 1
46. Light Shading Accent 2
47. Light Shading Accent 3
48. Light Shading Accent 4
49. Light Shading Accent 5
50. Light Shading Accent 6
51. Medium Grid 1
52. Medium Grid 1 Accent 1
53. Medium Grid 1 Accent 2
54. Medium Grid 1 Accent 3
55. Medium Grid 1 Accent 4
56. Medium Grid 1 Accent 5
57. Medium Grid 1 Accent 6
58. Medium Grid 2
59. Medium Grid 2 Accent 1
60. Medium Grid 2 Accent 2
61. Medium Grid 2 Accent 3
62. Medium Grid 2 Accent 4
63. Medium Grid 2 Accent 5
64. Medium Grid 2 Accent 6
65. Medium Grid 3
66. Medium Grid 3 Accent 1
67. Medium Grid 3 Accent 2
68. Medium Grid 3 Accent 3
69. Medium Grid 3 Accent 4
70. Medium Grid 3 Accent 5
71. Medium Grid 3 Accent 6
72. Medium List 1
73. Medium List 1 Accent 1
74. Medium List 1 Accent 2
75. Medium List 1 Accent 3
76. Medium List 1 Accent 4
77. Medium List 1 Accent 5
78. Medium List 1 Accent 6
79. Medium List 2
80. Medium List 2 Accent 1
81. Medium List 2 Accent 2
82. Medium List 2 Accent 3
83. Medium List 2 Accent 4
84. Medium List 2 Accent 5
85. Medium List 2 Accent 6
86. Medium Shading 1
87. Medium Shading 1 Accent 1
88. Medium Shading 1 Accent 2
89. Medium Shading 1 Accent 3
90. Medium Shading 1 Accent 4
91. Medium Shading 1 Accent 5
92. Medium Shading 1 Accent 6
93. Medium Shading 2
94. Medium Shading 2 Accent 1
95. Medium Shading 2 Accent 2
96. Medium Shading 2 Accent 3
97. Medium Shading 2 Accent 4
98. Medium Shading 2 Accent 5
99. Medium Shading 2 Accent 6
100. Table Grid

### 处理样式

本页使用了前一小节的概念，如果不熟悉，请参阅前一节[**了解样式**](#了解样式)

#### 访问一个样式

样式可以通过使用`Document.styles`属性访问：

```python
>>> document = Document()
>>> styles = document.styles
>>> styles
<docx.styles.styles.Styles object at 0x10a7c4f50>
```

`style对象`提供了对通过名称定义的样式的字典式访问:

```python
>>> styles['Normal']
<docx.styles.style._ParagraphStyle object at <0x10a7c4f6b>
```

**注意**: 内置样式使用英文名称(如“`Heading 1`”)存储在`WordprocessingML文件`中，但是 使用本地化版本的`Word`的用户还是会在`UI`中看到本地语言名称(如“`Kop1`”)。因为`python-docx`操作`WordprocessingML`文件，样式查找必须使用英文名。这个外部站点上的文档允许您在本地语言名称和英语样式名称之间创建映射: <http://www.thedoctools.com/index.php?show=mt_create_style_name_list> 用户定义的样式(也称为`自定义样式`)不是本地化的，它们是通过与`Word`中的`UI`中的相同的名字来访问的。

`Styles对象`也是可以迭代的，通过使用`BaseStyle`上的标识属性，可以生成定义样式的各种子集。例如，这段代码将生成一个定义的段落样式列表:

```python
>>> from docx.enum.style import WD_STYLE_TYPE
>>> styles = document.styles
>>> paragraph_styles = [
...     s for s in styles if s.type == WD_STYLE_TYPE.PARAGRAPH
... ]
>>> for style in paragraph_styles:
...     print(style.name)
...
Normal
Body Text
List Bullet
```

#### 应用一个样式

`Paragraph`、`Run`和`Table对象`每个都有`Styles`属性，为这些属性分配一个样式对象将应用该样式:

```python
>>> document = Document()
>>> paragraph = document.add_paragraph()
>>> paragraph.style
<docx.styles.style._ParagraphStyle object at <0x11a7c4c50>
>>> paragraph.style.name
'Normal'
>>> paragraph.style = document.styles['Heading 1']
>>> paragraph.style.name
'Heading 1'
```

样式名也可以直接指定，在这种情况下，`python-docx`将为您执行查找

```python
>>> paragraph.style = 'List Bullet'
>>> paragraph.style
<docx.styles.style._ParagraphStyle object at <0x10a7c4f84>
>>> paragraph.style.name
'List Bullet'
```

样式还可以在创建时使用样式对象或其名称:

```python
>>> paragraph = document.add_paragraph(style='Body Text')
>>> paragraph.style.name
'Body Text'
>>> body_text_style = document.styles['Body Text']
>>> paragraph = document.add_paragraph(style=body_text_style)
>>> paragraph.style.name
'Body Text'
```

#### 添加或删除样式

一个新样式可以通过指定一个唯一的名字和类型来添加到文档中：

```python
>>> from docx.enum.style import WD_STYLE_TYPE
>>> styles = document.styles
>>> style = styles.add_style('Citation', WD_STYLE_TYPE.PARAGRAPH)
>>> style.name
'Citation'
>>> style.type
PARAGRAPH (1)
```

使用`base_style属性`指定新样式应该从以下位置继承格式设置:

```python
>>> style.base_style
None
>>> style.base_style = styles['Normal']
>>> style.base_style
<docx.styles.style._ParagraphStyle object at 0x10a7a9550>
>>> style.base_style.name
'Normal'
```

一个样式可以通过使用一个简单的`delete()`方法来删除：

```python
>>> styles = document.styles
>>> len(styles)
10
>>> styles['Citation'].delete()
>>> len(styles)
9
```

**注意**: 从文档中删除`Style.delete()`方法。它不会影响应用该样式的文档中的内容。具有文档中未定义的样式的内容是使用该内容对象的默认样式呈现的，例如段落中的`“Normal”`

#### 定义字符格式

`字符`、`段落`和`表样式`都可以指定要应用于具有该样式的内容的`字符格式`。可以直接应用于文本的所有`字符格式`都可以用样式指定。示例包括字符`字体`和`大小`、`粗体`、`斜体`和`下划线`。

这三种样式类型中的每一种都有一个`font属性`，提供对`Font对象`的访问。样式的字体对象提供了获取和设置该样式的`字符格式`的属性。

这里提供了几个例子，要想了解更详细的信息，请参阅：`Font API参考手册`。

`Font样式`可以通过这样访问：

```python
>>> from docx import Document
>>> document = Document()
>>> style = document.styles['Normal']
>>> font = style.font
```

字体和字号可以通过这样访问：

```python
>>> from docx.shared import Pt
>>> font.name = 'Calibri'
>>> font.size = Pt(12)
```

许多字体属性都是`三态`的，意味着，意味着他们可以有：`True`,`False`和`None`。`True`意味着属性是`“打开”`，`False`意味着`“关闭”`，从概念上说，`None`意味着`“继承”`。因为样式存在于继承层次结构中，所以有能力在层次结构中的正确位置指定属性是很重要的，通常是在层次结构中越高越好。例如，如果所有标题都应该使用Arial字体，那么在标题1样式上设置这个属性，让标题2从标题1继承就更有意义了。

粗体和斜体是`三态`属性，`全大写`、`删除线`、`上标`等等也是三态属性。有关完整列表，请参阅`FontAPI文档`:

```python
>>> font.bold, font.italic
(None, None)
>>> font.italic = True
>>> font.italic
True
>>> font.italic = False
>>> font.italic
False
>>> font.italic = None
>>> font.italic
None
```

下划线是一种特殊的情况，它是三态属性和枚举值属性的混合。`True`表示单下划线，这是目前最常见的。`False`表示不需要下划线，但如果不需要下划线，通常都不是正确的选择，因为很少从基本样式继承下划线。其他形式的下划线，如`双划线`或`虚线`，都是由`WD_UNDERLINE`枚举成员指定的:

```python
>>> font.underline
None
>>> font.underline = True
>>> # or perhaps
>>> font.underline = WD_UNDERLINE.DOT_DASH
```

#### 定义段落格式

`段落样式`和`表格样式`都允许指定`段落格式`。这些样式都提供了对`ParagraphFormat对象`的`paragraph_format属性`的访问方法。

`段落格式`包括`布局`，如`对齐`、`缩进`、`前后空格`、`前分页`和`孤行控制`。有关可用属性的完整列表，请参阅`ParagraphFormat的API文档`。

这是一个例子，告诉你如何创建一个`段落样式`，悬挂缩进1/4字符，12pint的间距，和孤行控制:

```python
>>> from docx.enum.style import WD_STYLE_TYPE
>>> from docx.shared import Inches, Pt
>>> document = Document()
>>> style = document.styles.add_style('Indent', WD_STYLE_TYPE.PARAGRAPH)
>>> paragraph_format = style.paragraph_format
>>> paragraph_format.left_indent = Inches(0.25)
>>> paragraph_format.first_line_indent = Inches(-0.25)
>>> paragraph_format.space_before = Pt(12)
>>> paragraph_format.widow_control = True
```

#### 使用特定段落的样式属性

段落样式具有`next_paragraph_style`属性，该属性指定将应用于在该样式的段落之后插入的新段落的样式。当样式通常只在序列中出现一次(如标题)时，这是非常有用的。在这种情况下，段落样式可以在完成标题后自动恢复为主体样式。

在大多数的情况下(正文段落)，后续段落应采用与当前段落相同的风格。如果没有指定下一段的样式，默认的样式可以通过应用相同的样式很好地处理这种情况。

这里是一个如果在一个主体文本里改变下一段标题1样式的的例子：

```python
>>> from docx import Document
>>> document = Document()
>>> styles = document.styles
>>> styles['Heading 1'].next_paragraph_style = styles['Body Text']
```

这种默认可以通过设置其为`None`或`样式本身`来恢复:

```python
>>> heading_1_style = styles['Heading 1']
>>> heading_1_style.next_paragraph_style.name
'Body Text'
>>> heading_1_style.next_paragraph_style = heading_1_style
>>> heading_1_style.next_paragraph_style.name
'Heading 1'
>>> heading_1_style.next_paragraph_style = None
>>> heading_1_style.next_paragraph_style.name
'Heading 1'
```

##### 控制在Word的UI中样式如何显示？

样式的属性分为两类，`行为属性`和`格式属性`。它的**行为属性控制样式在UI中出现的时间和位置**。它的**格式属性决定了应用样式的内容的格式**，比如字体的大小和段落缩进。

这是5中样式的行为属性；

* hidden
* unhide_when_used
* priority
* quick_style
* locked

有关这些行为属性如何交互的描述，请参阅“[**了解样式**](#了解样式)”中的“[**样式行为**](#样式行为)”部分，以确定样式在UI中出现的时间和位置。
优先级属性接受一个整数值。其他四个样式行为属性是`三态属性`，这意味着它们可以取值`True`(打开)、`False`(关闭)或`None`(继承)。

##### 在样式库中显示一个样式

以下代码将使“正文文本”段落样式首先出现在样式库中:

```python
>>> from docx import Document
>>> document = Document()
>>> style = document.styles['Body Text']
>>> style.hidden = False
>>> style.quick_style = True
>>> style.priorty = 1
```

##### 在样式库中移除一个样式

他的代码将从样式库中删除“`普通`”段落样式，但允许它保留在推荐列表中:

```python
>>> style = document.styles['Normal']
>>> style.hidden = False
>>> style.quick_style = False
```

#### 处理隐式样式

请参阅“[**了解样式**](#了解样式)”中的“[**内置样式**](#内置样式)”和“[**隐式样式**](#隐式样式)”部分，以了解隐式样式如何定义尚未在样式中定义的内建样式的行为属性在`python.docx文件`的`styles.xml部分`。

##### 在文档中访问隐式样式

```python
>>> document = Document()
>>> latent_styles = document.styles.latent_styles
```

`LatentStyles对象`支持`len()`方法，迭代、和通过样式名进行字典式访问：

```python
>>> len(latent_styles)
161
>>> latent_style_names = [ls.name for ls in latent_styles]
>>> latent_style_names
['Normal', 'Heading 1', 'Heading 2', ... 'TOC Heading']
>>> latent_quote = latent_styles['Quote']
>>> latent_quote
<docx.styles.latent.LatentStyle object at 0x10a7c4f50>
>>> latent_quote.priority
29
```

##### 改变隐式样式默认属性

`LatentStyles对象`还提供对当前文档中内置样式的默认行为属性的访问。这些默认值为`_LatentStyle`定义的任何未定义属性以及没有显式潜式定义的内置样式的所有行为属性提供值。有关`LatentStyles对象`的完整可用属性集，请`参阅API文档`:

```python
>>> latent_styles.default_to_locked
False
>>> latent_styles.default_to_locked = True
>>> latent_styles.default_to_locked
True
```

##### 添加一个隐式样式定义

在`LatentStyles`中可以通过使用一个`.add_latent_style()`方法 来添加一个隐式样式。

```python
>>> latent_style = latent_styles['List Bullet']
KeyError: no latent style with name 'List Bullet'
>>> latent_style = latent_styles.add_latent_style('List Bullet')
>>> latent_style.hidden = False
>>> latent_style.priority = 2
>>> latent_style.quick_style = True
```

#### 删除一个隐式样式定义

一个隐式样式删除可以通过 `delete()` 方法。

```python
>>> latent_styles['Light Grid']
<docx.styles.latent.LatentStyle object at 0x10a7c4f50>
>>> latent_styles['Light Grid'].delete()
>>> latent_styles['Light Grid']
KeyError: no latent style with name 'Light Grid'
```

### 了解图片及其他一些形状

**从概念上讲，Word文档有两个层，一个文本层和一个绘图层**。在`文本层`中，文本对象从左到右、从上到下流动，当先前的页面被填充时，就开始一个新的页面。在`绘图层`中，绘制对象(称为形状)被放置在任意位置。这些形状有时被称为浮动形状。

图片是可以出现在文本或`绘图层`中的形状。当它出现在`文本层`时，它被称为`内联形状`，或者更具体地说，`内联图片`。

`内联形状`被视为一个大文本字符(字符符号)。线的高度增加，以适应形状，形状被包装成一条线，它将适合宽度，就像文本。在它前面插入文本会使它向右移动。通常，一幅画是单独放在一段中，但这不是必需的。它可以在放置它的段落前后有文本。

在编写本文时，`python-docx`只支持`内联图片`。可以添加浮动图片。如果您有一个案例，请在问题跟踪器上提交一个特性请求。`add_picture()`方法将一个指定的图片添加到文档末尾的一个段落中。然而，通过深入挖掘API，您可以在图片的任意一侧放置文本，或者两者都放置。

## API参考文档

### Document对象

主要文档及相关对象

#### Document构造函数

* docx.Document(docx=None)
  返回从`docx`加载的文档对象，其中 `docx` 可以是 `.docx文件` (字符串)的路径，也可以是 `类文件对象`。
  如果 `docx` 缺少或没有，则加载内置的默认文档“模板”

#### Document对象

* `class docx.document.Document`
    WordprocessingML(WML)文档。不打算直接构造。使用`docx.Document()`打开或创建一个文档。
  * `add_heading(text=u'', level=1)`
    返回新添加到文档末尾的标题段落，其中包含文本，其段落样式由级别决定。如果`level`为`0`，样式设置为`Title`。如果级别是`1`(或省略)，则使用`标题1`。否则样式设置为`Heading {level}`。如果级别在`0-9`范围之外，就会增加`ValueError`值。
  * `add_page_break()`
    返回新添加到文档末尾的段落，仅包含分页符。
  * `add_paragraph(text=u'', style=None)`
    返回一个新添加到文档末尾的段落，用文本填充，具有段落样式。文本可以包含制表符(`\t`)字符，这些字符被转换为制表符的适当`XML格式`。文本还可以包括换行符(`\n`)或回车符(`\r`)，每个换行符都被转换为换行符。
  * `add_picture(image_path_or_stream, width=None, height=None)`
    返回在文档末尾自己的段落中添加的新图形形状。图片包含image_path_or_stream的图片，根据宽度和高度缩放。如果既没有指定宽度也没有指定高度，则图像将以其实际大小显示。如果只指定了一个，则使用它来计算一个缩放因子，然后应用于未指定的维数，以保持图像的长宽比。图的实际大小使用图像文件中指定的点每英寸(dpi)值计算，如果没有指定值，默认为`72 dpi`，通常情况下是这样的。
  * `add_section(start_type=2)`
    返回一个Section对象，表示在文档末尾添加的新节。可选的start_type参数必须是WD_SECTION_START枚举的成员，如果没有提供NEW_PAGE,默认为WD_SECTION。
  * `add_table(rows, cols, style=None)`
    添加一个分别具有行和cols行数和表样式的表和列计数的表。样式可以是段落样式对象或段落样式名称。如果样式为空，则表继承文档的默认表样式。
  * `core_properties`
    CoreProperties对象提供对本文档核心属性的读写访问。
  * `inline_shapes`
    一个InlineShapes对象，提供对该文档中内联形状的访问。内联形状是一个图形对象，例如图片，包含在一段文本中，表现得像字符符号，像段落中的其他文本一样流动。
  * `paragraphs`
    与文档中各段相对应的段落实例列表，按文档顺序排列。注意，或等修订标记中的段落不在此列表中。
  * `part`
    文档的部分对象。
  * `save(path_or_stream)`
    将此文档保存到path_or_stream，它可以是文件系统位置(字符串)的路径，也可以是类文件对象。
  * `sections`
    sections对象提供对本文档中每个节的访问。
  * `settings`
    一个Styles对象，提供对该文档中的样式的访问。
  * `tables`
    与文档中的表相对应的表实例列表，按文档顺序排列。注意，只有出现在文档顶层的表出现在这个列表中;嵌套在表单元格中的表不会出现。修订标记内的表，如<w:ins>或<w:del>，也不会出现在列表中

#### CoreProperties对象

每个`Document对象`都提供了通过`core_properties属性`来提供对其`CorePropertiesvV1`来对其`CoreProperties对象`的访问。`CoreProperties对象`为文档提供对所谓的核心属性的读写访问。核心属性包括`作者`、`类别`、`注释`、`content_status`、`已创建`、`标识符`、`关键字`、`语言`、`last_modified_by`、`last_print`、`modified`、`revision`、`主题`、`标题`和`版本`等。

每个属性都是三种类型之一，`str`和`datetime`以及`int`。字符串属性的长度限制为`255个字符`，如果没有设置，则返回一个空字符串(")。没有时区的`datetime对象`，即UTC格式。任何时区转换都是客户端的责任。如果未设置日期属性，则返回`None`。

`python-docx`不会自动设置任何文档核心属性，除非将核心属性部分添加到没有核心属性的表示中(非常少见)。如果`python-docx`添加了一个核心属性部分，那么它包含`标题`、`last_modified_by`、`修订`和`修改属性`的默认值。如果需要，客户端代码应该更新诸如修订和`last_modified_by`之类的属性。

```python
class docx.opc.coreprops.CoreProperties
    author
        string--主要负责生成资源内容的实体。
    category
        string--此包内容的分类。示例值可能包括:简历、信函、财务预测、提案或技术演示。
    comments
        string--对资源内容的描述。
    content_status
        string--文档的完成状态，例如“草稿”
    created
        datetime--文件初始创建时间
    identifier
        string--对给定上下文中的资源的明确引用，例如ISBN
    keywords
        string--描述性单词或短语可能被用作本文档的搜索词
    language
        string--文件使用的语言
    last_modified_by
        string--最后修改文档的人的姓名或其他标识符(如电子邮件地址)
    last_printed
        datetime--最后一次打印文件的时间
    modified
        datetime--最后一次修改文档的时间
    revision
        int此修订的编号，每次保存文档时都会递增。但是请注意，python-docx在保存文档时不会自动增加修订号。
    subject
        string--文章资源内容的主题
    title
        string--给定资源的名字
    version
        string--自由格式的版本字符串
```

### Document Settings 对象

```python
class docx.settings.Settings
    提供对文档级别设置的访问。使用 Document.settingsf访问。设置属性。

    element
        这个对象代理的lxml元素。
```

### 样式关系对象

`style`用于在单个名称下收集一组格式化属性，并一次性将这些属性应用于内容对象。这促进了整个文档和相关文档的格式一致性，并允许通过以适当的样式更改定义来全局地进行格式更改。

#### Styles 对象

```python
class docx.styles.styles.Styles
    提供对文档中定义的样式的访问的集合。使用Document.Style属性访问。
    通过样式名称支持len()、迭代和字典样式访问。

    add_style(name, style_type, builtin=False)
        返回一个新添加的style对象，类型为style_type，并通过名称进行标识。
        内建样式可以通过为可选的内建参数传递True来定义。
    default(style_type)
        返回style_type的默认样式或None(如果没有为该类型定义默认样式)。
    element
        这个对象代理的lxml元素
    latent_styles
        LatentStyles对象提供对隐式样式的默认行为和_LatentStyle对象集合的访问，
        这些对象定义了特定的隐式样式的默认覆盖。
```

#### BaseStyle 对象

```python
class docx.styles.style.BaseStyle
    用于各种类型的样式对象、段落、字符、表和编号的基类。
    所有样式对象都继承这些属性和方法。

    builtin
        只读。如果这个样式是内置样式则为Ture，False就说明这个是自定义（用户样式）。
        注意，这个值是基于XML中存在的customStyle属性，而不是基于关于哪些样式构建到Word中的特定知识。
    delete()
        从文档中删除样式定义。注意，调用此方法不会删除或更改应用于任何文档内容的样式。
        具有已删除样式的内容项将使用默认样式呈现，文档中未定义样式的任何内容也是如此。
    element
        代理这个对象的lxml元素。
    hidden
        如果在样式库和推荐样式列表中显示此样式被禁止，则为True。
        否则为False。为了在样式库中显示，这个值必须为False, quick_style必须为True。
    locked
        可读写的布尔值。 
        如果这个样式是被锁住的状态则为True，一个被锁住状态的样式不能再在样式面板中显示出来或者说不能被文档内容应用。
        只有在打开文档的格式保护时(通过Developer菜单)，该行为才会激活。
    name
        这个style的UI中的名字。
    priority
        此样式在Word UI中的整数排序控制显示序列的关键字。None表示没有定义任何设置，导致Word使用默认值0。
        样式名用作二级排序键，用于解析具有相同优先级值的样式的排序。
    quick_style
        如果这个样式显示在样式库中则为True，
        如果该样式在隐藏时应该显示在样式库中，则为False。读/写布尔值。
    type
        对应于该样式类型的WD_STYLE_TYPE的成员，例如WD_STYLE_TYPE.段落。
    unhide_when_used
        如果应用程序在下一次应用于内容时应该使该样式可见，则为True。否则False。
        请注意，当将python-docx应用于内容时，它不会自动地为该属性打开具有True的样式。
```

#### \_CharacterStyle 对象

```python
class docx.styles.style._CharacterStyle
    基础: docx.styles.style.BaseStyle
    字符样式。字符样式应用于Run对象，主要通过字体属性中的Font对象提供字符级格式。

    base_style
        如果此样式不是基于另一种样式，则此样式将继承或不继承。
    builtin
        只读。如果这个样式是内置样式则为Ture，False就说明这个是自定义（用户样式）。
        注意，这个值是基于XML中存在的customStyle属性，而不是基于关于哪些样式构建到Word中的特定知识。
    delete()
        从文档中删除样式定义。注意，调用此方法不会删除或更改应用于任何文档内容的样式。
        具有已删除样式的内容项将使用默认样式呈现，文档中未定义样式的任何内容也是如此。
    font
        Font对象提供对这种样式的字符格式属性(如字体名称和大小)的访问。
    hidden
        如果在样式库和推荐样式列表中显示此样式被禁止，则为True。否则为False。
        为了在样式库中显示，这个值必须为False以及 quick_style必须为True。
    locked
        可读写的布尔值。 
        如果这个样式是被锁住的状态则为True，一个被锁住状态的样式不能再在样式面板中显示出来或者说不能被文档内容应用。
        只有在打开文档的格式保护时(通过Developer菜单)，该行为才会激活。
    name
        这个style的UI中的名字。
    priority
        此样式在Word UI中的整数排序控制显示序列的关键字。
        None表示没有定义任何设置，导致Word使用默认值0。
        样式名用作二级排序键，用于解析具有相同优先级值的样式的排序。
    quick_style
        如果这个样式显示在样式库中则为True，
        如果该样式在隐藏时应该显示在样式库中，则为False。读/写布尔值。
    unhide_when_used
        如果应用程序在下一次应用于内容时应该使该样式可见，则为True。否则False。
        请注意，当将python-docx应用于内容时，它不会自动地为该属性打开具有True的样式。
```

#### \_ParagraphStyle 对象

```python
class docx.styles.style._ParagraphStyle
    基础: docx.styles.style._CharacterStyle
    一种段落样式，一个段落样式提供了字符格式和段落格式例如缩进和行间距。
    
    base_style
        如果此样式不是基于另一种样式，则此样式将继承或不继承。
    builtin
        只读。如果这个样式是内置样式则为Ture，False就说明这个是自定义（用户样式）。
        注意，这个值是基于XML中存在的customStyle属性，而不是基于关于哪些样式构建到Word中的特定知识。
    delete()
        从文档中删除样式定义。注意，调用此方法不会删除或更改应用于任何文档内容的样式。
        具有已删除样式的内容项将使用默认样式呈现，文档中未定义样式的任何内容也是如此。
    font
        Font对象提供对这种样式的字符格式属性(如字体名称和大小)的访问。
    hidden
        如果在样式库和推荐样式列表中显示此样式被禁止，则为True。
        否则为False。为了在样式库中显示，这个值必须为False以及 quick_style必须为True。
    locked
        可读写的布尔值。 
        如果这个样式是被锁住的状态则为True，一个被锁住状态的样式不能再在样式面板中显示出来或者说不能被文档内容应用。
        只有在打开文档的格式保护时(通过Developer菜单)，该行为才会激活。
    name
        这个style的UI中的名字。
    next_paragraph_style
        _CharacterStyle对象，该对象表示将自动应用于插入该样式后的新段落的样式。
        如果没有定义下一段样式，则返回self。分配None或self会删除设置，以便使用相同的样式创建新段落。
    paragraph_format
        _CharacterStyle对象提供了对于例如像缩进等段落格式属性这样样式的访问。
    priority
        此样式在Word UI中的整数排序控制显示序列的关键字。
        None表示没有定义任何设置，导致Word使用默认值0。
        样式名用作二级排序键，用于解析具有相同优先级值的样式的排序。
    quick_style
        如果这个样式显示在样式库中则为True，如果该样式在隐藏时应该显示在样式库中，则为False。读/写布尔值。
    unhide_when_used
        如果应用程序在下一次应用于内容时应该使该样式可见，则为True。
        否则False。请注意，当将python-docx应用于内容时，它不会自动地为该属性打开具有True的样式。
```

#### \_TableStyle 对象

```python
class docx.styles.style._TableStyle
    基础:docx.styles.style._ParagraphStyle
    一个表的风格。表样式为其内容提供字符和段落格式，以及特殊的表格式属性。
    
    base_style
        如果此样式不是基于另一种样式，则此样式将继承或不继承。
    builtin
        只读。如果这个样式是内置样式则为Ture，False就说明这个是自定义（用户样式）。
        注意，这个值是基于XML中存在的customStyle属性，而不是基于关于哪些样式构建到Word中的特定知识。
    delete()
        从文档中删除样式定义。注意，调用此方法不会删除或更改应用于任何文档内容的样式。
        具有已删除样式的内容项将使用默认样式呈现，文档中未定义样式的任何内容也是如此。
    font
        Font对象提供对这种样式的字符格式属性(如字体名称和大小)的访问。
    hidden
        如果在样式库和推荐样式列表中显示此样式被禁止，则为True。否则为False。
        为了在样式库中显示，这个值必须为False以及 quick_style必须为True。
    locked
        可读写的布尔值。 
        如果这个样式是被锁住的状态则为True，一个被锁住状态的样式不能再在样式面板中显示出来或者说不能被文档内容应用。
        只有在打开文档的格式保护时(通过Developer菜单)，该行为才会激活。
    name
        这个style的UI中的名字。
    next_paragraph_style
        _CharacterStyle对象，该对象表示将自动应用于插入该样式后的新段落的样式。
        如果没有定义下一段样式，则返回self。分配None或self会删除设置，以便使用相同的样式创建新段落。
    paragraph_format
        _CharacterStyle对象提供了对于例如像缩进等段落格式属性这样样式的访问。
    priority
        此样式在Word UI中的整数排序控制显示序列的关键字。
        None表示没有定义任何设置，导致Word使用默认值0。
        样式名用作二级排序键，用于解析具有相同优先级值的样式的排序。
    quick_style
        如果这个样式显示在样式库中则为True，如果该样式在隐藏时应该显示在样式库中，则为False。读/写布尔值。
    unhide_when_used
        如果应用程序在下一次应用于内容时应该使该样式可见，则为True。否则False。
        请注意，当将python-docx应用于内容时，它不会自动地为该属性打开具有True的样式。
```

#### \_NumberingStyle 对象

```python
class docx.styles.style._NumberingStyle
    编号样式。没有实现。
```

#### LatentStyles objects

```python
class docx.styles.latent.LatentStyles
    提供对本文档中隐式样式的默认行为和_LatentStyle对象集合的访问，这些对象为特定的指定隐式样式定义这些缺省值的覆盖。

    add_latent_style(name)
        返回一个新添加的_LatentStyle对象，以覆盖这个潜在样式对象中为具有名称的内置样式定义的继承默认值。
    default_priority
        0到99之间的整数，指定样式列表和样式库中潜在样式的默认排序顺序。
        如果没有赋值，则为None，这将导致Word使用默认值99。
    default_to_hidden
        布尔值指定是否隐藏隐式样式的默认行为。隐式样式不会出现在推荐列表或样式库中。
    default_to_locked
        布尔值指定是否锁定潜在样式的默认行为。锁定样式不会出现在样式面板或样式库中，也不能应用于文档内容。
        只有在打开文档的格式保护时(通过Developer菜单)，该行为才会激活。
    default_to_quick_style
        布尔值指定隐藏样式的默认行为是否在不隐藏时出现在样式库中。
    default_to_unhide_when_used
        布尔值指定隐藏样式的默认行为是否在首次应用于内容时不隐藏。
    element
        通过这个对象代理lxml
    load_count
        指定要初始化到这个LatentStyles对象中指定的默认值的内置样式的数量。
        如果XML中没有设置(非常少见)，则没有设置。默认的Word 2011模板将该值设置为276，这是Word 2010中的内置样式。
```

#### \_LatentStyle objects

```python
class docx.styles.latent._LatentStyle
    w:lsdException元素的代理，当样式中尚未存储该样式的定义时，该元素指定内置样式的显示行为。
    style.xml的一部分。这个元素中的值覆盖了父w:latentStyles元素中指定的默认值。

    delete()
        删除这种潜在的样式定义，以便在包含LatentStyles对象中定义的默认值为其每个属性提供有效值。
        在调用此方法后试图访问此对象上的任何属性将引发AttributeError。
    element
        通过这个对象代理lxml
    hidden
        三态值，指定是否在推荐列表中显示这种隐式样式。
        没有一个表示有效值继承自父元素<w:latentstyles>
    locked
        三态值，指定这种隐式样式是否锁定。
        锁定样式不会出现在样式面板或样式库中，也不能应用于文档内容。
        只有在打开文档的格式保护时(通过Developer菜单)，该行为才会激活。
    name
        此异常应用于的内置样式的名称。
    priority
        整数排序键用于UI中这种隐式样式。
    quick_style
        三态值，指定当不隐藏时，这种潜在样式是否应该出现在样式库中。
        没有一个表示有效值应该从其父LatentStyles对象的默认值继承。
    unhide_when_used
        在下次将样式应用于内容时，指定该样式是否应该将其隐藏属性设置为False。
        None表示有效值应该继承自其父LatentStyles对象指定的默认值。
```

### 文本相关对象

#### Paragraph 对象

```python
class docx.text.paragraph.Paragraph
    代理对象包装元素

    add_run(text=None, style=None)
        在包含文本并具有由样式ID样式标识的字符样式的段落中追加一个run。
        文本可以包含制表符(\t)字符，这些字符被转换为制表符的适当XML格式。
        文本还可以包括换行符(\n)或回车符(\r)，每个换行符都被转换为换行符。
    alignment
        WD_PARAGRAPH_ALIGNMENT枚举变量成员，指定了这段的对齐设置。
        None值表示段落没有直接应用的对齐值，并将从其样式层次结构继承其对齐值。
        将None赋给此属性会删除任何直接应用的对齐值。
    clear()
        删除所有内容后返回相同的段落。段落级别的格式，比如样式，被保留了下来。
    insert_paragraph_before(text=None, style=None)
        返回一个新创建的段落，直接插入到这段前面。如果提供了文本，新段落将在一次运行中包含该文本。
        如果提供了样式，则将该样式分配给新段落。
    paragraph_format
        段落格式对象提供对段落格式属性的访问，例如行间距和缩进。
    runs
        本段中元素对应的运行实例序列。
    style
        读/写。_ParagraphStyle对象，表示分配给这段的样式。如果没有为该段落指定显式样式，则其值为文档的默认段落样式。
        可以用段落样式名称代替段落样式对象。分配None会移除任何应用的样式，使其有效值成为文档的默认段落样式。
    text
        连接段落中每个运行的文本而形成的字符串。XML中的制表符和换行符分别映射到\t和\n字符。
        将文本分配给此属性将导致将所有现有的段落内容替换为包含指定文本的单个运行。
        文本中的t字符映射到元素，每个\n或\r字符映射到换行符。
        段落级别的格式，比如样式，被保留了下来。所有运行级格式(如粗体或斜体)都被删除。
```

#### ParagraphFormat objects

```python
class docx.text.parfmt.ParagraphFormat
    提供对段落格式的访问，如对齐、缩进、行间距、前后缩进以孤行控制。

    alignment
        WD_PARAGRAPH_ALIGNMENT枚举变量成员，指定了这段的对齐设置。
        None值表示段落对齐是从样式层次结构继承而来的。
    first_line_indent
        指定段落第一行缩进的相对差异的长度值。一个正数会使第一行缩进。
        一个负数产生一个挂起缩进。None第一行缩进是从样式层次结构继承的。
    keep_together
        如果段落应该保持“完整”，并且在呈现文档时不跨页边界，则为True。
        None它的有效值是从样式层次结构继承的。
    keep_with_next
        如果该段落在呈现文档时应与随后的段落保持在同一页上，则为True。
        例如，此属性可用于将一个章节标题保持在与第一段相同的页面上。
        None它的有效值是从样式层次结构继承的。
    left_indent
        长度值，指定段落左侧空白处和左侧空白处之间的空间。
        None个表示左缩进值是从样式层次结构继承的。
        使用英寸值对象作为以英寸为单位应用缩进的方便方法。
    line_spacing
        float或Length，指定段落连续行中基线之间的空间。
        None值表示从样式层次结构继承行间距。
        浮动值，例如2.0或1.75，表示行距为线高的倍数。
        Lenght如Pt(12)表示间距是固定高度。
        Pt值类是在点的单位中应用行间距的一种方便方法。
        分配None会重置从样式层次结构继承的行间距。
    line_spacing_rule
        WD_LINE_SPACING枚举的一个成员，指示应该如何解释line_space的值。
        将任何WD_LINE_SPACING成员赋值为SINGLE、DOUBLE或ONE_POINT_FIVE都会导致line_space的值被更新，以产生相应的行间距。
    page_break_before
        如果段落应该出现在前面段落后面的页面顶部，则为True。None指出它的有效值是从样式层次结构继承的。
    right_indent
        Length，指定段落右侧和右侧之间的空间。None表示右缩进值是从样式层次结构继承的。
        使用Cm值对象作为一种方便的方法来应用以厘米为单位的缩进。
    space_after
        长度值，指定该段落与后续段落之间出现的间距。None表示这个值是从样式层次结构继承的。
        长度对象提供了方便的属性，例如pt和inch，允许轻松转换到各种长度单位。
    space_before
        长度值，指定在该段和前段之间出现的间距。None表示这个值是从样式层次结构继承的。
        Length对象提供了方便的属性，例如pt和cm，可以方便地转换到各种长度单位。
    tab_stops
        TabStops对象提供对为这种段落格式定义的选项卡停止的访问。
    widow_control
        如果一段中的第一行和最后一行与另一段保持在同一页上，则当单词重新标记文档时为True。
        None它的有效值是从样式层次结构继承的。
```

#### Run objects

```python
class docx.text.run.Run
    代理对象包装元素。运行中的一些属性接受三态值，True、False或None。
    True与False分别对应开关。False表示属性没有在运行中直接指定，它的有效值是从样式层次结构中获取的。

    add_break(break_type=6)
        在run添加break_type的break元素。
        break_type可以获取WD_BREAK.LINE，WD_BREAK.PAGE,WD_BREAK.COLUMN在docx.enum.text中导入WD_BREAK时。
        break_type默认为WD_BREAK.LINE。
    add_picture(image_path_or_stream, width=None, height=None)
        返回一个InlineShape实例，该实例包含image_path_or_stream标识的图像，并添加到运行的末尾。
        image_path_or_stream可以是路径(字符串)或包含二进制图像的类文件对象。
        如果既没有指定宽度也没有指定高度，则图像将以其实际大小显示。
        如果只指定了一个，则使用它来计算一个缩放因子，然后应用于未指定的维数，以保持图像的长宽比。
        图的本机大小使用图像文件中指定的点每英寸(dpi)值计算，如果没有指定值，默认为72 dpi，yiban情况下是这样的。
    add_tab()
        在run的末尾添加一个的元素，在Word中解释为一个制表符。
    add_text(text)
        将一个新添加的_Text对象(对应于一个新的子元素)返回到包含文本的run。
        与为运行分配文本给Run.text相比这一方法可能更加友好。
    bold
        使运行里面的文本以粗体显示。
    font
        Font对象提供对此运行的字符格式属性(如字体名称和大小)的访问。
    italic
        读/写。三态值。当为True时，将导致运行的文本以斜体显示。
    style
        读/写。一个_CharacterStyle对象，表示应用于此运行的字符样式。
        如果运行没有直接应用的字符样式，则返回文档的默认字符样式(通常是默认字符字体)。
        将此属性设置为None会删除任何直接应用的字符样式。
    text
        通过将每个run content子元素的文本等效连接到Python字符串而形成的字符串。
        每个元素添加它所包含的文本字符。元素添加了一个\t字符。一个或元素每个添加一个\n字符。
        注意，元素可以指示分页符或列分隔符以及行分隔符。所有元素都转换为一个\n字符，不管它们的类型如何。所有其他内容子元素，如，都被忽略。
        将文本赋给此属性会产生相反的效果，将每个\t字符转换为元素，将每个\n或\r字符转换为元素。任何现有的运行内容都将被替换。运行格式保持不变。
    underline
        Run的下划线样式，可以是一个为None、True、False或WD_UNDERLINE的值。
        None值表示运行没有直接应用的下划线样式，因此将继承包含段落的下划线值。
        将None赋给此属性会删除任何直接应用的下划线值。
        False值表示没有下划线的直接应用的设置，覆盖任何继承值。
        True值表示单下划线。
        WD_UNDERLINE的值用来指定其他的轮廓样式，比如double、wavy和点星型。
```

#### Font对象

```python
class docx.text.run.Font
    代理对象封装元素的父元素，并提供对字符属性(如字体名称、字体大小、粗体和下标)的访问。

    all_caps
        读/写. 使此字体中的文本以大写字母显示。
    bold
        读/写。使此文本内容以粗体显示。
    color
        一个ColorFormat对象，提供了一种获取和设置该字体文本颜色的方法。
    complex_script
        读写三态值。如果为True，则将运行中的字符视为复杂的脚本，而不考虑其Unicode值。
    cs_bold
        读/写三态值。当为True时，将使运行中的复杂脚本字符以粗体显示。
    cs_italic
        读/写三态值。当为True时，将使运行中的复杂脚本字符以斜体显示。
    double_strike
        读/写三态值。当为True时，将使运行中的文本以双删除线贯穿显示。
    emboss
        读/写三态值。当为True时，将使运行中的文本显示为凸起的页面。
    hidden
        读/写三态值。当为True时，将导致run中的文本隐藏不显示，除非应用程序设置强制显示隐藏文本。
    highlight_color
        WD_COLOR_INDEX的一个成员，指示应用了高亮显示的颜色，如果没有应用高亮显示，则为空。
    imprint
        读写三态值。当为True时，将使运行中的文本显示为压入页面的状态。
    italic
        读/写三态值。当为True时，将导致Run的文本以斜体显示。None表示有效值是从样式层次结构继承的。
    math
        读/写三态值。当为True时，指定此运行包含的WML应该像Office Open XML Math一样处理。
    name
        获取或设置此字体实例的字体名称，如果找到匹配的字体，则使其控制的文本出现在指定的字体中。
        None表示字体是从样式层次结构继承的。
    no_proof
        读/写三态值。当为True时，指定在扫描文档以查找拼写和语法时，此运行的内容不应报告任何错误。
    outline
        读/写三态值。当True使运行中的字符看起来好像有一个轮廓，通过在每个字符符号的内外边界上绘制一个像素宽的边框。
    rtl
        读/写三态值。当True使运行中的文本具有从右到左的特征时。
    shadow
        读/写三态值。当True使运行中的文本显示为每个字符都有阴影时。
    size
        读/写长度值或None，以英文单位(EMU)表示字体高度。None表字体大小应该从样式层次结构继承。
        Length是int的子类，具有方便转换为点或其他长度单位的属性。
        docx.shared.Pt类允许方便的点值规范:
            >> font.size = Pt(24)
            >> font.size
            304800
            >> font.size.pt
            24.0
    small_caps
        读/写三态值。当True时，运行中的小写字符显示为大写字母，比为运行指定的字体大小小两个点。
    snap_to_grid
        读/写三态值。当True使运行在布局此运行中的字符时，在FdocGrid元素中定义的每行设置中使用文档网格字符。
    spec_vanish
        读/写三态值。当True时，将使运行中的文本以一条横线穿过该行的中心出现。
    subscript
        :布尔值，指示此字体中的字符是否显示为下标。None下标/下标值是从样式层次结构继承的。

    superscript
        布尔值，指示此字体中的字符是否显示为上标。None表示下标/上标值是从样式层次结构继承的。
    underline
        此字体的下划线样式，为None、True、False或WD_UNDERLINE的值之一。
        没有指示字体从样式层次结构继承下划线值。False表示没有下划线。
        True表示单下划线。WD_UNDERLINE的值用来指定其他的轮廓样式，比如double、wavy和dotted。
    web_hidden
        读/写三态值。当为True时，指定在web页面视图中显示文档时，将隐藏该运行的内容。
```

#### TabStop 对象

```python
class docx.text.tabstops.TabStop
    一个单独的标签停止应用于一个段落或样式。使用包含制表位对象的列表语义进行访问。

    alignment
        指定此制表位停止的对齐设置的WD_TAB_ALIGNMENT成员。读/写。
    leader
        WD_TAB_LEADER中的一个成员，指定作为“leader”使用的重复字符，填充此选项卡所跨越的空间。
        分配None会产生与分配wd_tab_leader.space相同的结果。读/写。
    position
        一个长度对象，表示这个制表符从段落内边缘的距离。可能是积极的，也可能是消极的。读/写。
```

#### TabStops 对象

```python
class docx.text.tabstops.TabStops
    一组taosptop卡对象，提供对段落或段落样式的选项卡停止的访问。支持迭代、索引访问、del和len()。
    采用分段格式的tab_stops属性;它不打算直接建造。

    add_tab_stop(position, alignment=WD_TAB_ALIGNMENT.LEFT, leader=WD_TAB_LEADER.SPACES)
        在位置添加一个新的制表符停止，长度对象指定制表符停止相对于段落边缘的位置。
        一个负位置值是有效的，出现在挂起缩进。
        选项卡对齐默认为左侧，但可以通过将WD_TAB_ALIGNMENT枚举的成员作为对齐方式传递来指定。
        可以通过将WD_TAB_LEADER枚举的成员作为leader传递来指定可选的leader字符。
    clear_all()
        移除所有自定义制表位。
```

### 表格对象

```python
class docx.table.Table(tbl, parent)
    一个WordprocessingML elemen的代理类。

    add_column(width)
        返回一个宽度_Column对象，新添加到最右边的表。
    add_row()
        返回一个_Row实例，新添加到表的最底部。
    alignment
        读/写。WD_TABLE_ALIGNMENT或为None，指定该表在页边距之间的位置。
        如果没有指定设置，则会导致从样式层次结构继承有效值。
    autofit
        如果可以自动调整列宽以提高单元格内容的适合度，则为True。
        如果表布局是固定的，则为False。
        如果总列宽度超过页面宽度，则在两种情况下都会调整列宽。读/写布尔。
    cell(row_idx, col_idx)
        返回_Cell实例correponding到row_idx, col_idx交集的表单元格，其中(0,0)是最上面、最左边的单元格。
    column_cells(column_idx)
        表中column_idx列中的单元格序列。
    columns
        表示该表中列序列的_Columns实例。
    row_cells(row_idx)
        该表中row_idx行的单元格序列。
    rows
        包含此表中的行序列的_Rows实例。
    style
        读/写。表示应用于该表的样式的_TableStyle对象。
        如果表没有直接应用的样式，则返回文档的默认表样式(通常是普通表)。
        将None赋给此属性会删除任何直接应用的表样式，导致它继承文档的默认表样式。
        注意，表样式的样式名称与用户界面中显示的样式略有不同;连字符，如果出现，必须删除。
    table_direction
        WD_TABLE_DIRECTION中的一个成员，指示表单元格排列的方向，例如WD_TABLE_DIRECTION.LTR。
        没有一个表示值是从样式层次结构继承的。
```

#### \_Cell对象

```python
class docx.table._Cell(tc, parent)
    表格里的单元格

    add_paragraph(text=u'', style=None)
        回在单元格中内容末尾新添加的段落。如果出现，文本将在一次运行中添加到段落中。
        如果指定，则应用段落样式。如果没有指定或没有指定样式，结果就好像应用了“普通”样式。
        注意，单元格中的文本格式可能会受到表样式的影响。文本可以包含制表符(\t)字符，这些字符被转换为制表符的适当XML格式。
        文本还可以包括换行符(\n)或回车符(\r)，每个换行符都被转换为换行符。
    add_table(rows, cols)
        在现有单元格内容之后返回新添加到此单元格的表，其中包含行rows和cols列。
        在表后添加一个空段落，因为Word需要段落元素作为每个单元格中的最后一个元素。
    merge(other_cell)
        返回一个合并的单元格，该单元格是通过将此单元格和other_cell作为对角线跨越矩形区域而创建的。
        如果单元格没有定义一个矩形区域，就会引发InvalidSpanError。
    paragraphs
        单元格中的段落列表。表单元格需要包含至少一个块级元素并以段落结尾。
        默认情况下，新单元格包含一个段落。只读
    tables
        单元格中的段落列表。表单元格需要包含至少一个块级元素并以段落结尾。
        默认情况下，新单元格包含一个段落。只读。
    text
        这个单元格的整个内容作为一个文本字符串。
        将字符串赋给此属性将所有现有内容替换为在一次运行中包含指定文本的单个段落。
    vertical_alignment
        WD_CELL_VERTICAL_ALIGNMENT或None。
        None值表示该单元格的垂直对齐是继承的。分配None会导致删除任何明确定义的垂直对齐，从而恢复继承。
    width
        在EMU中设置此单元格的宽度，如果没有设置显式宽度，则为None。
```

#### \_Row对象

```python
class docx.table._Row(tr, parent)
    表格的行

    cells
        与这一行中的单元格对应的_Cell实例序列。
    height
        返回一个表示单元格高度的Length对象，如果没有设置显式高度，则返回None。
    height_rule
        作为WD_ROW_HEIGHT_RULE枚举的成员返回该单元格的高度规则，
        如果没有设置显式的height_rule，则返回None。
    table
        引用这一行所属的表对象。
```

#### \_Column objects

```python
class docx.table._Column(gridCol, parent)
    表格的列

    cells
        与此列中的单元格对应的_Cell实例序列。
    table
        引用此列所属的表对象。
    width
        在EMU中设置此列的宽度，如果没有设置显式宽度，则为None。
```

#### \_Rows 对象

```python
class docx.table._Rows(tbl, parent
    与表中的行对应的_Row对象序列。支持len()、迭代、索引访问和切片。

    table
        引用此行集合所属的Table对象
```

#### _Columns 对象

```python
class docx.table._Columns(tbl, parent)
    与表中的列相对应的_Column实例序列。支持len()、迭代和索引访问。

    table
        引用此列集合所属的Table对象。
```

### 章节对象

提供对部分属性(如页边距和页面方向)的访问。

#### Sections对象

```python
class docx.section.Sections(document_elm)
    与文档中的节相对应的节对象序列。支持len()、迭代和索引访问。
```

#### Section对象

```python
class docx.section.Section(sectPr)
    文档部分，提供对部分和页面设置设置的访问。

    bottom_margin
        Length对象，表示本节中所有页的底部空白，单位为英文公制单位。
    footer_distance
        Length对象，表示从页面底部边缘到页脚底部边缘的距离。如果XML中没有设置，则为None。
    gutter
        Length对象，表示本节中所有页的页槽大小(以英文公制单位表示)。页边距是在内页边距上增加的额外间距，以确保页边距均匀。
    header_distance
        Length对象，表示从页面顶部边缘到页眉顶部边缘的距离。如果XML中没有设置，则为None。
    left_margin
        Length对象，表示本节中所有页的左边空白处，单位为英文公制单位。
    orientation
        指定此部分的页面方向的WD_ORIENTATION成员，是WD_ORIENT.PORTRAIT或WD_ORIENT.LANDSCAPE。
    page_height
        本节使用的总页面高度，包括所有的边缘间距值，如页边距。考虑到页面方向，例如，当方向是横向的时候，它的预期值是英寸(8.5)。
    page_width
        本节使用的总页面宽度，包括所有的边间距值，如边距。考虑到页面方向，例如，当方向是横向时，字体大小的纸张的预期值为英寸(11)。
    right_margin
        Length对象，表示本节中所有页的右边距，单位为英文公制单位。
    start_type
        WD_SECTION_START枚举的成员对应于此部分的初始中断行为，例如WD_SECTION。如果部分应该从下一个奇数页开始，则为奇数页。
    top_margin
        Length对象，表示本节中所有页的顶部空白，单位为英文公制单位。
```

### Shape-related 对象

#### InlineShapes 对象

```python
class docx.shape.InlineShapes(body_elm, parent)
    InlineShape实例序列，支持len()、迭代和索引访问。
```

#### InlineShape 对象

`InlineShape`的`width`和`height`属性提供了一个`length`对象，它是`length`的实例。这些实例的行为像`int`，但也有内置单元转换属性，例如:

```python
>>> inline_shape.height
914400
>>> inline_shape.height.inches
1.0
```

```python
class docx.shape.InlineShape(inline)
    一个元素的代理，表示一个内联图形对象的容器

    height
        读/写。这个内联形状作为Emu实例的显示高度。
    type
        此内联图形作为docx.enum.shape.WD_INLINE_SHAP枚举的成员，例如LINKED_PICTURE,只读。
    width
        读/写。这个内联形状作为Emu实例的显示宽度。
```

### DrawingML 对象

低级的绘图元素，如出现在各种文档上下文中的颜色。

#### ColorFormat对象

```python
class docx.dml.color.ColorFormat
    提供对颜色设置的访问，例如RGB颜色、主题颜色和亮度调整。

    rgb
        如果没有指定RGB颜色，则为RGBColor值或None。
        当type为MSO_COLOR_TYPE.RGB时，这个属性的值总是一个RGBColor值。
        如果type是MSO_COLOR_TYPE.THEME，它也可能是RGBColor值。就像Word在指定主题颜色时写入当前值一样。
        在这种情况下，RGB值应该被解释为仅仅是一个好的猜测，因为主题颜色在呈现时优先。
        当type为None或MSO_COLOR_TYPE.AUTO时，其值为None。
        指定RGBColor值yiji将使type变为MSO_COLOR_TYPE.RGB。分配`None``会导致没有任何颜色，从而从样式层次结构继承有效颜色。
    theme_color
        MSO_THEME_COLOR_INDEX的成员，如果没有指定主题颜色，则为None。
        当type为MSO_COLOR_TYPE.THEME时。这个属性的值总是MSO_THEME_COLOR_INDEX的成员。当类型有任何其他值时，此属性的值为None。
        分配MSO_THEME_COLOR_INDEX的成员会使type变成MSO_COLOR_TYPE.THEME。
        任何现有的RGB值都被保留，但被Word忽略。
        分配None会导致删除所有颜色规范，从而从样式层次结构继承有效的颜色。
    type
        只读的。MSO_COLOR_TYPE (RGB、THEME或AUTO中的一个)的成员，对应于该颜色的定义方式。
        如果在此级别没有应用颜色，则其值为None，这将导致有效颜色从样式层次结构继承。
```

### Shared classes

### Length 对象

`python-docx`中的长度值表示为标准长度值对象。`Length`是`int`的子类，具有`int`的所有行为。

```python
>>> inline_shape.height
914400
>>> inline_shape.height.inches
1.0
```

`Length对象`是使用一系列方便的构造函数来构造的，允许在最适合上下文的单元中表示值。

```python
class docx.shared.Length
    长度构造函数类的基类:英寸、厘米、毫米、Px和Emu。作为英制公制单位的int计数，914,400到英寸，36,000到毫米。以只读属性的形式提供方便的单位转换方法。不可变的。

    cm
        以厘米表示的等效长度(浮点数)。
    emu
        用英制单位(int)表示的等效长度。
    inches
        以英寸表示的等效长度(浮点数)。
    mm
        以毫米表示的等效长度(浮点数)。
    pt
        浮点数的长度
    twips
        以twips (int)表示的等效长度。

class docx.shared.Inches
    长度(英寸)的构造函数，例如width = Inches(0.5)。

class docx.shared.Cm
    方便的构造函数长度以厘米为单位,例如：height = Cm(12)

class docx.shared.Mm
    长度单位为毫米的方便构造函数，例如width = Mm(240.5)。

class docx.shared.Pt
    用于在点中指定长度的类

class docx.shared.Twips
    长度的方便构造函数，例如width = Twips(42)。twip是0.20,635 EMU。

class docx.shared.Emu
    长度的构造函数，用英文公制单位表示，例如width = Emu(457200)。
```

#### RGBColor 对象

```python
class docx.shared.RGBColor(r, g, b)
    定义特定RGB颜色的不可变值对象。、
    r、g和b都是0-255范围内的整数。使用h十六进制表示法(例如0x42)可以增强可读性，在使用十六进制RGB值时:

    >>> lavender = RGBColor(0xff, 0x99, 0xcc)
    
    @classmethod
    from_string(rgb_hex_str)
        从RGB颜色十六进制字符串返回一个新实例，比如'3C2F80'
```

### 枚举量

在这里可以找到用于python-docx属性设置的各种枚举文档:

#### MSO_COLOR_TYPE

指定颜色规格方案, 例子：

```python
from docx.enum.dml import MSO_COLOR_TYPE
assert font.color.type == MSO_COLOR_TYPE.THEME
```

* **RGB**: 颜色由RGBColor值指定。
* **THEME**: 颜色是预设的主题颜色之一。
* **AUTO**: 颜色是自动确定的应用程序。

#### MSO_THEME_COLOR_INDEX

表示Office主题颜色，即格式色带上的颜色画廊中显示的颜色之一。

别名:MSO_THEME_COLOR

实例：

```python
from docx.enum.dml import MSO_THEME_COLOR
font.color.theme_color = MSO_THEME_COLOR.ACCENT_1
```

* **NOT_THEME_COLOR**: 表示没有主题颜色
* **ACCENT_1**: 指定ACCENT_1为主题颜色。
* **ACCENT_2**: 指定ACCENT_2为主题颜色。
* **ACCENT_3**: 指定ACCENT_3为主题颜色。
* **ACCENT_4**: 指定ACCENT_4为主题颜色。
* **ACCENT_5**: 指定ACCENT_5为主题颜色。
* **ACCENT_6**: 指定ACCENT_6为主题颜色。
* **BACKGROUND_1**: 指定背景1的主题颜色。
* **BACKGROUND_1**: 指定背景2的主题颜色。
* **DARK_1**: 指定Drak1为主题颜色.
* **DRAK_2**: 指定Drak2为主题颜色
* **FOLLOWED_HYPERLINK**: 指定被单击超链接的主题颜色。
* **HYPERLINK**: 指定超链接的主题颜色。
* **LIGHT_1**: 指定Light 1主题颜色。
* **LIGHT_2**: 指定Light 2主题颜色。
* **TEXT_1**: 指定文本1的主题颜色。
* **TEXT_2**: 指定文本2的主题颜色。
* **MIXED**: 表示使用了多种主题颜色。

#### WD_PARAGRAPH_ALIGNMENT

别名：WD_ALIGN_PARAGRAPH
指定段落对齐类型。
例子：

```python
from docx.enum.text import WD_ALIGN_PARAGRAPH

paragraph = document.add_paragraph()
paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
```

* **LEFT**: 左对齐
* **CENTER**: 居中
* **RIGHT**: 右对齐。
* **JUSTIFY**: xx
* **DISTRIBUTE**: 段落字符被分配以填充整个段落的宽度。
* **JUSTIFY_MED**: 用中等字符压缩比证明。
* **JUSTIFY_HI**: 具有高字符压缩比。
* **JUSTIFY_LOW**: 用低字符压缩比证明。
* **THAI_JUSTIFY**: 根据泰国格式布局对齐。

#### WD_BUILTIN_STYLE

别名: WD_STYLE
指定内置的`Microsoft Word样式`。
例子：

```python
from docx import Document
from docx.enum.style import WD_STYLE

document = Document()
styles = document.styles
style = styles[WD_STYLE.BODY_TEXT]
```

* **BLOCK_QUOTATION**: 块文本
* **BODY_TEXT**: 主体文本
* **BODY_TEXT_2**: 主体文本2
* **BODY_TEXT_3**: 主体文本3
* **BODY_TEXT_FIRST_INDENT**: 正文文本首行缩进
* **BODY_TEXT_FIRST_INDENT_2**: 正文文本首行缩进
* **BODY_TEXT_INDENT**: 正文文本缩进
* **BODY_TEXT_INDENT_2**: 正文文本缩进2
* **BODY_TEXT_INDENT_3**: 正文文本缩进3
* **BOOK_TITLE**: 文章名
* **CAPTION**: 标题
* **CLOSING**: 关闭
* **COMMENT_REFERENCE**: 评论参考
* **COMMENT_TEXT**: 批注文本。
* **DATE**: 日期
* **DEFAULT_PARAGRAPH_FONT**: 默认段落字体。
* **EMPHASIS**: 强调
* **ENDNOTE_REFERENCE**: 尾注引用。
* **ENDNOTE_TEXT**: 尾注的文本。
* **ENVELOPE_ADDRESS**: 信封地址。
* **ENVELOPE_RETURN**: 返回一个信封对象
* **FOOTER**: 页脚。
* **FOOTNOTE_REFERENCE**: 脚注引用
* **FOOTNOTE_TEXT**: 脚注文本
* **HEADER**: 头
* **HEADING_1**: 标题1。
* **HEADING_2**: 标题2。
* **HEADING_3**: 标题3。
* **HEADING_4**: 标题4。
* **HEADING_5**: 标题5
* **HEADING_6**: 标题6
* **HEADING_7**: 标题7
* **HEADING_8**: 标题8
* **HEADING_9**: 标题9
* **HTML_ACRONYM**: HTML缩略词。
* **HTML_ADDRESS**: HTML的地址。
* **HTML_CITE**: HTML引用。
* **HTML_CODE**: HTML代码
* **HTML_DFN**: HTML定义。
* **HTML_KBD**: HTML 快捷键。
* **HTML_NORMAL**: 正常(网络)。
* **HTML_PRE**: HTML格式化。
* **HTML_SAMP**: HTML示例。
* **HTML_TT**: HTML字体。
* **HTML_VAR**: HTML变量。
* **HYPERLINK**: 超链接
* **HYPERLINK_FOLLOWED**: 跟踪超链接
* **INDEX_1**: 目录1
* **INDEX_2**: 目录2
* **INDEX_3**: 目录3
* **INDEX_4**: 目录4
* **INDEX_5**: 目录5
* **INDEX_6**: 目录6
* **INDEX_7**: 目录7
* **INDEX_8**: 目录8
* **INDEX_9**: 目录9
* **INDEX_HEADING**: 目录标题
* **INTENSE_EMPHASIS**: 强烈的强调。
* **INTENSE_QUOTE**: 强调引用。
* **INTENSE_REFERENCE**: 强调的参考。
* **LINE_NUMBER**: 行号。
* **LIST**: 列表
* **LIST_2**: 列表2
* **LIST_3**: 列表3
* **LIST_4**: 列表4
* **LIST_5**: 列表5
* **LIST_BULLET**: 符号列表
* **LIST_BULLET_2**: 符号列表2
* **LIST_BULLET_3**: 符号列表3
* **LIST_BULLET_4**: 符号列表4
* **LIST_BULLET_5**: 符号列表5
* **LIST_CONTINUE**: List Continue.
* **LIST_CONTINUE_2**: List Continue 2.
* **LIST_CONTINUE_3**: List Continue 3.
* **LIST_CONTINUE_4**: List Continue 4.
* **LIST_CONTINUE_5**: List Continue 5.
* **LIST_NUMBER**: List Number.
* **LIST_NUMBER_2**: List Number 2.
* **LIST_NUMBER_3**: List Number 3.
* **LIST_NUMBER_4**: List Number 4.
* **LIST_NUMBER_5**: List Number 5.
* **LIST_PARAGRAPH**: List 段落
* **MACRO_TEXT**: 宏观文本
* **MESSAGE_HEADER**: 消息标题
* **NAV_PANE**: Document Map.
* **NORMAL**: 正常
* **NORMAL_INDENT**: 正常缩进
* **NORMAL_OBJECT**: 正常对象
* **NORMAL_TABLE**: 普通(应用于表中)。
* **NOTE_HEADING**: 请注意标题。
* **PAGE_NUMBER**: 页码。
* **PLAIN_TEXT**: 纯文本。
* **QUOTE**: 引用
* **SALUTATION**: 问候。
* **SIGNATURE**: 签名。
* **STRONG**: 强大。
* **SUBTITLE**: 副标题。
* **SUBTLE_EMPHASIS**: 次要重点
* **SUBTLE_REFERENCE**: 次要参考
* **TABLE_COLORFUL_GRID**: 多色彩网格边框
* **TABLE_COLORFUL_LIST**: 多色彩列表
* **TABLE_COLORFUL_SHADING**: 彩色的阴影。
* **TABLE_DARK_LIST**: 暗色列表
* **TABLE_LIGHT_GRID**: 亮色表格边框
* **TABLE_LIGHT_GRID_ACCENT_1**: 光网格重音1。
* **TABLE_LIGHT_LIST**: 亮色表格
* **TABLE_LIGHT_LIST_ACCENT_1**: Light List Accent 1.
* **TABLE_LIGHT_SHADING**: 光的阴影。
* **TABLE_LIGHT_SHADING_ACCENT_1**: 浅阴影重音1。
* **TABLE_MEDIUM_GRID_1**: 中等宽度边框。
* **TABLE_MEDIUM_GRID_2**: 中等宽度边框2
* **TABLE_MEDIUM_GRID_3**: 中等宽度边框3
* **TABLE_MEDIUM_LIST_1**: 中等宽度表格列表1所示。
* **TABLE_MEDIUM_LIST_1_ACCENT_1**: Medium List 1 Accent 1.
* **TABLE_MEDIUM_LIST_2**: 中等 List 2.
* **TABLE_MEDIUM_SHADING_1**: Medium Shading 1.
* **TABLE_MEDIUM_SHADING_1_ACCENT_1**: Medium Shading 1 Accent 1.
* **TABLE_MEDIUM_SHADING_2**: Medium Shading 2.
* **TABLE_MEDIUM_SHADING_2_ACCENT_1**: Medium Shading 2 Accent 1.
* **TABLE_OF_AUTHORITIES**: Table of Authorities.
* **TABLE_OF_FIGURES**: 数据表
* **TITLE**: 题目
* **TOAHEADING**: TOA标题。
* **TOC_1**: TOC 1.
* **TOC_2**: TOC 2.
* **TOC_3**: TOC 3.
* **TOC_4**: TOC 4.
* **TOC_5**: TOC 5.
* **TOC_6**: TOC 6.
* **TOC_7**: TOC 7.
* **TOC_8**: TOC 8.
* **TOC_9**: TOC 9.

#### WD_CELL_VERTICAL_ALIGNMENT

别名：WD_ALIGN_VERTICAL
指定表的一个或多个单元格中文本的垂直对齐方式。
实例:

```python
from docx.enum.table import WD_ALIGN_VERTICAL

table = document.add_table(3, 3)
table.cell(0, 0).vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
```

* **TOP**: 文本对齐到单元格的顶部边框。
* **CENTER**: 文本对齐单元格的中心。
* **BOTTOM**: 文本对齐单元格的底部。
* **BOTH**: 这是OpenXml规范中的一个选项，但不是`Word`本身。目前还不清楚这种设置会产生什么样的文字行为。如果你发现了请让我们知道，我们将更新这个文件。否则，最好避免这种选择。

#### WD_COLOR_INDEX

别名：WD_COLOR
指定要应用的标准预设颜色。用于字体高亮显示和其他应用程序。

* **AUTO**: 自动颜色，默认通常是黑色。
* **BLACK**: 黑色
* **BRIGHT_GREEN**: 亮绿色
* **DARK_BLUE**: 暗蓝色
* **DARK_RED**: 暗红色
* **DARK_YELLOW**: 暗黄色
* **GRAY_25**: 25%深浅的灰色。
* **GRAY_50**: 50%深浅的灰色。
* **GREEN**: 绿色
* **PINK**: 粉色。
* **RED**: 红色。
* **TEAL**: Teal颜色。
* **TURQUOISE**: 湖色 color。
* **VIOLET**: 紫罗兰色的。
* **WHITE**: 白色。
* **YELLOW**: 黄色。

#### WD_LINE_SPACING

指定要应用于段落的行间距格式。

实例:

```python
from docx.enum.text import WD_LINE_SPACING

paragraph = document.add_paragraph()
paragraph.line_spacing_rule = WD_LINE_SPACING.EXACTLY
```

* **ONE_POINT_FIVE**: Space-and-a-half行间距。
* **AT_LEAST**: 行间距总是至少指定的数量。金额是单独指定的。
* **DOUBLE**: 双倍空格。
* **EXACTLY**: 行间距正好是规定的量。金额是单独指定的。
* **MULTIPLE**: 线间距指定为线高的倍数。改变字体大小会相应地改变行距。
* **SINGLE**: 单一的间隔(默认)。

#### WD_ORIENTATION

别名： WD_ORIENT
指定页面方向：
实例：

```python
from docx.enum.section import WD_ORIENT

section = document.sections[-1]
section.orientation = WD_ORIENT.LANDSCAPE
```

* **PORTRAIT**: 纵向
* **LANDSCAPE**: 横向。

#### WD_TABLE_ALIGNMENT

指定表对齐类型
实例：

```python
from docx.enum.table import WD_TABLE_ALIGNMENT
table = document.add_table(3, 3)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
```

* **LEFT**: 左对齐
* **CENTER**: 中间对齐
* **RIGHT**: 右对齐

#### WD_ROW_HEIGHT_RULE

别名：WD_ROW_HEIGHT
指定确定表行高度的规则
实例：

```python
from docx.enum.table import WD_ROW_HEIGHT_RULE

table = document.add_table(3, 3)
table.rows[0].height_rule = WD_ROW_HEIGHT_RULE.EXACTLY
```

* **AUTO**: 调整行高度以适应行的最高值。

* **AT_LEAST**: 行高度至少是指定的最小值。

* **EXACTLY**: 行高度是一个精确的值。

#### WD_SECTION_START

别名：WD_SECTION指定段中断的开始类型。
实例：

```python
from docx.enum.section import WD_SECTION

section = document.sections[0]
section.start_type = WD_SECTION.NEW_PAG
```

* **CONTINUOUS**: 连续的部分。
* **NEW_COLUMN**: 新的列中断。
* **NEW_PAGE**: 新页段中断。
* **EVEN_PAGE**: 偶数页分段。
* **ODD_PAGE**: 新章节从下一页开始

#### WD_STYLE_TYPE

指定四种样式类型之一:段落、字符、列表或表。
实例：

```python
from docx import Document
from docx.enum.style import WD_STYLE_TYPE

styles = Document().styles
assert styles[0].type == WD_STYLE_TYPE.PARAGRAPH
```

* **CHARACTER**: 字符样式。
* **LIST**: 列表样式
* **PARAGRAPH**: 段落样式
* **TABLE**: 表样式

#### WD_TAB_ALIGNMENT

指定要应用的制表符对齐方式。

* **LEFT**: 左对齐
* **CENTER**: 中心对齐
* **RIGHT**: 右对齐
* **DECIMAL**: Decimal-aligned.
* **BAR**: Bar-aligned.
* **LIST**: List-aligned. (deprecated)
* **CLEAR**: 清除继承的制表符.
* **END**: 右对齐 (弃用)
* **NUM**: 左对齐 (弃用)
* **START**: 左对齐. (弃用)

#### WD_TAB_LEADER

指定要用作带格式化选项卡的标题的字符。

* **SPACES**: 默认空格
* **DOTS**: 点
* **DASHES**: 破折号。
* **LINES**: 双行
* **HEAVY**: 一个加粗线。
* **MIDDLE_DOT**: 垂直。

#### WD_TABLE_DIRECTION

指定应用程序在指定表或行中对单元格进行排序的方向。
实例：

```python
from docx.enum.table import WD_TABLE_DIRECTION

table = document.add_table(3, 3)
table.direction = WD_TABLE_DIRECTION.RTL
```

* **LTR**: 表或行与第一列排列在最左边的位置。
* **RTL**: 表或行与第一列排列在最右边的位置。

#### WD_UNDERLINE

指定应用于一系列字符的下划线的样式

* **NOTE**: 没有下划线。此设置覆盖所有继承的下划线值，因此可用于从从其包含段落中继承下划线的运行中删除下划线。注意，这与为Run.underline分配None不一样。None是一个有效的赋值，但会导致运行继承其下划线值。分配WD_UNDERLINE。没有人会无条件地关闭下划线。
* **SINGL**: 一行。注意，此设置是只写的，因为在运行时使用此设置会返回True(而不是WD_UNDERLINE.SINGLE)。
* **WORDS**: 只在单个字下面加划线。
* **DOUBLE**: 一个双下划线
* **DOTTED**: 点
* **THICK**: 一个单行细线
* **DASH**: 破折号
* **DOT_DASH**: 交替点和破折号。
* **DOT_DOT_DASH**: 一种交替的点-点-划模式。
* **WAVY**: 一条波浪线。
* **DOTTED_HEAVY**: 加粗的点。
* **DASH_HEAVY**: 加粗的破折号。
* **DOT_DASH_HEAVY**: 交替使用加粗点和加粗线。
* **DOT_DOT_DASH_HEAVY**: 一种交替的重点-点-划模式。
* **WAVY_HEAVY**: 一条加粗的波浪线。
* **DASH_LONG**: 长破折号。
* **WAVY_DOUBLE**: 双波浪线。
* **DASH_LONG_HEAVY**: 长加粗破折号。

## python-docx源代码

```python
# encoding: utf-8
"""
|Document| and closely related objects
"""
from __future__ import (
    absolute_import, division, print_function, unicode_literals
)
from .blkcntnr import BlockItemContainer
from .enum.section import WD_SECTION
from .enum.text import WD_BREAK
from .section import Section, Sections
from .shared import ElementProxy, Emu
[docs]
class Document(ElementProxy):
    """
    WordprocessingML (WML) document. Not intended to be constructed directly.
    Use :func:`docx.Document` to open or create a document.
    """
    __slots__ = ('_part', '__body')
    def __init__(self, element, part):
        super(Document, self).__init__(element)
        self._part = part
        self.__body = None
[docs]
    def add_heading(self, text='', level=1):
        """
        Return a heading paragraph newly added to the end of the document,
        containing *text* and having its paragraph style determined by
        *level*. If *level* is 0, the style is set to `Title`. If *level* is
        1 (or omitted), `Heading 1` is used. Otherwise the style is set to
        `Heading {level}`. Raises |ValueError| if *level* is outside the
        range 0-9.
        """
        if not 0 <= level <= 9:
            raise ValueError("level must be in range 0-9, got %d" % level)
        style = 'Title' if level == 0 else 'Heading %d' % level
        return self.add_paragraph(text, style)
[docs]
    def add_page_break(self):
        """
        Return a paragraph newly added to the end of the document and
        containing only a page break.
        """
        paragraph = self.add_paragraph()
        paragraph.add_run().add_break(WD_BREAK.PAGE)
        return paragraph
[docs]
    def add_paragraph(self, text='', style=None):
        """
        Return a paragraph newly added to the end of the document, populated
        with *text* and having paragraph style *style*. *text* can contain
        tab (``\\t``) characters, which are converted to the appropriate XML
        form for a tab. *text* can also include newline (``\\n``) or carriage
        return (``\\r``) characters, each of which is converted to a line
        break.
        """
        return self._body.add_paragraph(text, style)
[docs]
    def add_picture(self, image_path_or_stream, width=None, height=None):
        """
        Return a new picture shape added in its own paragraph at the end of
        the document. The picture contains the image at
        *image_path_or_stream*, scaled based on *width* and *height*. If
        neither width nor height is specified, the picture appears at its
        native size. If only one is specified, it is used to compute
        a scaling factor that is then applied to the unspecified dimension,
        preserving the aspect ratio of the image. The native size of the
        picture is calculated using the dots-per-inch (dpi) value specified
        in the image file, defaulting to 72 dpi if no value is specified, as
        is often the case.
        """
        run = self.add_paragraph().add_run()
        return run.add_picture(image_path_or_stream, width, height)
[docs]
    def add_section(self, start_type=WD_SECTION.NEW_PAGE):
        """
        Return a |Section| object representing a new section added at the end
        of the document. The optional *start_type* argument must be a member
        of the :ref:`WdSectionStart` enumeration, and defaults to
        ``WD_SECTION.NEW_PAGE`` if not provided.
        """
        new_sectPr = self._element.body.add_section_break()
        new_sectPr.start_type = start_type
        return Section(new_sectPr)
[docs]
    def add_table(self, rows, cols, style=None):
        """
        Add a table having row and column counts of *rows* and *cols*
        respectively and table style of *style*. *style* may be a paragraph
        style object or a paragraph style name. If *style* is |None|, the
        table inherits the default table style of the document.
        """
        table = self._body.add_table(rows, cols, self._block_width)
        table.style = style
        return table
    @property
    def core_properties(self):
        """
        A |CoreProperties| object providing read/write access to the core
        properties of this document.
        """
        return self._part.core_properties
    @property
    def inline_shapes(self):
        """
        An |InlineShapes| object providing access to the inline shapes in
        this document. An inline shape is a graphical object, such as
        a picture, contained in a run of text and behaving like a character
        glyph, being flowed like other text in a paragraph.
        """
        return self._part.inline_shapes
    @property
    def paragraphs(self):
        """
        A list of |Paragraph| instances corresponding to the paragraphs in
        the document, in document order. Note that paragraphs within revision
        marks such as ``<w:ins>`` or ``<w:del>`` do not appear in this list.
        """
        return self._body.paragraphs
    @property
    def part(self):
        """
        The |DocumentPart| object of this document.
        """
        return self._part
[docs]
    def save(self, path_or_stream):
        """
        Save this document to *path_or_stream*, which can be either a path to
        a filesystem location (a string) or a file-like object.
        """
        self._part.save(path_or_stream)
    @property
    def sections(self):
        """
        A |Sections| object providing access to each section in this
        document.
        """
        return Sections(self._element)
    @property
    def settings(self):
        """
        A |Settings| object providing access to the document-level settings
        for this document.
        """
        return self._part.settings
    @property
    def styles(self):
        """
        A |Styles| object providing access to the styles in this document.
        """
        return self._part.styles
    @property
    def tables(self):
        """
        A list of |Table| instances corresponding to the tables in the
        document, in document order. Note that only tables appearing at the
        top level of the document appear in this list; a table nested inside
        a table cell does not appear. A table within revision marks such as
        ``<w:ins>`` or ``<w:del>`` will also not appear in the list.
        """
        return self._body.tables
    @property
    def _block_width(self):
        """
        Return a |Length| object specifying the width of available "writing"
        space between the margins of the last section of this document.
        """
        section = self.sections[-1]
        return Emu(
            section.page_width - section.left_margin - section.right_margin
        )
    @property
    def _body(self):
        """
        The |_Body| instance containing the content for this document.
        """
        if self.__body is None:
            self.__body = _Body(self._element.body, self)
        return self.__body
class _Body(BlockItemContainer):
    """
    Proxy for ``<w:body>`` element in this document, having primarily a
    container role.
    """
    def __init__(self, body_elm, parent):
        super(_Body, self).__init__(body_elm, parent)
        self._body = body_elm
    def clear_content(self):
        """
        Return this |_Body| instance after clearing it of all content.
        Section properties for the main document story, if present, are
        preserved.
        """
        self._body.clear_content()
        return self
```
