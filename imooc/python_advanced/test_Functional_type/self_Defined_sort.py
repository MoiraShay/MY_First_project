#_*_coding:utf-8_
__author__ = 'mamadongpei'

print 'python内置的sorted 函数,可以对list或者是字符串进行排序。'
print sorted([2,3,7,1])#
print sorted(['bob','about','Zoo','Credit'])
print '如果我们要实现倒序排,自定义排序函数'
def reversed_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1

    return 0
print sorted([36,5,12,9,21],reversed_cmp)
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)