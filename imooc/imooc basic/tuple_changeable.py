#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#list：['A', 'B']。list作为一个整体是tuple的第3个元素
t=('a','b',['A','B'])
print t
L=t[2]
print L
#修改list的元素
L[0]='X'
L[1]='Y'
print t
#我们把list的元素'A'和'B'修改为'X'和'Y'后，表面上看，tuple的元素确实变了，但其实变的不是 tuple 的元素，而是list的元素。
t=('a','b',['A','B'])
print t
#让tuple内容不可变(['A', 'B']是list，因此内容可变，但('A', 'B')的内容是不可变的。)
t=('a','b',('A','B'))
print t