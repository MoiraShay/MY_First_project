#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#面向对象编程的基本思想是类和实例
#人是一种抽象的数据类型就可以看做一个类，小明小丁就是实例
#根据类来创建具体的实例
#面向对象编程最重要的思想是：数据封装（在类中把每一个实例的属性封装起来）
#2.定义类并创建实例
#按照 Python 的编程习惯，类名以大写字母开头，紧接着是(object)，表示该类是从哪个类继承下来的。类的继承将在后面的章节讲解，现在我们只需要简单地从object类继承。
class Person(object):
    pass
#4.初始化实例属性
# 在定义 Person 类时，可以为Person类添加一个特殊的__init__()方法，当创建实例时，__init__()方法被自动调用，我们就能在此为每个实例都统一加上以下属性：
#_init__() 方法的第一个参数必须是 self，后续参数则可以自由指定，创建实例时，就必须要提供除 self 以外的参数
def __init__(self,name,gender,birth):
       self.name=name
       self.gender=gender
       self.birth=birth
#创建实例使用 类名+()，类似函数调用的形式创建：
# xiaoming=Person()
# xiaohong=Person()
# print xiaohong
# print xiaohong
# print xiaoming==xiaohong
#3.创建实例属性
#给实例的属性赋值，例如，给xiaoming这个实例加上name、gender和birth属性：
# xiaoming=Person()
# xiaoming.name='Xiao Ming'
# xiaoming.gender='Male'
# xiaoming.birth='1990-1-1'
# xiaohong=Person()
# xiaohong.name='Xiao Hong'
# xiaohong.school='No.1 High School'
# xiaohong.grade=2
#创建实例属性
# 虽然可以通过Person类创建出xiaoming、xiaohong等实例，但是这些实例看上除了地址不同外，没有什么其他不同。在现实世界中，区分xiaoming、xiaohong要依靠他们各自的名字、性别、生日等属性。
# 如何让每个实例拥有各自不同的属性？由于Python是动态语言，对每一个实例，都可以直接给他们的属性赋值，例如，给xiaoming这个实例加上name、gender和birth属性：
#实例的属性可以像普通变量一样进行操作
# xiaohong.grade=xiaohong.grade+1
#任务
#请创建包含两个 Person 类的实例的 list，并给两个实例的 name 赋值，然后按照 name 进行排序。
p1=Person()
p1.name='Bart'
p2=Person()
p2.name='Adam'
p3=Person()
p3.name='Lisa'
L1=[p1,p2,p3]
# 首先是sorted函数，第一个参数为LIST 即 L1 第二个参数为定义的比较函数；
# lambda p1, p2: cmp(p1.name, p2.name)  意思是，传入p1和p2，比较两者的name
# 这样一分解就容易理解了吧
L2=sorted(L1,lambda p1,p2:cmp(p1.name,p2.name))
print L2[0].name
print L2[1].name
print L2[2].name
