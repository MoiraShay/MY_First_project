#_*_coding:utf-8_
__author__ = 'mamadongpei'
# reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，
# reduce()传入的函数 f 必须接收两个参数，
# reduce()对list的每个元素反复调用函数f，并返回最终结果值。
def f(x,y):
    return x+y
print reduce(f,[1,3,5,7])
# 还可以接收第3个可选参数，作为计算的初始值。如果把初始值设为100，计算：
print reduce(f,[1,3,5,7,9],100)
def product(x,y):
    return x*y
print reduce(product,[2,4,5,7,12])