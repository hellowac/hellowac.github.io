# logging

- 创建时间: 2022年08月09日16:17:05
- 官网: <https://docs.python.org/zh-cn/3.7/library/logging.html>

## 输出到控制台:

```python
import logging

formatter = logging.Formatter("[%(asctime)s] - %(pathname)s:%(lineno)d %(message)s")
logger = logging.getLogger("parse_ppt")
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(console)

logger.info("这是日志")
```

## 快速创建logger

```python
import sys
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

        
def initializeLogger(name, logfile, log_level=logging.DEBUG, file_level=logging.INFO):

    logger = logging.getLogger(name)

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        "[%(asctime)s] - %(levelname)s in %(pathname)s:%(lineno)d - %(message)s"
    )
    logger.setLevel(log_level)

    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(formatter)
    consoleHandler.setLevel(log_level)
    logger.addHandler(consoleHandler)

    rotatingFileHanlder = RotatingFileHandler(
        f"{logfile}.{datetime.utcnow().strftime('%Y%m%d')}.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=1,
    )
    rotatingFileHanlder.setFormatter(formatter)
    rotatingFileHanlder.setLevel(file_level)
    logger.addHandler(rotatingFileHanlder)

    return logger
```

## 字符串格式

原文: <https://docs.python.org/zh-cn/3.7/library/logging.html#logrecord-attributes>

| 属性名称        | 格式                | 描述                                                                                                                                                                                                |
| --------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| args            | 不需要格式化。      | 合并到 `msg` 以产生 `message` 的包含参数的元组，或是其中的值将被用于合并的字典（当只有一个参数且其类型为字典时）。                                                                                  |
| asctime         | %(asctime)s         | 表示 [LogRecord](https://docs.python.org/zh-cn/3.7/library/logging.html#logging.LogRecord) 何时被创建的供人查看时间值。 默认形式为 '2003-07-08 16:49:45,896' (逗号之后的数字为时间的毫秒部分)。     |
| created         | %(created)f         | [LogRecord](https://docs.python.org/zh-cn/3.7/library/logging.html#logging.LogRecord) 被创建的时间（即 [time.time()](https://docs.python.org/zh-cn/3.7/library/time.html#time.time) 的返回值）。    |
| exc_info        | 不需要格式化。      | 异常元组 (例如 `sys.exc_info`) 或者如未发生异常则为 `None`。                                                                                                                                        |
| filename        | %(filename)s        | `pathname` 的文件名部分。                                                                                                                                                                           |
| funcName        | %(funcName)s        | 函数名包括调用日志记录.                                                                                                                                                                             |
| levelname       | %(levelname)s       | 消息文本记录级别 ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').                                                                                                                                 |
| levelno         | %(levelno)s         | 消息数字记录级别 (DEBUG, INFO, WARNING, ERROR, CRITICAL).                                                                                                                                           |
| lineno          | %(lineno)d          | 发出日志记录调用所在的源行号（如果可用）。                                                                                                                                                          |
| message         | %(message)s         | 记入日志的消息，即 `msg % args` 的结果。 这是在发起调用 [Formatter.format()](https://docs.python.org/zh-cn/3.7/library/logging.html#logging.Formatter.format) 时设置的。                            |
| module          | %(module)s          | 模块 (`filename` 的名称部分)。                                                                                                                                                                      |
| msecs           | %(msecs)d           | [LogRecord](https://docs.python.org/zh-cn/3.7/library/logging.html#logging.LogRecord) 被创建的时间的毫秒部分。                                                                                      |
| msg             | 不需要格式化。      | 在原始日志记录调用中传入的格式字符串。 与 args 合并以产生 message，或是一个任意对象 (参见 [使用任意对象作为消息](https://docs.python.org/zh-cn/3.7/howto/logging.html#arbitrary-object-messages))。 |
| name            | %(name)s            | 用于记录调用的日志记录器名称。                                                                                                                                                                      |
| pathname        | %(pathname)s        | 发出日志记录调用的源文件的完整路径名（如果可用）。                                                                                                                                                  |
| process         | %(process)d         | 进程ID（如果可用）                                                                                                                                                                                  |
| processName     | %(processName)s     | 进程名（如果可用）                                                                                                                                                                                  |
| relativeCreated | %(relativeCreated)d | 以毫秒数表示的 [LogRecord](https://docs.python.org/zh-cn/3.7/library/logging.html#logging.LogRecord) 被创建的时间，即相对于 `logging` 模块被加载时间的差值。                                        |
| stack_info      | 不需要格式化。      | 当前线程中从堆栈底部起向上直到包括日志记录调用并导致创建此记录的堆栈帧的堆栈帧信息（如果可用）。                                                                                                    |
| thread          | %(thread)d          | 线程ID（如果可用）                                                                                                                                                                                  |
| threadName      | %(threadName)s      | 线程名（如果可用）                                                                                                                                                                                  |

> 在 3.1 版本中更改: 添加了 `processName`
