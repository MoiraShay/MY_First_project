#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
class Person(object):
    pass
#4.__init__()函数初始化实例属性:在定义 Person 类时，可以为Person类添加一个特殊的__init__()方法，当创建实例时，__init__()方法被自动调用，我们就能在此为每个实例都统一加上以下属性：
#__init__() 方法的第一个参数必须是 self,创建实例时，就必须要提供除 self 以外的参数
#任务：请定义Person类的__init__方法，除了接受 name、gender 和 birth 外，还可接受任意关键字参数，并把他们都作为属性赋值给实例。
#使用**kw定义关键字；
#除了可以直接使用self.name = 'xxx'设置一个属性外，还可以通过 setattr(self, 'name', 'xxx') 设置属性。
    def __init__(self,name,gender,birth,**kw):
        self.name=name
        self.gender=gender
        self.birth=birth
        #解释器内部会将**kw拆分成对应的dict.
        #setattr()方法接受3个参数：setattr(对象，属性，属性的值)
        #setattr(self,k,v)相当于self.k = v
        #kw.iteritems()历遍字典kw的所有key和value，分别匹配k，v
        for k,v in kw.iteritems():
            setattr(self,k,v)
xiaoming = Person('XiaoMing','Male','1991-1-1',job='Student')
xiaohong = Person('XiaoHong','Female','1992-2-2',job='Teacher')
        # return xiaoming.birth
print '小名的生日是：', xiaoming.birth
print '小红的工作是：',xiaohong.job
