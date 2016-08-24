#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#我们可以给一个实例绑定很多属性，如果有些属性不希望被外部访问到怎么办？
#Python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头(__)，该属性就无法被外部访问
class Person(object):
    pass
    def __init__(self,name,score):
        self.name=name
        # self._title='Mr'
        #只有双下划线才能设置权限
        # self.__job='Student'
        self.__score=score
p=Person('Bob',99)
print p.name
try:
   print p.__score
except:
  print 'attributerError'
# print p._title
# print p.__job
