#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
#我们把名字称为key，对应的成绩称为value，dict就是通过 key 来查找 value。
#dict是字典的意思
print u'''花括号 {} 表示这是一个dict，然后按照 key: value, 写出来即可。最后一个 key: value 的逗号可以省略。

由于dict也是集合，len() 函数可以计算任意集合的大小：'''
#写一个字典（用于表示名字和成绩的对应关系）
d={
    'adam':95,
    'lisa':85,
    'bart':59,
    'pual':75
}
print d
#由于dict也是集合，len() 函数可以计算任意集合的大小：
print len(d)
#访问字典:d[key];
#list 必须使用索引返回对应的元素，而dict使用key：
print d['pual']
print d['bart']
print u'''通过 key 访问 dict 的value，如果key不存在，会直接报错：KeyError。要避免 KeyError 发生，有两个办法：
一是先判断一下 key 是否存在，用 in 操作符;二是使用dict本身提供的一个 get 方法，在Key不存在的时候，返回None：'''
#避免keyerror方法一：使用in操作符
if 'pual' in d:
    print d['pual']
if 'bart' in d:
    print d['bart']
#避免keyerror方法二：二是使用dict本身提供的一个 get 方法，在Key不存在的时候，返回None
print d.get('bart')
#liss不存在，所以返回none
print d.get('liss')
#;;;;;
d={
    'd':3,
    'e':4,
    'f':5
}
if 'd' in d:
    print d['d']
    print d