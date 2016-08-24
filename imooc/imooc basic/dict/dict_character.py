#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#dict字典的特性
# 特性一：查找快速(无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。
#dict缺点是占用内存大，list占内存小
#dict 是按key查找的，所以key不能重复
#dict第二个特点就是存储的key-value序对是没有顺序的,内部是无序的，不能用dict存储有序的集合。
#dict第三特点：key的元素不可变
#根据名字查询
d={
    'adam':95,
    'lisa':85,
    'bart':59
}
print d
#＃根据分数查询
d={
    95:'adam' ,
    85:'lisa' ,
    59:'bart'
}
d[71]='pual'
print d


