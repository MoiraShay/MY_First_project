#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了
#创建tuple和创建list唯一不同之处是用( )替代了[ ]。
T=('adam','lisa','bart')
print T
#获取 tuple 元素的方式和 list 是一模一样的，我们可以正常使用 t[0]，t[-1]等索引方式访问元素，但是不能赋值成别的元素
print T[2]
#Python2.7的str（）函数没有作用呢，我刚运行print str（1234），输出来还是1234，不带引号，并没有转化成字符串
def print_plus(arg):
    print arg, type(arg)
#调用重构后的函数：
a = str(1234)
b = "ALICE"
print a
print b
# print type（str）
##这样就知道 str() 有效果了。
#str是将所有值转换为字符串，相当tostring()，而repr则是相当于编译器，转换后的内容是给编译器看的
print repr("abc")
print str("abc")