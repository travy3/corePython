import types

std1 = {'name':'zyu','score':98}

def print_score():
    print('%s : %s' % (std1['name'],std1['score']))

print(print_score())

class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score2(self):
        print('%s : %s ' % (self.name,self.score))

zyu = Student('zyu dfd',100)
lisa = Student('lisa rong',12)
zyu.print_score2()

print(zyu)
zyu.age=27
print(zyu.age)

#访问权限
class Student2(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score2(self):
        print('%s : %s ' % (self.__name,self.__score))

    def set_score(self,score):
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

asd = Student2('bmw',84)
print(asd.get_name())
asd.set_score(82)
print(asd.get_score())
#asd._Student2__name 也可以直接访问
# _name 代表我虽然可以被外部访问，但请视我为私有
print(asd._Student2__name)

#继承多态

class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    def run(self):
        print('dog is running')
class Cat(Animal):
    pass

dog = Dog()
print(dog.run())

print(isinstance(dog,Animal))

def run_twice(animal):
    animal.run()
    animal.run()

print(run_twice(Animal()))
print(run_twice(Dog()))

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly')

print(run_twice(Tortoise()))

#获取对象信息

print(type(123))

print(type(dog))
def fn():
    pass

print(type(fn)==types.FunctionType)
#dir 获取对象所有属性 方法
print(dir(Dog))

print(hasattr(dog,'run'))
print(dog.run())
print(setattr(dog,'sleep','Ooooo'))
print(getattr(dog,'sleep'))
print(dog.sleep)

# 实例属性和类属性
print(type(Dog))


