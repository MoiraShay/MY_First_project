#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
import math
#能接受函数作为参数的函数成为高阶函数即变量名可以指向函数
#下面程序中是把abs函数作为add函数的参数
def  add(x,y,f):
    return f(x)+f(y)
print add(-5,9,abs)
#求开平方根只用换个函数
print add(25,9, math.sqrt)