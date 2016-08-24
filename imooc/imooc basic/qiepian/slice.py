#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#1.对list 切片(tuple也一样0
#实例：取一个list的部分元素
L=['Adam','Lisa','Bart','pual']
#取前3个元素
#笨方法：
print [L[0],L[1],L[2]]
#对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
#对应上面问题用一行代码可以完成切片
print L[0:3]#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
#如果第一个索引是0，还可以省略
print L[:3]
print L[1:3]
print L[2:3]
#只用一个 : ，表示从头到尾：
print L[: ]
#切片操作还可以指定第三个参数：(第三个参数表示每N个取一个，上面的 L[::2] 会每两个元素取出一个来，也就是隔一个取一个。
print L[::2]
print L[0::2]
#任务：请利用切片，取出：
'''请利用切片，取出：

1. 前10个数；
2. 3的倍数；
3. 不大于50的5的倍数'''
L=range(1,101)
print L
print L[0:10]
print L[2::3]
print L[4:50:5]
#2.倒序切片
#记住倒数第一个元素的索引是-1。倒序切片包含起始索引，不包含结束索引。
L = ['Adam', 'Lisa', 'Bart', 'Paul']
print L[-2:]
print L[:-2]
print L[-3:-1]
print L[-4:-1:2]
L=range(1,101)
print L
print L[-10:]
print L[-46::5]
#对字符串切片
str='ABCDEFG'
print str[:3]
print str[-3:-1]
print str[-3:]
print str[::3]
#实例：字符串有个方法upper()可以把字符变成大写字母
print 'xyz'.upper()
#请设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。
#取除首字母外的字符串用[1:]
def firstCharUpper(s):
    return s[0].upper()+s[1:]
print firstCharUpper('sunshine') +"  "+firstCharUpper('boy')

