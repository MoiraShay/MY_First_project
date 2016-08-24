#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#10.定义类方法
#方法分为类方法和实例方法
#在class中定义的全部都是实例方法，实例方法第一个参数self是实例本省
#在class中定义类方法这样写
class Person(object):
    #count=0
    #将类的属性count 改为私有的
    __count =0
    #通过标记一个 @classmethod，该方法将绑定到 Person 类上，而非类的实例。
    # 类方法的第一个参数将传入类本身，通常将参数名命名为 cls，上面的 cls.count 实际上相当于 Person.count。
    @classmethod
    def how_many(cls):
        #return cls.count
        return cls.__count
    def __init__(self,name):
        self.name=name
        Person.__count=Person.__count+1
#因为是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获得类的引用
print Person.how_many()
p1=Person('Bob')
print Person.how_many()


