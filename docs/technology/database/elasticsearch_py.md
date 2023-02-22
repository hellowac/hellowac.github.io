# ElasticSearch

* 创建时间: 2023年02月21日17:32:47
* github: <https://github.com/elastic/elasticsearch-py>{target="_blank"}
* 源文档: <https://ela.st/es-python>{target="_blank"}
* RTD地址: <https://elasticsearch-py.readthedocs.io/en/v8.6.2/>{target="_blank"}
* ES官方中文资料: <https://www.elastic.co/guide/cn/index.html>{target="_blank"}

**Elasticsearch Python Client**

## 功能

* 将基本的 Python 数据类型与 JSON 相互转换
* 集群节点的可配置自动发现
* 持久连接
* 跨可用节点的负载平衡（使用可插入选择策略）
* 失败的连接惩罚（基于时间 - 在达到超时之前不会重试失败的连接）
* 支持 TLS 和 HTTP 身份验证
* 跨请求的线程安全
* 可插拔架构
* 惯用地一起使用 API 的辅助函数

## 安装

使用 [pip](https://pypi.org/project/elasticsearch){target="_blank"} 安装 elasticsearch 包：

```shell
python -m pip install elasticsearch
```

如果您的应用程序在 Python 中使用 `async/await`，您可以安装`async`扩展以使用：

```shell
python -m pip install elasticsearch[async]
```

阅读有关[如何在此项目中使用 asyncio 的更多信息](https://elasticsearch-py.readthedocs.io/en/latest/async.html){target="_blank"}。

## 兼容性

语言客户端向前兼容； 这意味着客户端支持与更大或相等的次要版本的 Elasticsearch 进行通信。 Elasticsearch 语言客户端仅向后兼容默认发行版，并且不作任何保证。

如果您需要同时安装多个版本，旧版本也作为 elasticsearch2 和 elasticsearch5 发布。

## 文档

客户端文档可在 [elastic.co](https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/index.html){target="_blank"} 和[Read the Docs](https://elasticsearch-py.readthedocs.io/){target="_blank"}中找到。

## 快速开始

```python
# Import the client from the 'elasticsearch' module
>>> from elasticsearch import Elasticsearch

# Instantiate a client instance
>>> client = Elasticsearch("http://localhost:9200")

# Call an API, in this example `info()`
>>> resp = client.info()

# View the result
>>> resp
{
  "name" : "instance-name",
  "cluster_name" : "cluster-name",
  "cluster_uuid" : "cluster-uuid",
  "version" : {
    "number" : "7.14.0",
    ...
  },
  "tagline" : "You know, for Search"
}
```

您可以在文档中阅读有关[配置客户端](https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/connecting.html){target="_blank"}的更多信息。

## 许可证

Copyright 2023 Elasticsearch B.V. Licensed under the Apache License, Version 2.0.

版权所有 2023 Elasticsearch B.V. 根据 Apache 许可证 2.0 版获得许可。
