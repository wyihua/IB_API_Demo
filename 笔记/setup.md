## 文档链接
http://interactivebrokers.github.io/tws-api/initial_setup.html#tws&gsc.tab=0

API可以控制IB Gateway和TWS。

#### TWS
用来交易股票的有GUI的服务器，能够支持全球100个市场的交易。

#### 区分IB Gateway和TWS
IB Gateway能执行的功能和TWS一样，但是不是基于GUI的。IB Gateway能够管理API的请求。
所以我要做的做的工作有可能有一下几种情况：
1.	API -> TWS -> market
2.	API -> IB Gateway -> market
3.	Both 1 and 2

#### 允许API联系
需要设置允许以下客户端：
1.	ActiveX（微软的用来下载网络数据的框架）
2.	Socket Client（就是TCP用户，主要用于unix系统）

后面是下载安装API。

## 尝试安装API
#### API的文件夹里面有两个文件夹：
1.	IBJts
2.	META-INF

两个文件家里面都没有看到说明文件和安装文件。

所以现在我没有办法安装API。只能希望接下来的讲述这个API的结构的章节能够提供我信息。
