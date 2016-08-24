#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
class Person(object):
    pass
    #定义类的属性
    address="Earth"
    count=0
    def __init__(self,name,gender):
        #每创建一个实例，count 属性就加 1，这样就可以统计出一共创建了多少个 Person 的实例。
        Person.count+=1
        self.name=name
        self.__gender=gender
#因为类属性是直接绑定在类上的，所以，访问类属性不需要创建实例，就可以直接访问：
print "Person的地址为",Person.address
p1=Person('Bob','女')
p2=Person('Alice','男')
#所有实例都可以访问到它所属的类的属性：
print "p1的地址为",p1.address
print "p2的地址为",p2.address
#由于Python是动态语言，类属性也是可以动态添加和修改的
Person.address='China'
print p1.address
print Person.count
#实例属性和类属性重名时，实例属性优先级高
p1.address="shanghai"
print p1.address