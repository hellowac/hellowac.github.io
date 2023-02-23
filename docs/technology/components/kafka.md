# kafka命令行使用

默认命令目录：`/opt/bitnami/kafka/bin`

## 查看topic列表

<!--more-->

```shell
# 到kafka的bin目录下
> cd /opt/bitnami/kafka/bin
# 查看有哪些主题列表
 > ./kafka-topics.sh --list --zookeeper zoo:2181 \

__consumer_offsets
alert_log__10148251-f73a-4e6b-9ec2-d87734acc496
alert_log__34c0f64a-7e5b-4c69-9121-e8f74e4dfce2
alert_log__39dfedf6-6e50-4010-861f-4ccd45d984e3
alert_log__3a6d77ce-3c5c-46ab-80a4-8afdec95376c
alert_log__6241e819-c4f3-4bb6-8826-7bd7a29a3edc
alert_log__7ab04bf0-6ac3-43d9-9a1a-c54a87421b6d
alert_log__7f66a0c3-9f0f-487b-80c9-8e0139da32e7
alert_log__85f10ae8-75a5-403c-96d1-fc726d0bab5b
alert_log__b9977e9f-5c64-4400-867a-de1f2a03ccd9
alert_log__bf931192-4662-4a16-94e5-399d720e6241
alert_log__c8ad8364-4fed-41c6-81c6-a6c1eae41045
alert_log__d7130cd1-3fda-4d9d-9af8-131e195edd7f
alert_log__f7c7b780-018a-441c-886a-09b2410516d0
attacker__
event__10148251-f73a-4e6b-9ec2-d87734acc496
event__34c0f64a-7e5b-4c69-9121-e8f74e4dfce2
event__39dfedf6-6e50-4010-861f-4ccd45d984e3
event__3a6d77ce-3c5c-46ab-80a4-8afdec95376c
event__6241e819-c4f3-4bb6-8826-7bd7a29a3edc
event__7ab04bf0-6ac3-43d9-9a1a-c54a87421b6d
event__7f66a0c3-9f0f-487b-80c9-8e0139da32e7
event__85f10ae8-75a5-403c-96d1-fc726d0bab5b
event__b9977e9f-5c64-4400-867a-de1f2a03ccd9
event__bf931192-4662-4a16-94e5-399d720e6241
event__c8ad8364-4fed-41c6-81c6-a6c1eae41045
event__d7130cd1-3fda-4d9d-9af8-131e195edd7f
event__f7c7b780-018a-441c-886a-09b2410516d0
no_org_look_alert_log__
org__
```

## 查看group列表

```shell
#  查看有哪些组
$ ./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list

g_out_event
g_attacker
g_org
g_alert_log
g_event
g__no_org_look_alert_log
g_out_log
g_monitor
g_out_attacker
```

## 查看某一具体group详情

- **CURRENT-OFFSET**： 当前已消费的条数
- **LOG-END-OFFSET**： 总条数
- **LAG**： 未消费的条数

