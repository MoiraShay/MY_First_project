#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#要表示有理数，可以用一个Rational类来表示：
#p、q 都是整数，表示有理数 p/q。
#两个整数的最大公约数等于其中较小的数和两数的相除余数的最大公约数
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    #如果要让Rational进行+运算，需要正确实现__add__：
    #Rational类虽然可以做加法，但无法做减法、乘方和除法，请继续完善Rational类，实现四则运算。
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __sub__(self, r):
        return Rational(self.p * r.q -self.q * r.p, self.q * r.q)
    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)
    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)
    def __str__(self):
        g=gcd(self.p,self.q)
        return '%s/%s' % (self.p/g, self.q/g)
    __repr__ = __str__
#Rational(1,2)表示有理数1/2，Rational(1,4)表示有理数1/4
r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 -r2
print r1*r2
print r1/ r2
