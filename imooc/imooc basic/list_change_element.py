#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
L=['adam','lisa','bart']
#对list中的某一个索引赋值，就可以直接用新的元素替换掉原来的元素，list包含的元素个数保持不变
L[2]='niu'
print L
#倒序还可以表示为
L[-1]='BART'
print L
#替换元素
L = ['Adam', 'Lisa', 'Bart']
L[0]='Bart'
L[2]='Adam'
print L