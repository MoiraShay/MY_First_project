#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#1.生成list
print range(1,11)
#生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
# 方法一是循环
L=[]
for x in range(1,11):
    L.append(x*x)
print L
#方法二：列表生成式
#这种写法就是Python特有的列表生成式。利用列表生成式，可以以非常简洁的代码生成 list。
L=[x * x for x in range(1,11)]
print L
#丽君的练习
n = [3, 5, 7]
def double_list(x):
   for i in range(0, len(n)):
       x[i] = x[i] * 2
# Don't forget to return your new list!
   return x
print double_list(n)
#任务：请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
#range(1, 100, 2) 可以生成list [1, 3, 5, 7, 9,...]
L=[x*(x+1) for x in range(1,100,2)]
print L
#2. 负责表达式
#使用for循环的迭代不仅可以迭代普通的list，还可以迭代dict。
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
#完全可以通过一个复杂的列表生成式把它变成一个 HTML 表格
#注：字符串可以通过 % 进行格式化，用指定的参数替代 %s。字符串的join()方法可以把一个 list 拼接成一个字符串。
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'