# ElasticSearch-DSL包

原文: <https://elasticsearch-dsl.readthedocs.io/en/latest/>{target="_blank"}

摘自: <https://www.cnblogs.com/lit10050528/p/12178822.html>{target="_blank"}

## 简介

elasticsearch-dsl是基于elasticsearch-py封装实现的，提供了更简便的操作elasticsearch的方法。

## 具体使用

elasticsearch的官方文档介绍一共包括六个部分，分别是：**configuration**、**search dsl**、**persistence**、**update by query**、**API document**。

### Configuration

有许多方式可以配置连接，最简单且有效的方式是设置默认连接，该默认连接可以被未传递其他连接的API调用使用。

#### Default connection

默认连接的实现需要使用到`connections.create_connection()`方法。

```python
from elasticsearch_dsl import connections

connections.create_connection(hosts=['localhost'], timeout=20)
```

同时还可以通过alias给连接设置别名，后续可以通过别名来引用该连接，默认别名为`default`

```python
from elasticsearch_dsl import connections

connections.create_connection(alias='my_new_connection', hosts=['localhost'], timeout=60)
```

#### Multiple clusters

可以通过`configure`定义多个指向不同集群的连接。

```python
from elasticsearch_dsl import connections

connections.configure(
    default={'hosts': 'localhost'},
    dev={
        'hosts': ['esdev1.example.com:9200'],
        'sniff_on_start': True
    }
)
```

还可以通过`add_connection`手动添加连接。

##### Using aliases

下面的例子展示了如何使用连接别名。

```python
s = Search(using='qa')
```

#### Manual

如果你不想提供一个全局的连接，你可以通过使用`using`参数传递一个`elasticsearch.Elasticsearch`的实例做为连接，如下：

```python
s = Search(using=Elasticsearch('localhost'))
```

你还可以通过下面的方式来覆盖已经关联的连接。

```python
s = s.using(Elasticsearch('otherhost:9200'))
```

### Search DSL

#### The search object

search对象代表整个搜索请求，包括：`queries`、`filters`、`aggregations`、`sort`、`pagination`、`additional parameters`、`associated client`。

API被设置为可链接的。search对象是不可变的，除了聚合，对对象的所有更改都将导致创建包含该更改的浅表副本。

当初始化Search对象时，你可以传递low-level elasticsearch客户端参数。

```python
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

client = Elasticsearch()

s = Search(using=client)
```

注意

所有的方法都返回一个该对象的拷贝，这样可以保证它被传递给外部代码时是安全的。

该API是可以链接的，允许你组合多个方法调用在一个语句中：

```python
s = Search().using(client).query("match", title="python")
```

执行execute方法将请求发送给elasticsearch：

```python
response = s.execute()
```

如果仅仅是想要遍历返回结果提示，可以通过遍历Search对象（前提是执行过execute方法）：

```python
for hit in s:
    print(hit.title)
```

可以通过to_dict()方法将Search对象序列化为一个dict对象，这样可以方便调试。

```python
print(s.to_dict())
```

##### Delete By Query

可以通过调用Search对象上的delete方法而不是execute来实现删除匹配查询的文档，如下：

```python
s = Search(index='i').query("match", title="python")
response = s.delete()
```

##### Queries

该库为所有的Elasticsearch查询类型都提供了类。以关键字参数传递所有的参数，最终会把参数序列化后传递给Elasticsearch，这意味着在原始查询和它对应的dsl之间有这一个清理的一对一的映射。

```python
from elasticsearch_dsl.query import MultiMatch, Match

# {"multi_match": {"query": "python django", "fields": ["title", "body"]}}
MultiMatch(query='python django', fields=['title', 'body'])

# {"match": {"title": {"query": "web framework", "type": "phrase"}}}
Match(title={"query": "web framework", "type": "phrase"})
```

你可以使用快捷方式Q通过命名参数或者原始dict类型数据来构建一个查询实例：

```python
from elasticsearch_dsl import Q

Q("multi_match", query='python django', fields=['title', 'body'])
Q({"multi_match": {"query": "python django", "fields": ["title", "body"]}})
```

通过.query()方法将查询添加到Search对象中：

