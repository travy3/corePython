from enum import Enum, unique
from types import MethodType

# 使用__slots__
# from django.db.models import Model


class Student(object):
    #只对当前类实例起作用，对继承无效
    # __slots__=('name','age')
    pass

s = Student()
s.name = 'travy'
print(s.name)

def set_age(self,age):
    self.age = age

s.set_age = MethodType(set_age, s)
s.set_age(27)
print(s.age)

s2 = Student()
# print(s2.age)

def set_score(self,score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)

#使用@property
class Student2(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')
        if value < 0  or value > 100 :
            raise ValueError('score must between 0 ^ 100')
        self.__score = value

s = Student2()
s.score = 11
print(s.score)
print(dir(Student2))

class Student3(object):
    def __init__(self,name):
        self.__name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.__name
    __repr__ = __str__

print(Student3('qwe'))

s = Student3('g')
print(s)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0 ,1

    def __iter__(self):
        return self
    def __next__(self):
        self.a ,self.b = self.b,self.a+self.b
        if self.a >10000:
            raise StopIteration()
        return self.a



    def __getitem__(self, item):
       if isinstance(item,int):
            a,b =1,1
            for x in range(item):
                a,b = b,a+b
            return a
       if isinstance(item,slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x>= start:
                    L.append(a)
                a,b = b,a+b
            return L



for n in Fib():
    print(n)
print(Fib()[5])
print(Fib()[1:6])

class Student4(object):
    def __init__(self,name):
        self.name = name

    def __getattr__(self, item):
        if item == 'score':
            return 99
        raise  AttributeError('\'Student\' object has no attribute \'%s\'' % item)

    def __call__(self, *args, **kwargs):
        print('student \'s name: %s' % self.name)

sv = Student4('vbcv')
print(sv.name)
print(sv.score)
# print(sv.abc)

class Chain(object):

    def __init__(self,path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path,path))

    def __str__(self):
        return self._path

    __repr__=__str__

print(Chain().status.user.timeline.list)

print(sv())

print(callable(sv))

#枚举类

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
    print(name, '-->',member,',',member.value)

@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Mon.value)

#使用元类 metaclass

def fn(self, name='world'):
    print('hello %s' % name)

Hello = type('Hello',(object,), dict(hello=fn))

h = Hello()

print(h.hello())

class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return  type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
    pass

l = MyList()
l.add(1)
print(l)

#ORM

class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self,name):
        super(StringField, self).__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField, self).__init__(name,'bigint')

class ModelMetaclass(type):

    def __new__(cls, name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        print('found model: %s' % name)
        mappings=dict()

        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k]=v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__']=mappings
        attrs['__table__']= name
        return  type.__new__(cls,name,bases,attrs)


class Model(dict,metaclass=ModelMetaclass):

    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k , v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k , None))

        sql = 'insert into %s (%s) VALUES (%s)' % (self.__table__,','.join(fields),','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
u = User(id=123,name='zyu',email = 'qwre@qq.com', password = '123123123')

u.save()