```shell
# 查看g_alert_log 组的主题消费如何
$ ./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group g_alert_log --describe
GROUP           TOPIC                                           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                                             HOST            CLIENT-ID
g_alert_log     alert_log__6241e819-c4f3-4bb6-8826-7bd7a29a3edc 0          9012021         9012021         0               kafka-python-1.3.5-ebcdba18-293d-4e03-a511-fff8311bbf24 /172.20.0.1     kafka-python-1.3.5
g_alert_log     alert_log__d7130cd1-3fda-4d9d-9af8-131e195edd7f 0          11140739        11140741        2               kafka-python-1.3.5-ebcdba18-293d-4e03-a511-fff8311bbf24 /172.20.0.1     kafka-python-1.3.5
g_alert_log     alert_log__c8ad8364-4fed-41c6-81c6-a6c1eae41045 0          8276611         8276611         0               kafka-python-1.3.5-ebcdba18-293d-4e03-a511-fff8311bbf24 /172.20.0.1     kafka-python-1.3.5
g_alert_log     alert_log__10148251-f73a-4e6b-9ec2-d87734acc496 0          10234750        10234751        1               kafka-python-1.3.5-ebcdba18-293d-4e03-a511-fff8311bbf24 /172.20.0.1     kafka-python-1.3.5
g_alert_log     alert_log__f7c7b780-018a-441c-886a-09b2410516d0 0          8183641         8183641         0               kafka-python-1.3.5-ebcdba18-293d-4e03-a511-fff8311bbf24 /172.20.0.1     kafka-python-1.3.5
g_alert_log     alert_log__39dfedf6-6e50-4010-861f-4ccd45d984e3 0          642903          642903          0               kafka-python-1.3.5-ebcdba18-293d-4e03-a511-fff8311bbf24 /172.20.0.1     kafka-python-1.3.5
g_alert_log     alert_log__34c0f64a-7e5b-4c69-9121-e8f74e4dfce2 0          11130361        11130361        0               kafka-python-1.3.5-ebcdba18-293d-4e03-a511-fff8311bbf24 /172.20.0.1     kafka-python-1.3.5
g_alert_log     alert_log__7ab04bf0-6ac3-43d9-9a1a-c54a87421b6d 0          2227789         2227789         0               kafka-python-1.3.5-ebcdba18-293d-4e03-a511-fff8311bbf24 /172.20.0.1     kafka-python-1.3.5
g_alert_log     alert_log__bf931192-4662-4a16-94e5-399d720e6241 0          7543358         7543358         0               kafka-python-1.3.5-ebcdba18-293d-4e03-a511-fff8311bbf24 /172.20.0.1     kafka-python-1.3.5
g_alert_log     alert_log__b9977e9f-5c64-4400-867a-de1f2a03ccd9 0          529276717       529276717       0               kafka-python-1.3.5-ebcdba18-293d-4e03-a511-fff8311bbf24 /172.20.0.1     kafka-python-1.3.5
g_alert_log     alert_log__3a6d77ce-3c5c-46ab-80a4-8afdec95376c 0          25129562        25129562        0               kafka-python-1.3.5-ebcdba18-293d-4e03-a511-fff8311bbf24 /172.20.0.1     kafka-python-1.3.5
g_alert_log     alert_log__85f10ae8-75a5-403c-96d1-fc726d0bab5b 0          940400237       940400262       25              kafka-python-1.3.5-ebcdba18-293d-4e03-a511-fff8311bbf24 /172.20.0.1     kafka-python-1.3.5
g_alert_log     alert_log__7f66a0c3-9f0f-487b-80c9-8e0139da32e7 0          3224238         3224238         0               kafka-python-1.3.5-ebcdba18-293d-4e03-a511-fff8311bbf24 /172.20.0.1     kafka-python-1.3.5


$ ./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group g_event --describe
GROUP           TOPIC                                       PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                                             HOST            CLIENT-ID
g_event         event__3a6d77ce-3c5c-46ab-80a4-8afdec95376c 0          975             975             0               kafka-python-1.3.5-4366646c-e350-424d-83cb-86f9d9526d92 /172.20.0.1     kafka-python-1.3.5
g_event         event__f7c7b780-018a-441c-886a-09b2410516d0 0          617             617             0               kafka-python-1.3.5-4366646c-e350-424d-83cb-86f9d9526d92 /172.20.0.1     kafka-python-1.3.5
g_event         event__6241e819-c4f3-4bb6-8826-7bd7a29a3edc 0          535             535             0               kafka-python-1.3.5-4366646c-e350-424d-83cb-86f9d9526d92 /172.20.0.1     kafka-python-1.3.5
g_event         event__7f66a0c3-9f0f-487b-80c9-8e0139da32e7 0          512             512             0               kafka-python-1.3.5-4366646c-e350-424d-83cb-86f9d9526d92 /172.20.0.1     kafka-python-1.3.5
g_event         event__bf931192-4662-4a16-94e5-399d720e6241 0          474             474             0               kafka-python-1.3.5-4366646c-e350-424d-83cb-86f9d9526d92 /172.20.0.1     kafka-python-1.3.5
g_event         event__34c0f64a-7e5b-4c69-9121-e8f74e4dfce2 0          831             831             0               kafka-python-1.3.5-4366646c-e350-424d-83cb-86f9d9526d92 /172.20.0.1     kafka-python-1.3.5
g_event         event__c8ad8364-4fed-41c6-81c6-a6c1eae41045 0          7503            7503            0               kafka-python-1.3.5-4366646c-e350-424d-83cb-86f9d9526d92 /172.20.0.1     kafka-python-1.3.5
g_event         event__7ab04bf0-6ac3-43d9-9a1a-c54a87421b6d 0          309             309             0               kafka-python-1.3.5-4366646c-e350-424d-83cb-86f9d9526d92 /172.20.0.1     kafka-python-1.3.5
g_event         event__d7130cd1-3fda-4d9d-9af8-131e195edd7f 0          8849            8849            0               kafka-python-1.3.5-4366646c-e350-424d-83cb-86f9d9526d92 /172.20.0.1     kafka-python-1.3.5
g_event         event__b9977e9f-5c64-4400-867a-de1f2a03ccd9 0          1422            1422            0               kafka-python-1.3.5-4366646c-e350-424d-83cb-86f9d9526d92 /172.20.0.1     kafka-python-1.3.5
g_event         event__10148251-f73a-4e6b-9ec2-d87734acc496 0          8741            8741            0               kafka-python-1.3.5-4366646c-e350-424d-83cb-86f9d9526d92 /172.20.0.1     kafka-python-1.3.5
g_event         event__39dfedf6-6e50-4010-861f-4ccd45d984e3 0          361             361             0               kafka-python-1.3.5-4366646c-e350-424d-83cb-86f9d9526d92 /172.20.0.1     kafka-python-1.3.5
g_event         event__85f10ae8-75a5-403c-96d1-fc726d0bab5b 0          3435            3435            0               kafka-python-1.3.5-4366646c-e350-424d-83cb-86f9d9526d92 /172.20.0.1     kafka-python-1.3.5

```

## 查看某topic里的数据

- 从头开始消费topicname
- 手动消费一条数据
- 命令：`./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topicName --from-beginning`

```shell

```
