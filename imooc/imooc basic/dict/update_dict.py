#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#更新dict
#我们可以随时往dict中添加新的 key-value。比如已有dict：
d={
    'adam':95,
    'lisa':85,
    'bart':59
}
print d
#给dict添加新元素
d['pual']=72
print d
#如果 key 已经存在，则赋值会用新的 value 替换掉原来的 value：
d['bart']=60
print d
