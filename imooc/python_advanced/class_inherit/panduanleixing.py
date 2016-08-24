#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
class Person(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
class Student(Person):
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score=score
class Teacher(Person):
    def __init__(self,name,gender,course):
        super(Teacher,self).__init__(name,gender)
        self.course=course
p=Person('Tom','Male')
s=Student('Bob','Male',88)
t=Teacher('Alice','Female','English')
#当我们拿到变量p,s,t时，可以使用isinstance判断类型
#例判断p是不是person类型
print isinstance(p,Person)
print isinstance(p,Teacher)
print isinstance(t,object)