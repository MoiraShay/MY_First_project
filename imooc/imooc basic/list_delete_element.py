#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#list添加新元素
L=['adam','lisa','bart']
#给list添加新元素Paul方法一（把新元素追加到list的末尾）
L.append('Paul')#append()总是把新的元素添加到 list 的尾部。
print L
#给list添加新元素Paul方法二(把新元素追加到list的第一位)方法是用list的 insert()方法，它接受两个参数，第一个参数是索引号，第二个参数是待添加的新元素：
L.insert(0,'pa')
print L
#练习
L.insert(2,'jim')
print L
#pop()方法总是删掉list的最后一个元素，并且它还返回这个元素，
L.pop()
print L
#pop(i)方法总是删掉list的第i+1个元素，并且它还返回这个元素，
L.pop(2)
print L
#例题（注意到Bart的索引已经从原来的3变成2了）
L.pop(2)
L.pop(2)
print L
