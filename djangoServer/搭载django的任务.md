## Django的教程链接
https://docs.djangoproject.com/en/2.0/contents/


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

## 给TEMPLATE输入参数
#### 能做的工作是：
1.	获得一个HTML的sample
2.	给render函数最后的一个参数设置一个变量（数组）
3.	在HTML文件里面调用那个变量

#### 发现传递的参数是有限制的：
1.	普通的数组、字符串和数字不能直接传递
2.	能够传递的有model等context

所以我可能需要知道这里的context的标准是什么

#### 尝试普通的dict
粗略的看了几个答案，发现结论可能是context要求是dict。那么我创建一个dict来看看是否能够传参。
结果是不能使用普通的python的dict。

#### 那么可能是：
1.	这里的dict并不是并不是指的python里面的dict
2.	现在的context要求又变了，dict也不行了

错误的提醒信息是“dict不是hashable的”。这意味着传参的对象必须要hashable的。

#### 那么我们现在有两种解决办法：
1.	按常规做一个model出来，然后调用那个model
2.	想办法做出一个简单的hashable的对象


#### 必须是dict
我尝试用一个比较简单的方法创造hashable的对象，结果发现django服务器报错，要求是dict。但是之前我们创造dict的时候又说dict不是hashable的对象。
基本上我们只能创造model对象，然后以model对象传参了

