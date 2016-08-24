#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#1.迭代
# 在Python中，迭代是通过 for ... in 来完成的
#迭代通过for循环遍历list,tuple,等任何可迭代对象上
'''迭代操作就是对于一个集合，无论该集合是有序还是无序，我们用 for 循环总是可以依次取出集合的每一个元素。
注意: 集合是指包含一组元素的数据结构，我们已经介绍的包括：
1. 有序集合：list，tuple，str和unicode；
2. 无序集合：set
3. 无序集合并且具有 key-value 对：dict'''
#迭代与按下标访问数组最大的不同是，后者是一种具体的迭代实现方式，而前者只关心迭代结果，根本不关心迭代内部是如何实现的。
for n in range(1,101):
        if n % 7==0:
           print n
#2.索引迭代
#在for循环中拿到有序集合的索引，怎么办？方法是使用enumerate()函数
L=['Adam','Lisa','Bart','Pual']
#使用 enumerate() 函数，我们可以在for循环中同时绑定索引index和元素name,实际上迭代的每个元素是一个tuple,
#enumerate() 函数自动把每个元素变成 (index, element) 这样的tuple，再迭代，就同时获得了索引和元素本身
for t in enumerate(L):
    index = t[0]
    name = t[1]
    print index, '-', name
#每个tuple元素都包含两个元素，for循环又可以进一步简写为：
for index,name in enumerate(L):
    print index,'-',name
#索引迭代任务
L=['A','B','C']
for index,name in zip(range(1,len(L)+1),L):
    print index,'-',name
#3.迭代dict的value:两种方法
d={'Adam':95,'Lisa':85,'Bart':59}
print d.values()
for v in d.values():
    print v
#dict除了values()方法外，还有一个 itervalues() 方法，（values() 方法实际上把一个 dict 转换成了包含 value 的list。但是 itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存。）
d={'Adam':95,'Lisa':85,'Bart':59}
print d.itervalues()
for v in d.itervalues():
    print v
#请计算所有同学的平均分。
d={'Adam':95,'Lisa':85,'Bart':59,'pual':74}
sum=0.0
for v in d.itervalues():
     sum=sum+v
print sum/len(d)
#4.迭代dict 的key 和value
#在一个 for 循环中同时迭代 key和value。
d={'Adam':95,'Lisa':85,'Bart':59,'pual':74}
#items() 方法把dict对象转换成了包含tuple的list，我们对这个list进行迭代，可以同时获得key和value：
print d.items()
for key,value in d.items():
    print key,":",value
#任务
d={'Adam':95,'Lisa':85,'Bart':59,'pual':74}
sum=0.0
for key,value in d.iteritems():
    print key,":",value
    sum=sum+value
print "average",":",sum/len(d)