```python
q = Q("multi_match", query='python django', fields=['title', 'body'])
s = s.query(q)
```

该方法还可以接收所有Q的参数作为参数。

```python
s = s.query("multi_match", query='python django', fields=['title', 'body'])
```

###### Dotted fields

有时候你想要引用一个在其他字段中的字段，例如多字段（title.keyword）或者在一个json文档中的address.city。为了方便，Q允许你使用双下划线‘__’代替关键词参数中的‘.’

```python
s = Search()
s = s.filter('term', category__keyword='Python')
s = s.query('match', address__city='prague')
```

除此之外，如果你愿意，也可以随时使用python的kwarg解压缩功能。

```python
s = Search()
s = s.filter('term', **{'category.keyword': 'Python'})
s = s.query('match', **{'address.city': 'prague'})
```

###### Query combination

查询对象可以通过逻辑运算符组合起来：

```python
Q("match", title='python') | Q("match", title='django')
# {"bool": {"should": [...]}}

Q("match", title='python') & Q("match", title='django')
# {"bool": {"must": [...]}}

~Q("match", title="python")
# {"bool": {"must_not": [...]}}
```

当调用`.query()`方法多次时，内部会使用`&`操作符：

```python
s = s.query().query()
print(s.to_dict())
# {"query": {"bool": {...}}}
```

如果你想要精确控制查询的格式，可以通过Q直接构造组合查询：

```python
q = Q('bool',
    must=[Q('match', title='python')],
    should=[Q(...), Q(...)],
    minimum_should_match=1
)
s = Search().query(q)
```

##### Filters

如果你想要在过滤上下文中添加查询，可以使用`filter()`函数来使之变的简单。

```python
s = Search()
s = s.filter('terms', tags=['search', 'python'])
```

在背后，这会产生一个`bool`查询，并将指定的条件查询放入其`filter`分支，等价与下面的操作：

```python
s = Search()
s = s.query('bool', filter=[Q('terms', tags=['search', 'python'])])
```

如果你想要使用`post_filter`元素进行多面导航，请使用`.post_filter()`方法，你还可以使用`exculde()`方法从查询中排除项目：

```python
s = Search()
s = s.exclude('terms', tags=['search', 'python'])
```

##### Aggregations

你可以是使用A快捷方式来定义一个聚合。

```python
from elasticsearch_dsl import A

A('terms', field='tags')
# {"terms": {"field": "tags"}}
```

为了实现聚合嵌套，你可以使用`.bucket()`、`.metirc()`以及`.pipeline()`方法。

```python
a = A('terms', field='category')
# {'terms': {'field': 'category'}}

a.metric('clicks_per_category', 'sum', field='clicks')\
    .bucket('tags_per_category', 'terms', field='tags')

# {
#   'terms': {'field': 'category'},
#   'aggs': {
#     'clicks_per_category': {'sum': {'field': 'clicks'}},
#     'tags_per_category': {'terms': {'field': 'tags'}}
#   }
# }
```

为了将聚合添加到`Search`对象中，使用`.aggs`属性，它是作为一个`top-level`聚合的。

```python
s = Search()
a = A('terms', field='category')
s.aggs.bucket('category_terms', a)

# {
#   'aggs': {
#     'category_terms': {
#       'terms': {
#         'field': 'category'
#       }
#     }
#   }
# }
```

或者：

```python
s = Search()
s.aggs.bucket('articles_per_day', 'date_histogram', field='publish_date', interval='day')\
    .metric('clicks_per_day', 'sum', field='clicks')\
    .pipeline('moving_click_average', 'moving_avg', buckets_path='clicks_per_day')\
    .bucket('tags_per_day', 'terms', field='tags')

s.to_dict()
# {
#   "aggs": {
#     "articles_per_day": {
#       "date_histogram": { "interval": "day", "field": "publish_date" },
#       "aggs": {
#         "clicks_per_day": { "sum": { "field": "clicks" } },
#         "moving_click_average": { "moving_avg": { "buckets_path": "clicks_per_day" } },
#         "tags_per_day": { "terms": { "field": "tags" } }
#       }
#     }
#   }
# }
```

你可以通过名字来访问一个存在的桶。

