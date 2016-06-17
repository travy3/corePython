# help(abs)

# print(max(1,2,3,4))

print(bool(0))
# 函数赋值，设置函数别名，可以直接调用别名
a = max
print(a(3,4,5,6,7))

#定义函数
def my_abs(x):
    if x >= 0 :
        return x
    else:
        return -x



#空函数 pass 返回None

def my_zyu(age):
    if not isinstance(age,(int,float)):
        raise TypeError('bad operand type')
    if age > 18:
        return age
    else:
        pass

# print(my_zyu('d'))

# 必选参数在前，默认参数在后
def power(x,n=2):
    s =1
    while n>0:
        n = n-1
        s = s*x
    return s
print(power(5,2))

power(5)

def add_end(L=[]):
    L.append('end')
    return L

print(add_end([1,2,3]))
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
add_end()
print(add_end())
def add_end2(L=None):
    if L is None:
        L = []
    L.append('end')
    return L

add_end2()
add_end2()
print(add_end2())

#可变参数 传入参数前加* 表示把list或者tuple 作为可变参数传入
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n

    return sum
print(calc([1,2,3]))

def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc2(1,2,3))

#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name,age,**kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('zyu',27)
person('zyu',27,city='sjz',sex='m')

extra = {'city': 'Beijing', 'job': 'Engineer'}

person('zyu',27,**extra)



def person2(name,age,**kwargs):
    if 'city' in kwargs:
        pass
    elif 'job' in kwargs:
        pass
    print('name:', name, 'age:', age, 'other:', kwargs)

person2('zyu',27,asd='asd')

person2('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
#命名关键字参数
#关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person3(name,age,*,city,job):
    print(name, age, city, job)
person3('Jack', 24, city='Beijing', job='Engineer')

def person4(name,age,*args,city,job):
    print(name, age, args, city, job)

person4('Jack', 24, (1,2,3),city='qwe',job='asd')

#组合参数 顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def f1(a,b,c=0,*args,**kwargs):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kwargs)

def f2(a,b,c=0,*,d,**kwargs):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kwargs)

#递归函数

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(3))
