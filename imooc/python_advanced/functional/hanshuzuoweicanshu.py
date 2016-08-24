 #_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#函数式functional，是一种编程范式
#2.高阶函数：能接受函数作为参数（把函数通过一个变量传给另外一个函数）
#例：接受abs函数
# 定义一个函数，接收x,y,f三个参数（其中x,y是数值，f是函数）
print abs(-10)
#用参数表示一个函数
f=abs
print f(-20)
def add(x,y,f):
    return f(x)+f(y)
#函数执行的代码实际上是abs(-5)+abs(9)
print add(-5,9,abs)
#2.把函数作为参数
#任务：利用add(x,y,f)函数，计算：x开根号+y开根号
import math
f=math.sqrt
def add(x,y,f):
    return f(x)+f(y)
print add(25,9,f)