```python
s = Search()

s.aggs.bucket('per_category', 'terms', field='category')
s.aggs['per_category'].metric('clicks_per_category', 'sum', field='clicks')
s.aggs['per_category'].bucket('tags_per_category', 'terms', field='tags')
```

##### Sorting

要指定排序顺序，可以使用`.order()`方法。

```python
s = Search().sort(
    'category',
    '-title',
    {"lines" : {"order" : "asc", "mode" : "avg"}}
)
```

可以通过不传任何参数调用sort()函数来重置排序。

##### Pagination

要指定from、size，使用slicing API：

```python
s = s[10:20]
# {"from": 10, "size": 10}
```

要访问匹配的所有文档，可以使用scan()函数，scan()函数使用scan、scroll elasticsearch API：

```python
for hit in s.scan():
    print(hit.title)
```

需要注意的是这种情况下结果是不会被排序的。

##### Highlighting

要指定高亮的通用属性，可以使用`highlight_options()`方法：

```python
s = s.highlight_options(order='score')
```

可以通过`highlight()`方法来为了每个单独的字段设置高亮：

```python
s = s.highlight('title')
# or, including parameters:
s = s.highlight('title', fragment_size=50)
```

然后，响应中的分段将在每个结果对象上以`.meta.highlight.FIELD`形式提供，其中将包含分段列表：

```python
response = s.execute()
for hit in response:
    for fragment in hit.meta.highlight.title:
        print(fragment)
```

##### Suggestions

要指定一个suggest请求在你的search对象上，可以使用suggest()方法：

```python
# check for correct spelling
s = s.suggest('my_suggestion', 'pyhton', term={'field': 'title'})
```

##### Extra properties and parameters

要为search对象设置额外的属性，可以使用`.extra()`方法。可以用来定义body中的key，那些不能通过指定API方法来设置的，例如explain、search_filter。

```python
s = s.extra(explain=True)
```

要设置查询参数，可以使用`.params()`方法：

```python
s = s.params(routing="42")
```

如果要限制elasticsearch返回的字段，可以使用`source()`方法：

```python
# only return the selected fields
s = s.source(['title', 'body'])
# don't return any fields, just the metadata
s = s.source(False)
# explicitly include/exclude fields
s = s.source(includes=["title"], excludes=["user.*"])
# reset the field selection
s = s.source(None)
```

##### Serialization and Deserialization

查询对象可以通过使用.to_dict()方法被序列化为一个字典。

你也可以使用类方法from_dict从一个dict创建一个Search对象。这会创建一个新的Search对象并使用字典中的数据填充它。

```python
s = Search.from_dict({"query": {"match": {"title": "python"}}})
```

如果你希望修改现有的Search对象，并覆盖其属性，则可以使用update_from_dict()方法就地更改实例。

```python
s = Search(index='i')
s.update_from_dict({"query": {"match": {"title": "python"}}, "size": 42})
```

#### Response

你可以通过调用execute方法来执行你的搜索，它会返回一个Response对象，Response对象允许你通过属性的方式访问返回结果字典中的任何key。

```python
print(response.success())
# True

print(response.took)
# 12

print(response.hits.total.relation)
# eq
print(response.hits.total.value)
# 142

print(response.suggest.my_suggestions)
```

如果想要检查response对象的内容，可以通过to_dict方法访问原始数据。

##### Hits

可以通过`hits`属性访问返回的匹配结果，或者遍历Response对象。

```python
response = s.execute()
print('Total %d hits found.' % response.hits.total)
for h in response:
    print(h.title, h.body)
```

##### Result

每个匹配项被封装到一个类中，可以方便通过类属性来访问返回结果字典中的key，所有的元数据存储在meta属性中。

```python
response = s.execute()
h = response.hits[0]
print('/%s/%s/%s returned with score %f' % (
    h.meta.index, h.meta.doc_type, h.meta.id, h.meta.score))
```

##### Aggregations

可以通过aggregations属性来访问聚合结果：

```python
for tag in response.aggregations.per_tag.buckets:
    print(tag.key, tag.max_lines.value)
```

#### MultiSearch

可以通过MultiSearch类同时执行多个搜索，它将会使用_msearch API：

