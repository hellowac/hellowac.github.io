# importlib

官方文档: <https://docs.python.org/zh-cn/3/library/importlib.html>

## 导入文件中的某个类

比如我们想动态导入某个py文件中的类，那么就需要用到`importlib`包, 先导入`module`，然后执行`module`, 最后取出`module`中的类供我们使用。

参考: <https://docs.python.org/zh-cn/3/library/importlib.html#importing-a-source-file-directly>

```py
module_name = f"LeakModule"
spec = importlib_util.spec_from_file_location(module_name, file_path)
module = importlib_util.module_from_spec(spec)
spec.loader.exec_module(module)

# 类名: TheExploit 是固定的。
excutor = module.TheExploit(ip, port)
logger.info(excutor)
result = excutor.run()

logger.info(f"leak测试结果: {result}")
```
