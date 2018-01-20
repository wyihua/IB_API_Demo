（所以要使用的只能是python3，而不能用python2.7）
1.	初始化django应用
2.	在django上面绑定一个template
3.	给template输入指定参数
4.	调用ibpy的库
5.	在template上面做一个按钮
6.	按钮激发获取信息的功能
7.	把获取信息发到传入参数里面

## 创建VIEW

我们没有考虑做sub-app，就直接在默认的主页上面来显示我们的股票信息。
那么必须要做的就是把默认的url指向一个我们定制的HTTP回应上面。

#### 现在遇到的问题：
我已经把url的设置改好了，但是服务器表示不知道views.py文件在哪。
说明我需要设置文件的默认读取路径

#### 如何设置默认读取路径
（我之前在StackOverFlow上面有提到过修改Django的路径，可以查看我之前自己的记录）
然后真正的问题/解答不是修改设置，而是在url.py文件里面引入views文件

#### 现在已经能够展示默认的文字了。

## 展示HTML文件
#### 地址是怎么操作的
Template的地址是index.html。
那么我可能有：
1.	template/index.html
2.	./index.html

两种选择。

#### 测试结果
问题不在地址，而是在于genericView需要Model，而我现在没有model。

#### 初始渲染HTML的方法
在django的shortcut里面调用render函数