```python
from elasticsearch_dsl import MultiSearch, Search

ms = MultiSearch(index='blogs')

ms = ms.add(Search().filter('term', tags='python'))
ms = ms.add(Search().filter('term', tags='elasticsearch'))

responses = ms.execute()

for response in responses:
    print("Results for query %r." % response.search.query)
    for hit in response:
        print(hit.title)
```

### Persistence

你可以使用dsl库来定义你的mappings和一个基本的持久化层为你的应用程序。

#### Document

如果你要为你的文档创建一个model-like的封装，可以使用Document类。它可以被用作创建在elasticsearch中所有需要的mappings和settings。

```python
from datetime import datetime
from elasticsearch_dsl import Document, Date, Nested, Boolean, \
    analyzer, InnerDoc, Completion, Keyword, Text

html_strip = analyzer('html_strip',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

class Comment(InnerDoc):
    author = Text(fields={'raw': Keyword()})
    content = Text(analyzer='snowball')
    created_at = Date()

    def age(self):
        return datetime.now() - self.created_at

class Post(Document):
    title = Text()
    title_suggest = Completion()
    created_at = Date()
    published = Boolean()
    category = Text(
        analyzer=html_strip,
        fields={'raw': Keyword()}
    )

    comments = Nested(Comment)

     class Index:
        name = 'blog'

    def add_comment(self, author, content):
        self.comments.append(
          Comment(author=author, content=content, created_at=datetime.now()))

    def save(self, ** kwargs):
        self.created_at = datetime.now()
        return super().save(** kwargs)
```

##### Data types

定义Document实例时，除了可以使用python类型，还可以使用InnerDoc、Range等类型来表示非简单类型的数据。

```python
from elasticsearch_dsl import Document, DateRange, Keyword, Range

class RoomBooking(Document):
    room = Keyword()
    dates = DateRange()


rb = RoomBooking(
  room='Conference Room II',
  dates=Range(
    gte=datetime(2018, 11, 17, 9, 0, 0),
    lt=datetime(2018, 11, 17, 10, 0, 0)
  )
)

# Range supports the in operator correctly:
datetime(2018, 11, 17, 9, 30, 0) in rb.dates # True

# you can also get the limits and whether they are inclusive or exclusive:
rb.dates.lower # datetime(2018, 11, 17, 9, 0, 0), True
rb.dates.upper # datetime(2018, 11, 17, 10, 0, 0), False

# empty range is unbounded
Range().lower # None, False
```

##### Note on dates

当实例化一个Date字段时，可以通过设置default_timezone参数来明确指定时区。

```python
class Post(Document):
    created_at = Date(default_timezone='UTC')
```

##### Document life cycle

在你第一次使用Post文档类型前，你需要在elasticsearch中创建mappings。可以通过Index对象或者调用init()方法直接创建mappings。

```python
# create the mappings in Elasticsearch
Post.init()
```

所有metadata字段，可以通过meta属性访问。

```python
post = Post(meta={'id': 42})

# prints 42
print(post.meta.id)

# override default index
post.meta.index = 'my-blog'
```

可以通过get()方法来检索一个存在的文档：

```python
# retrieve the document
first = Post.get(id=42)
# now we can call methods, change fields, ...
first.add_comment('me', 'This is nice!')
# and save the changes into the cluster again
first.save()
```

要删除一个文档，直接调用delete()方法即可：

```python
first = Post.get(id=42)
first.delete()
```

#### Analysis

要为text字段指定analyzer，你只需要使用analyze的名字，使用已有的analyze或者自己定义。

##### Search

为了在该文档类型上搜索，使用search方法即可。

```python
# by calling .search we get back a standard Search object
s = Post.search()
# the search is already limited to the index and doc_type of our document
s = s.filter('term', published=True).query('match', title='first')


results = s.execute()

# when you execute the search the results are wrapped in your document class (Post)
for post in results:
    print(post.meta.score, post.title)
```

##### class Meta options

在Meta类中定义了多个你可以为你的文档定义的metadata，例如mapping。

##### class Index options

Index类中定义了该索引的信息，它的名字、settings和其他属性。

##### Document Inheritance

#### Index

在典型情况下，在Document类上使用Index类足够处理任何操作的。在少量case下，直接操作Index对象可能更有用。

