#_*_coding:utf-8_*_
import math#math包提供了sin()和 cos()函数，我们先用import引用它
__author__ = 'mamadongpei'
#7.2.调用函数（Python很多内置函数，可以直接调用）
#求绝对值的函数abs()
print abs(100)
print abs(-20)
#abs('a')(错误的参数类型)
#比较函数cmp(x,y)(比较函数 cmp(x, y) 就需要两个参数，如果 x<y，返回 -1，如果 x==y，返回 0，如果 x>y，返回 1：)
print cmp(1,2)
print cmp(1,1)
print cmp(2,1)
#Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
print int('123')
print int(12.5)
print int(12.34)
print int(0.4)
#str()函数把其他类型转换成str
#str()一般是将数值转成字符串。
#打印str(1240)的数据类型
print type(str(1240))
print str(1240)
print str(1.23)
#实战（sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。）
L=[]
x=1
#首先，可以用 while 循环构造出 list。（追加）
while x<=100:
    L.append(x*x)
    x=x+1
print sum(L)
print unicode(100)
print type(unicode(100))
#7.3编写函数
#在Python中，定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。
#示例：定义一个也求绝对值得函数my_abs()
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
#调用函数并给函数传递实际参数5：print my_abs(5)
#实例
def square_of_sum(L):
    sum=0
    for x in L:
        sum=sum+x*x
    return sum
print square_of_sum([1,2,3,4,5])
#函数返回多值（ython的函数返回多值其实就是返回一个tuple，但写起来更方便。）
## math包提供了sin()和 cos()函数，我们先用import引用它
#`实例：比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标
def move(x,y,step,angle):
    nx=x+step*math.cos(angle)## math包提供了sin()和 cos()函数，我们先用import引用它
    ny=y-step*math.sin(angle)#step代表位移
    return nx,ny
print move(100,100,60,math.pi/6)
#7.4函数返回多值（ython的函数返回多值其实就是返回一个tuple，但写起来更方便。）
r=move(100,100,60,math.pi/6)
print r
#实例一元二次方程的定义是：ax² + bx + c = 0请编写一个函数，返回一元二次方程的两个解。
def quadratic_equation(a, b, c):
    t = math.sqrt(b * b - 4 * a * c)
    return (-b + t) / (2 * a),( -b - t )/ (2 * a)
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)
#7.5递归函数（自己调用自己）
#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
#示例计算阶乘 n! = 1 * 2 * 3 * ... * n，用函数 fact(n)表示，可以看出：
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print fact(100)
#使用递归函数需要注意防止栈溢出stack
#实例：汉诺塔的移动也可以看做递归函数
def move(n,a,b,c):
    if n==1:
        print a,'-->',c
        return
#表示的是将n-1的盘子从a柱子上面移到b柱子上面去
    move(n-1,a,b,c)
#输出最下面个盘子移从a移到c的路径
    print a,'-->',c
#将b柱子上面的n-1个盘子移动到c柱子上面
    move(n-1,b,a,c)
move(4,'A','B','C')
#7.6定义默认参数
#例：例如Python自带的 int() 函数，其实就有两个参数，我们既可以传一个参数，又可以传两个参数：
#int()函数的第二个参数是转换进制，如果不传，默认是十进制 (base=10)，如果传了，就用传入的参数。
print int('123')
print int('123',8)#123转换成八进制
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print power(5)
#实例:请定义一个 greet() 函数，它包含一个默认参数，如果没有传入，打印 'Hello, world.'，如果传入，打印 'Hello, xxx.'
def greet(name='world'):
    print 'hello,'+ name +'.'
greet()
greet('bart')
#7.7定义可变参数
#如果想让一个函数能接受任意个参数，我们就可以定义一个可变参数：
#可变参数的名字前面有个 * 号，
#Python解释器会把传入的一组参数组装成一个tuple传递给可变参数，因此，在函数内部，直接把变量 args 看成一个 tuple 就好了。
def average(*args):
    sum=0.0
    if len(args)==0.0:
        return sum
    for x  in args:
        sum=sum+x
    return sum/len(args)
print average(0)
print average(1,2)
print average(1,2,2,3,4)
print average(1,2,2)


