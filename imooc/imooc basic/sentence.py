#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
'''
缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，更不要混合Tab和空格，否则很容易造成因为缩进引起的语法错误。

注意: if 语句后接表达式，然后用:表示代码块开始。

如果你在Python交互环境下敲代码，还要特别留意缩进，并且退出缩进需要多敲一行回车：
'''
#if....语句
age=20
if age >= 18:
    print 'your age is ',age
    print 'adult'
print 'end'
#exercise
score=75
if score>=60:
    print 'passed'
#if......else语句(else 后面有个“:”)
age=10
if age>=18:
    print 'adult'
else:print 'teenager'
#if-elif-else
score=85
if score>=90:
    print  'eccellent'
elif score>=80:
    print 'good'
elif score>=60:
    print 'passed'
else:
    print 'failed'
#for 循环
#Python的 for 循环就可以依次把list或tuple的每个元素迭代出来
print u'''Python的 for 循环就可以依次把list或tuple的每个元素迭代出来'''
L=['Adam','Lisa','Bart']
#name 这个变量是在 for 循环中定义的，意思是，依次取出list中的每一个元素，并把元素赋值给 name，然后执行for循环体,遍历L）。
for name in L:
    print name
#for 循环遍历 list练习
L=[75,92,59,68]
sum=0.0
for score in L:
    sum=sum+score
    average=sum/4
print average
#while循环
sum = 0
x = 1
while x < 100:
    sum = sum + x
    x = x + 2
print sum
#break 跳出当前循环
sum = 0
x = 1
n = 1
while True:
    x=x*2
    sum=sum+x
    n=n+1
    if n>20:
       break
print sum
#continue跳出本次循环，继续下一次
#for 循环计算平均数
L=[75,98,59,81,66,43,69,85]
sum=0.0
n=0
for x in L:
    sum=sum+x
    n=n+1
print sum/n
#现在只统计合格的平均分
L=[75,98,59,81,66,43,69,85]
sum=0.0
n=0
for x in L:
    if x<60:
        continue
    sum=sum+x
    n=n + 1
print sum / n
#对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：
sum=0
x=0
while True:
    x=x+1
    if x>100:
        break
    if x%2==0:
        continue
    sum=sum +x
print sum
#多重循环
for x in ['A','B','C']:
    for y in ['1','2','3']:
        print x+y
#多重循环练习
for  x in['0','1','2','3','4','5','6','7','8','9']:
    for y in['0','1','2','3','4','5','6','7','8','9']:
        if x<y:
            print 10*x+y
