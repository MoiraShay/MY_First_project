#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#5.6获取对象信息
#拿到一个变量，除了用 isinstance() 判断它是否是某种类型的实例外，还有没有别的方法获取到更多的信息呢？
#例如：已有定义
class Person(object):
    def __init__(self,name,gender,**kw):
        self.name=name
        self.gender=gender
        #任务希望除了 name和gender 外，可以提供任意额外的关键字参数，并绑定到实例，请修改 Person 的 __init__()定 义，完成该功能
        #传入**kw即可传入任意数量的参数，并通过setattr()绑定属性
        for k,v in kw.iteritems():
            setattr(self,k,v)
class Student(Person):
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score=score
    def whoAmI(self):
        return 'I am a Student,my name is %s' %self.name
#首先可以用type()函数获取变量的类型，它返回一个type对象：
print type(123)
s=Student('Bob','Male',88)
print type(s)
#其次可以用dir()函数获取变量的所有属性：
print dir(123)
print dir(s)
#ir()返回的属性是字符串列表，如果已知一个属性名称，要获取或者设置对象的属性，就需要用 getattr() 和 setattr( )函数了：
print getattr(s,'name')
#给s改名为adam
setattr(s,'name','Adam')
print s.name
#获取age属性，如果属性不存在，就返回默认值20：
print getattr(s,'age',20)
p = Person('Bob', 'Male', age=18, course='Python')
print p.age
print p.course