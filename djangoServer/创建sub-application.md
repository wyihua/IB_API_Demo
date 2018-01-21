## 教程链接
https://docs.djangoproject.com/en/2.0/contents/

#### 我们要做的工作有：
1.	初始化应用（已完成）
2.	调整url（这一步是最麻烦的，因为我不熟悉）
3.	创建一个model
4.	创建一个generic的view

## 调整URL
#### 我记得要调整的设置包括：
1.	在主程序的setting里面加入子应用的config文件（这是为绑定数据库）（貌似已完成）
2.	URL不确定怎么设置，应该要查看URL文件（已完成）
3.	还需要在子应用里面创建url文件（已完成）


## 创建一个MODEL
#### 参考链接：
https://docs.djangoproject.com/en/2.0/intro/tutorial02/#database-setup 

#### 我们要做的工作有：
1.	在主程序绑定数据库（上一步已完成）
2.	在 models.py文件里面定义新的model类（ticket）（我昨天应该在主程序里面写了）（已完成）
3.	在命令行使用makeimmigration（已完成，这之后的变化是子应用的migrations文件夹里面多了一个初始化的py文件）
4.	然后使用sqlmigrate查看（注意检查下migration文件夹有什么不同）（已完成，文件中知识多了一个缓存文件）
5.	在命令行migrate（已完成）
6.	使用shell测试（已完成）

## 创建一个GENERIC的VIEW
#### 参考链接：
https://docs.djangoproject.com/en/2.0/intro/tutorial04/#use-generic-views-less-code-is-better

#### 我们要做的工作有：
1.	在views.py文件里面创建一个view类
2.	在这个类里面绑定model和template
3.	在url文件里面采用URLconf

## 给DB家两个ITEMS
#### 解释
出现这个问题的原因是，在使用generic view的时候，我不知道template是否会主动显示model里面的对象。
所以我要在数据库里面家两个items，看看template会不会自动渲染这两个items。

#### 手动给数据库增加items的办法-使用shell

## 遇到问题：刚才常见的数据貌似没有属性
这里说没有属性的依据是在migrations文件夹的init文件里面，创建命令里面只有创建table的语句，跟没有提到和属性相关的语句。
然后通过sql命令检查schema文件，发现确实没有属性。

#### 我们之前认为应该有属性的原因是
我在models文件里面按道理创建了model类，并且设置了几个变量。
不确定如何将这几个变量和model类绑定起来。难道需要使用self？

#### 检查之后，发现
1.	我的代码里面确实没有self语句
2.	但是教程里面也是没有使用self语句的

#### 解决问题
最后发现，问题的根源并不是有没有self语句，还是是否在变量的声明语句后面提供默认值。只有提供默认值，才是一个完整的属性声明函数。


