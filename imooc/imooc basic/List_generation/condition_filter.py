#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#列表生成式的for 循环后面还可以加上if判断
L=[x * x for x in range(1,11) ]
print L
#只要偶数的平方
L=[x * x for x in range(1,11) if x % 2==0 ]
print L
#任务
def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]
print toUppers(['Hello', 'world', 101])
#3.多层表达式
L=[m+n for m in 'ABC' for n in '123']
print L
#翻译成循环代码就是这样
L=[]
for m in 'ABC':
    for n in '123':
        L.append(m+n)
print L
#任务
#利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
L=[100*n1+10*n2+n3 for n1 in range(1,10) for n2 in range(0,10) for n3 in range(10) if n1==n3]
print L