#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#list添加新元素
L=['adam','lisa','bart']
#给list添加新元素Paul方法一（把新元素追加到list的末尾）
L.append('Paul')#append()总是把新的元素添加到 list 的尾部。
print L
#给list添加新元素Paul方法二(把新元素追加到list的第一位)方法是用list的 insert()方法，它接受两个参数，第一个参数是索引号，第二个参数是待添加的新元素：
L.insert(0,'paul')
print L
#练习
L.insert(2,'jim')
print L