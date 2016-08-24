#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#set内部存储的元素无序，但是元素无重复（有的时候，我们只想要 dict 的 key，不关心 key 对应的 value，目的就是保证这个集合的元素不会重复，这时，set就派上用场了。）
#创建set的方式是调用set()并传入一个list,list的元素将作为set的元素
s=set(['A','B','C'])
print s
#因为set不能包含重复元素，所以set会自动去掉重复的元素
s=set(['A','B','C','C'])
print s
print len(s)
s = set(['Adam','lisa','bart','paul'])
print s
#访问set(由于set存储的是无序集合，所以我们没法通过索引来访问。用 in 操作符判断)
print 'Adam' in  s
print 'adam' in s
#set的特点（只存储key,不存储value）set存储的元素必须是不可变的
#实例：假设我们让用户输入星期一至星期日的某天，如何判断用户的输入是否是一个有效的星期呢
weekdays=set(['MON','TUE','WED','THU','FRI','SAT','SUN'])
x='???'#用户输入的字符串
if x in weekdays:
    print 'input ok'
else:
    print 'input error'
#实例（请设计一个set并判断用户输入的月份是否有效。）
months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
x1 = 'Feb'
x2 = 'Sun'
if x1 in months:
    print 'x1: ok'
else:
    print 'x1: error'
if x2 in months:
    print 'x2: ok'
else:
    print 'x2: error'
#遍历set
s=set(['adam','lisa','bart'])
for name in s:
    print name
#set遍历实例
s=set([('adam',95),('lisa',85),('bart',59)])
#注意到set的元素是tuple，因此 for 循环的变量被依次赋值为tuple(元组)。
for x in s:
    print x[0]+":",x[1]
#更新set
#add()可以直接添加，remove（）需要判断
s=set([1,2,3])
s.add(4)
print s
s.remove(3)
print s
#如果删除的元素不存在set中，remove()会报错
#s.remove(6)
#如果删除的元素不存在set中，remove()会报错，所以remove()要先判断
#实例（针对下面的set，给定一个list，对list中的每一个元素，如果在set中，就将其删除，如果不在set中，就添加进去。）
S=set(['adam','lisa','pual'])
L=['adam','lisa','bart','pual']
for name in L:
    if name in S:
        S.remove(name)
    else: S.add(name)
print S