from math import sqrt

from functools import reduce

import functools

import module

print(abs)
print(abs(-10))

#函数名也是变量
f = abs
print(f(-20))
#修改了指向绝对值函数的变量值abs
# abs = 100

print(abs)
print(f(-8))
print(abs(-9))

#传入函数

def add(x,y,f):
    return f(x)+f(y)

print(add(-5,6,abs))

def same(x=[],*fs):
    s = [f(xTmp) for xTmp in x for f in fs]
    return s
print(same([2,3,4],sqrt,abs))

#map() reduce()

def f(x):
    return x * x

l = [1,2,3,4,5]
a= map(f,l)

print(list(a))
print(list(map(str,l)))

def fn(x,y):
    return x * 10 +y
print(reduce(fn,l))

def str2int(s):
    def fn(x,y):
        return x *10 +y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2num,s))

print(str2int('123542'))

#filter

def is_old(n):
    return n %2 ==1

print(list(filter(is_old,[1,2,3,4,5,6,7])))

# 素数计算start
def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield  n

def _not_divisible(n):
    return  lambda x : x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

#end

#sorted

print(sorted([3,2,-5,1,2,4],key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))

#返回函数 闭包 延长了局部变量/参数的生命周期
def lazy_sum(*args):
    def calc_sum(*args):
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return calc_sum

f = lazy_sum()

print(f(1,2,3,4))

#闭包
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量 ex

def count():
    fs = []
    for i in range(1,4):
        def f():
            # 由于函数f并非立即执行，所以i变为3 导致结果为9
            return i * i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())


def count1():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3 = count1()
print(f1())
print(f2())
print(f3())

#匿名函数 lambda

print(list(map(lambda x: x * x ,[1,2,3,4,5,6])))

f = lambda x: 2 * x
print(f)
print(f(5))

def build(x,y):
    return lambda : x * x + y * y


#装饰器 增强函数

def now():
    print('2015-3-25')

f = now

print(f())

print(now.__name__)
print(f.__name__)

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return  func(*args,**kw)
    return wrapper
@log
def now():
    print('2016')

print(now())

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return  func(*args,**kw)
        return wrapper
    return decorator

@log2('hello')
def now():
    print('zyu')

print(now.__name__)

#偏函数 把函数的某些参数固定住

int2 = functools.partial(int,base=2)
print(int2('10000'))
print(int2('10000',base=6))
print('asd')
print(module.test())