Index是一个类，负责保存一个索引在elasticsearch中的所有关联元数据，例如mapping和settings。由于它允许方便的同时创建多个mapping，所以当定义mapping的时候它是最有用的。当在迁移elasticsearch对象的时候是特别有用的。

```python
from elasticsearch_dsl import Index, Document, Text, analyzer

blogs = Index('blogs')

# define custom settings
blogs.settings(
    number_of_shards=1,
    number_of_replicas=0
)

# define aliases
blogs.aliases(
    old_blogs={}
)

# register a document with the index
blogs.document(Post)

# can also be used as class decorator when defining the Document
@blogs.document
class Post(Document):
    title = Text()

# You can attach custom analyzers to the index

html_strip = analyzer('html_strip',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

blogs.analyzer(html_strip)

# delete the index, ignore if it doesn't exist
blogs.delete(ignore=404)

# create the index in elasticsearch
blogs.create()
```

你可以为你的索引设置模板，并使用clone()方法创建一个指定的拷贝：

```python
blogs = Index('blogs', using='production')
blogs.settings(number_of_shards=2)
blogs.document(Post)

# create a copy of the index with different name
company_blogs = blogs.clone('company-blogs')

# create a different copy on different cluster
dev_blogs = blogs.clone('blogs', using='dev')
# and change its settings
dev_blogs.setting(number_of_shards=1)
```

##### Index Template

elasticsearch-dsl还提供了使用IndexTemplate类在elasticsearch中来管理索引模板的选项，该类与Index的API非常相似。

一旦一个索引模板被保存到elasticsearch，他的内容将会自动应用到匹配模式的新索引上（已存在的索引不会受影响），即使索引是当索引一个文档时自动创建的。

```python
from datetime import datetime

from elasticsearch_dsl import Document, Date, Text


class Log(Document):
    content = Text()
    timestamp = Date()

    class Index:
        name = "logs-*"
        settings = {
          "number_of_shards": 2
        }

    def save(self, **kwargs):
        # assign now if no timestamp given
        if not self.timestamp:
            self.timestamp = datetime.now()

        # override the index to go to the proper timeslot
        kwargs['index'] = self.timestamp.strftime('logs-%Y%m%d')
        return super().save(**kwargs)

# once, as part of application setup, during deploy/migrations:
logs = Log._index.as_template('logs', order=0)
logs.save()

# to perform search across all logs:
search = Log.search()
```

### Faceted Search

该API是实验性的，并且也没有用到，所以先跳过。

### Update By Query

#### The Update By Query object

Update By Query对象允许使用_update_by_query实现在一个匹配过程中更新一个文档。

##### Serialization and Deserialization

该查询对象可以通过.to_dict()方法序列化为一个字典，也可以通过类方法from_dict()从一个字典构建一个对象。

```python
ubq = UpdateByQuery.from_dict({"query": {"match": {"title": "python"}}})
```

##### Extra properties and parameters

可以通过.extra()方法设置额外的属性：

```python
ubq = ubq.extra(explain=True)
```

可以通过.params()方法设置查询参数：

```python
ubq = ubq.params(routing="42")
```

#### Response

你可以调用.execute()方法执行查询，它会返回一个Response对象。Response对象允许通过属性访问结果字典中的任何key。

```python
response = ubq.execute()

print(response.success())
# True

print(response.took)
# 12
```

如果需要查看response对象的内容，使用to_dic()方法获取它的原始数据即可。

### API Documentation

API Documention详细介绍了`elasticsearch-dsl`库中的公共类和方法的用法，具体使用的时候直接翻阅参考即可。

## 总结

1. `elasticsearch-dsl`相比于**elasticsearch**来说，提供了更简便的方法来操作**elasticsearch**，减少了生成DSL查询语言的复杂性，推荐使用。
2. `elasticsearch-dsl`的方法其实还是和**elasticsearch**的**restful API**对应的，所以它的API文档有些地方写的并不清晰，例如实例构造可以传递哪些参数？它的说明时可以接收任何关键字参数并会直接把参数传递给elasticsearch，所以要确定哪些参数生效，还是需要我们去查看`elasticsearch`的**restful API**文档。
