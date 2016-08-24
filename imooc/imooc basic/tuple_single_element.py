#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#包含 0 个元素的 tuple，也就是空tuple，直接用 ()表示
t=()
print t
#创建包含1个元素的 tuple(Python 规定，单元素 tuple 要多加一个逗号“,”,避免因为()既可以表示tuple，又可以作为括号表示运算时的优先级，结果 (1) 被Python解释器计算出结果 1，导致我们得到的不是tuple，而是整数 1)
t=(1,)
print  t
#单元素tuple必须加上额外的逗号
m=('Adam',)
print m
m=('Adam')
#没有逗号不能创建包含一个元素的tuple
print m