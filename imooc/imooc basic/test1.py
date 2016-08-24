#_*_coding:utf-8_*_
__author__ = 'mamadongpei'
print 'a,b,c '
print "abc"
print 45678+0x12fd2
print "learn python in imooc"
#ji suan boolean zhi
print 100<99
print 0xff==255
#deng cha shu lie
x1 = 1
d = 3
n = 100
x100 = x1 + (n - 1) * d
s1 = (x1 + x100) * n / 2
print s1
#ding yi zi fu chuan
#zi fu chuan ben shen dai yin hao (danyinhaohuoshuangyinhao)
cata1="I'm ok"
print cata1
cata2='I am "cat girl"'
print cata2
#zhuan yi zi fu
cata3='Bob said \"I\'m ok\" .'
print cata3
s2='python was started in 1989 by \"guido\".\n python is freee and easy to learn.'
print s2
#raw zi fu chuan yu duo hang zi fu chuan
print r'''"To be, or not to be": that is the question.
Whether it is nobler in the mind to suffer.'''
#unicode zi fu chuan(dan yi duo hang wen zi )
print u'''打印多行文字：u
静夜思
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。'''
print u'''Python的整数除法，即使除不尽，结果仍然是整数，余数直接被扔掉
'''
print 1.25+10/4
print 1.25+10.0/4.0
print u'''布尔类型'''
a = 'python'
print 'hello,', a or 'world'

b = ''
print 'hello,', b or 'world'