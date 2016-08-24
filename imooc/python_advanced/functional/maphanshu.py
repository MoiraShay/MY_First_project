 #_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#利用map()函数，可以把一个 list 转换为另一个 list，只需要传入转换函数。(map()函数不改变原有的 list，而是返回一个新的 list。)
#它可以处理包含任意类型的 list，只要传入的函数f可以处理这种数据类型
#例如，对于list [1, 2, 3, 4, 5, 6, 7, 8, 9]如果希望把list的每个元素都作平方，就可以用map()函数：
L=[1,2,3,4,5,6,7,8,9]
def f(x):
   return x*x
print map(f,L)
#任务假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：
# 输入：['adam', 'LISA', 'barT']
# 输出：['Adam', 'Lisa', 'Bart']
L=['adam', 'LISA', 'barT']
# def f(L):
#     for i in range(0,len(L)):
#        L[i].[0].upper()+L[i].[1:].lower()
# print map(f,L)
def format_name(s):
    return s[0].upper() + s[1:].lower()
print map(format_name, ['adam', 'LISA', 'barT'])