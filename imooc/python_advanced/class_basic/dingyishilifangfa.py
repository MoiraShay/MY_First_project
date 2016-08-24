#_*_coding:utf-8_*_
import types
__author__ = 'mamadongpei'
#方法也是属性
def fn_get_grade(self):
    if self.score>=80:
        return 'A'
    if self.score>=60:
        return 'B'
    return 'C'
class Person(object):
    pass
#8.实例的方法就是在类中定义的函数，它的第一个参数永远是 self，指向调用该方法的实例本身
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
        self.score=score
    #get_name(self) 就是一个实例方法，它的第一个参数是self
    def get_name(self):
        return self.__name
    def get_grade(self):
        if self.__score>=80:
           return 'A'
        if self.__score>=60:
            return 'B'
        return 'C'
    #调用实例方法必须在实例上调用
p1=Person('Bob',90)
p2=Person('Alice',65)
p3=Person('Tim',45)
print p1.get_name()+":"+p1.get_grade()
print p2.get_name()+":"+p2.get_grade()
print p3.get_name()+":"+p3.get_grade()
#在实例方法内部，可以访问所有实例属性，这样，如果外部需要访问私有属性，可以通过方法调用获得，
# 这种数据封装的形式除了能保护内部数据一致性外，还可以简化外部调用的难度。
#9.方法也是属性
#因为方法也是属性，所以它也可以动态的添加到实例上，只是要用types.MethodType()把一个函数变成一个方法
p1.get_grade=types.MethodType(fn_get_grade,p1,Person)
print p1.get_grade()