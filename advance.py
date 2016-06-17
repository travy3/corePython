from collections import Iterator

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L2)

#generator 生成器

l = [x * x for x in range(10)]
print(l)
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))

def fid(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'
ab = fid(5)
# print(next(ab))
# d(next(ab))
# print(next(ab))
# print(next(ab))
#
# print(next(ab))


while True:
    try:
        x = next(ab)
        print('ab:',x)
    except StopIteration as e:
        print('generator return value:', e.value)
        break

#迭代器
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
print(isinstance([],Iterator))
print(isinstance(iter([]),Iterator))


#小结

#凡是可作用于for循环的对象都是Iterable类型；

#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。