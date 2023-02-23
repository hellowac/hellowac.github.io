---
comments: true
---


# flask

这里是和flask相关的问题学习记录。

- `1.1.x` 版本的文档：<https://flask.palletsprojects.com/en/1.1.x/>
- `2.0.x` 版本的文档：<https://flask.palletsprojects.com/en/2.0.x/>
- 较新的版本的中文文档: <https://flask-zh.readthedocs.io/>

## falsk 中文学习网

访问: <http://flask123.sinaapp.com/flatpage/flask-docs/>

## flask 之旅

> 本书旨在展示使用 Flask 的最佳实践。 开发一个普通的 Flask 应用需要跟形形色色的领域打交道。比如，你经常需要操作数据库，验证用户。 在接下来的几页里我将尽我所能来介绍处理这些事情时的“正确之道”。 我的建议并不总能有用，但我希望它们在大多数情况下都是一个好选择。

访问: <https://hellowac.github.io/explore-flask-zh/>

## flask 中文版

> 欢迎阅读 Flask 的文档。推荐您先阅读《 安装 》，然后阅读 《 快速上手 》。《 教程 》比快速上手文档更详细一点，该 文档介绍了如何创建一个完整（尽管很小）的 Flask 应用。 《 Flask 方案 》 中介绍了一些常用的解决方案。其余的文档详细介绍了 Flask 的每一个组件。 《 API 》提供了最详细的参考。
>
> Flask 依赖 Jinja 模板引擎和 Werkzeug WSGI 套件。这两个库的文档请移步：
>
> - [Jinja 文档](http://jinja.pocoo.org/docs)
> - [Werkzeug 文档](https://werkzeug.palletsprojects.com/)
>

访问: <https://flask.net.cn/api.html>

## 文件

[flask 1.1.x]: https://flask.palletsprojects.com/en/1.1.x/
[FileStorage]: https://werkzeug.palletsprojects.com/en/2.0.x/datastructures/#werkzeug.datastructures.FileStorage
[file]: https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/

[flask 1.1.x] 版本上传的文件对象 [file] 的类为 `werkzeug.datastructures.FileStorage`, 参考: [FileStorage]

## 日志配置

使用 **flask** 开发 **web app** 时，需在 `create_app` 之前配置好日志记录器。

1. 先配置好 `logger_config.py`
2. 然后导入 `logger_config.py` 文件中的 `config_dict` 变量
3. 使用 `logging` 的 **dictConfig** 配置日志

### logger_config.py

```python
import os

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"

os.makedirs(LOG_DIR, exist_ok=True)

DEBUG = os.environ.get("FLASK_DEBUG", False)

logger_name = 'tsgz'

dict_config = {
    "version": 1,
    "formatters": {
        "simple": {"format": "{asctime} {levelname} {message}", "style": "{"},
        "verbose": {
            "format": "{asctime} {pathname}:{lineno}: {funcName}: {message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
    },
    "handlers": {
        "console": {
            "level": os.environ.get("LOG_LEVEL", "DEBUG"),
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "log_to_detail_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "verbose",
            "filename": LOG_DIR / "detail.log",
            "mode": "w+",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 20,
            "encoding": "utf8",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO" if DEBUG else "WARNING",
    },
    "loggers": {
        logger_name: {
            "handlers": ["console", "log_to_detail_file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

```

### init.py

```python
from logging.config import dictConfig
from flask import Flask

from logger_config import dict_config

# 配置日志文件
dictConfig(dict_config)


db = SQLAlchemy()

app = Flask(__name__)


def create_app():
    app.config.from_object('settings.xxxConfig')
    
    # ...

    db.init_app(app)

    return app
```

### 使用定义的logger

某个py文件

```python
import logging

# ...

from logger_config import logger_name

logger = logging.getLogger(logger_name)
```

现在就能使用配置好的 `logger_name` 咯
