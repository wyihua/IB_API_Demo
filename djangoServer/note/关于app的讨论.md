#### 遇到这个问题的缘由：
当我想要执行makemigrate的命令的时候，发现教程上面说的是对指定的目标app执行命令。而我的数据库和应用是在根文件夹里面，也就是和整个django服务器同名的文件夹里面。
但是当我用这个服务器的名字当成应用的名字的时候，编译器提示没有这个叫做“服务器的名字”的应用。

#### 我想要知道的关于app的信息有：
1.	在setting里面有什么和app相关的信息
2.	App需要注册些什么内容
3.	根app的名字是什么

#### 在setting文件里面，有一个INSTALL_APPS的变量：
这里面初始的app有auth、admin、session 、message等等，但是没有根app。
或者说，django初始的时候不带初始app。
App只能在开始的时候单独声明。

#### App的声明方式
python manage.py startapp appName
