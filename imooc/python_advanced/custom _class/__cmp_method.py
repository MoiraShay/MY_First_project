#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#3.__cmp__
class Person(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def __str__(self):
        return '(Person:%s,%s)' %(self.name,self.gender)
class Student(Person):
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score=score
    def __str__(self):
       # return '(Student:%s,%s,%s)'  % (self.name,self.gender,self.score)
        return '(%s:%s)' %(self.name,self.score)
    #1.如果要把一个类的实例变成 str，就需要实现特殊方法__str__()：2.__str__()用于显示给用户，而__repr__()用于显示给开发人员。
    __repr__=__str__
    #实现了__cmp__()方法，__cmp__用实例自身self和传入的实例 s 进行比较，如果 self 应该排在前面，就返回 -1，如果 s 应该排在前面，就返回1，如果两者相当，返回 0
    #Student类实现了按name进行排序
    #请修改 Student 的 __cmp__ 方法，让它按照分数从高到底排序，分数相同的按名字排序。
    def __cmp__(self, s):
        if self.score==s.score:
            return cmp(self.name,s.name)
        return -cmp(self.score,s.score)
#s=Student('tom','female',70)
#print s
#3.__cmp__
#对 int、str 等内置数据类型排序时，Python的 sorted() 按照默认的比较函数 cmp 排序
#但是，如果对一组 Student 类的实例排序时，就必须提供我们自己的特殊方法 __cmp__()：
L=[Student('Tim','Male',99),Student('Bob','Male',88),Student('Alice','Male',77)]
print sorted(L)
