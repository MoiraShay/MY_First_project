#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#继承可以实现代码复用
#python类继承的特点：1.总是从某个类继承，找不到合适的话要从object类继承2.不要忘记调用super().__init__方法，该方法是用来初始化父类的
#2.继承一个类
#首先定义person类
class Person(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    #
#     def whoAmI(self):
#         return 'I am a Person,my name is %s' % self.name
# #其次定义student类
class Student(Person):
    def __init__(self,name,gender,score):
        #一定要用super(Student,self).__init__(name,gender)去初始化父类，否则继承自Person的Student将没有name和gender
        super(Student,self).__init__(name,gender)
        self.score=score
    # def whoAmI(self):
    #     return 'I am a Student,my name is %s' % self.name
class Teacher(Person):
    def __init__(self,name,gender,id,course):
        super(Teacher,self).__init__(name,gender)
        self.id=id
        self.course=course
    # def whoAmI(self):
    #     return 'I am a Teacher,my name is %s' % self.name
t=Teacher('Alice','Female','2','English')
print t.name+":"+t.course