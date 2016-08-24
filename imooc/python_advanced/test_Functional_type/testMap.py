#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#map()函数,是python内置的高阶函数,接收的参数:一个函数 f，一个list
# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。

# 例如，对于list [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 如果希望把list的每个元素都作平方，就可以用map()函数：
def square(x):
    return x*x
#利用map()函数，可以把一个 list 转换为另一个 list，只需要传入转换函数。
print map(square,[1,2,3,4,5,6,7,8,9])
def format_name(s):
    return s.title()
# title方法是将一个字符串中的每个单词的第一个字母大写，其余的字母小写，如果一个人名是  name = 'john snow'; name.title() 会返回 'John Snow'，而 capitalize 是将整个字符串的第一个字母大写，其余的字母小写，name.capitalize() 会返回 'John snow'

print map(format_name,['adam', 'LISA', 'barT'])