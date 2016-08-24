#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#除了从一个父类继承外，Python允许从多个父类继承，称为多重继承。
#多重继承的目的是从两种继承树中分别选择并继承出子类，以便组合功能使用。
# class A(object):
#     def __init__(self, a):
#         print 'init A...'
#         self.a = a
#
# class B(A):
#     def __init__(self, a):
#         super(B, self).__init__(a)
#         print 'init B...'
#
# class C(A):
#     def __init__(self, a):
#         super(C, self).__init__(a)
#         print 'init C...'
#
# class D(B, C):
#     def __init__(self, a):
#         super(D, self).__init__(a)
#         print 'init D...'
# 通过多重继承，请定义“会打篮球的学生”和“会踢足球的老师”。
class Person(object):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(Student,BasketballMixin):
    pass

class FTeacher(Teacher,FootballMixin):
    pass

s = BStudent()
print s.skill()

t = FTeacher()
print t.skill()