# Zookeeper

官网: <https://zookeeper.apache.org/>

下载: <https://zookeeper.apache.org/releases.html>

## 配置样例

```cfg
tickTime = 2000
dataDir = /home/data/zookeeper/data
dataLogDir = /home/data/zookeeper/dataLog
clientPort = 2181
initLimit = 5
syncLimit = 2

# 定时清理数据
# The number of snapshots to retain in dataDir
autopurge.snapRetainCount=10
# Purge task interval in hours
# Set to "0" to disable auto purge feature
autopurge.purgeInterval=1

# admin.enableServer=false
# admin.serverPort=8088
```
