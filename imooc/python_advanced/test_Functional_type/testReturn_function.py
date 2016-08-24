#_*_coding:utf-8_
__author__ = 'mamadongpei'
def calc_prod(list1):
    def lazy_prod():
        def f(x,y):
            return x*y
        return reduce(f,list1,1)
    return lazy_prod()
f=calc_prod([1,2,3,4])
print f