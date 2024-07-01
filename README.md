## 介绍
* 一个微信消息转发服务，手机端需要安装APP`短信转发器`，配置一个bark转发器，将微信信息发送到服务器上。服务器读取到数据之后进行解析和转发
* 针对私聊和群消息分别做了消息解析拼装
* BARK_BASE_URL 为手机接收消息的bark地址

## 测试用例
> 私聊
> 下面这个就是连续发送多条的情况
```json
{
  "title": "com.tencent.mm", 
  "body": "com.tencent.mm\\n[2条]慎微姐: test13\\n慎微姐\\nUID：10234\\n2024-06-29 15:34:18",
  "isArchive": 1,
  "level": "active"
}
```
> 私聊-单条
```json
{
  "title": "com.tencent.mm", 
  "body": "com.tencent.mm\\ntest12\\n慎微姐\\nUID：10234\\n2024-06-29 15:23:18",
  "isArchive": 1,
  "level": "active"
}
```
> 群消息
```json
{
  "title": "com.tencent.mm",
  "body": "com.tencent.mm\\n张: 发之前再对其一下颗粒度，辛苦一下赶紧整理\\n开发室A2\\nUID：10234\\n2024-06-29 15:34:18",
  "isArchive": 1,
  "level": "active"
}
```


## 要点
* 主要是适配苹果的语音播报，如果是转发器直接转发过来的服务，播报会阅读很多消息相关但没必要的参数，所以加了一个中转站进行过滤
* 从上面样例可以看到，群消息和私聊多条的样式基本类似，所以暂时通过配置项进行匹配群名称来走群相关的解析