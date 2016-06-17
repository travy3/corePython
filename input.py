# -*- coding: utf-8 -*-
print('\"1024\" * \"768\" = \'',1024*768,'\'')
a =-100
if a>=0:
    print(a)
else:
    print(-a)

#数据类型和变量
#\转义
print('\\\t\\')
#\r'' 阻止转义
print(r'\\\\\\')
# '''...'''表示多行内容
print('''line1
      ...line2
      ...line3''')

print(not 1>2)
print(True or False)
print(True and False)
age = 15
if age >= 16:
    print('adult')
else:
    print('teenager')

# None 空值
# PI大写表示常量
PI = 3.14
PI  = True
print(PI)

# // 除法最精确 永远是整数 Python 整数没有大小限制 但超出一定范围 表示为inf（无限大）
print(10 // 3)

print(ord('c'))

print(chr(66))
# 网络传输 或者保存硬盘，需要把str变为以字节为单位的 bytes
# Python对bytes类型的数据用带b前缀的单引号或双引号表示
X = b'ABC1'

print('abc'.encode('utf-8'))
print(b'abc'.decode('utf-8'))

# len字符长度 如果参数是bytes 则计算字节数
print(len('中文'))
print(len('中文'.encode('utf-8')))

print(len(b'abc'))

# 字符格式化a
# %d 整数 %f 浮点数 %s 字符串 %x 十六进制整数  %%转义%
str = 'hello, %s' % ('zyu')

str = 'hi %s , you have $%d' % ('travy',100000)

print(str)
#list 可变有序表
classmates = ['1','2','3']
print(classmates[len(classmates)-1])

classmates.insert(0,'zyu')
print(classmates)

#tuple 元组 一旦初始化，不能修改
s = [1,2,3]
classmates = ('a','b','c',s)

# classmates = ('1',)
print(classmates)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
#条件判断
age =13
if age > 10:
    print("ee")
elif age >20:
    print("ff")
else:
    print("cc")

# s = input('birth:')
# birth = int(s)
# if birth>2000:
#     print('00')
# elif birth>1990:
#     print('90')
# else:print('80')

#循环
for name in L:
    print(name)

print(list(range(5)))

sum = 0
# 缩进4个字节 进入循环体
for x in range(101):
    sum = sum + x
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    x = 'Hello, %s!'% x
    print(x)

# dict 相当于map
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d['adam'] = 100
print(len(d))

print('zyu' in d)
print(d.get('adam'))

x = d.pop('Bob')
print(x)
print(d)
#set
s = set([1,2,3])
print(s)
s.add(4)
print(s)
s.remove(1)
print(s)


