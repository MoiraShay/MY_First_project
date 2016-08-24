#_*_coding:utf-8_
__author__ = 'mamadongpei'
import math
# filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，
# 这个函数 f 的作用是对每个元素进行判断，返回 True或 False，
# filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
def is_not_empty(s):
    # s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。
    return s and len(s.strip()) > 0
print filter(is_not_empty,['test',None,'','str',' ','END'])
def is_not_integer(num):
   # math.sqrt()返回结果是浮点数。
   r=int(math.sqrt(num))
   return r*r == num
print filter(is_not_integer,range(1,101))
