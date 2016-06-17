# -*- coding: utf-8 -*-
import json
import os
import pickle
import string
from io import StringIO,BytesIO

try:
    f = open('D:\qwasd.txt','r')
    print(f.read())
finally:
    if f:

        f.close()


with open(r'D:\账号.txt','r',encoding='utf-8',errors='ignore') as f:
    for line in f.readlines():
        print(line.strip())
    while f.readline()!='':
        print(line.strip())
    # print(f.read())

f = open('D:\qwasd.txt','w')
f.write('i \'m come in')
f.close()

with open ('D:\qwasd.txt','w') as f:
    f.write('hello world')

#StringIO BytesIO

f = StringIO('Hello!\nHi!\nGoodbye!');
# f.write('hey hello')
while True:
    s = f.readline()
    if s =='':
        break
    print(s.strip())

b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())

#操作文件，目录

print(os.name)
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
print(os.path.join('D:\\','testdir'))
# os.mkdir('D:\\testdir')
# os.rmdir('D:\\testdir')

print(os.path.split('/Users/michael/testdir/file.txt'))

l = [x for x in os.listdir('.') if os.path.isdir(x)]
print(l)
l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(l)

#序列化
d = dict(name='Bob', age=20,score=88)
print(pickle.dumps(d))

f= open('D:\\abs.txt','wb')
pickle.dump(d,f)
f.close()

b = open('D:\\abs.txt','rb')
a = pickle.load(b)
print(a)

#json

g = dict(name='bmw', type='3')
kk =json.dumps(g)
print(kk)
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

class Student(object):

     def __init__(self,name,age,score):
         self.name = name
         self.age = age
         self.score = score

s = Student('Bob',20,81)
# print(json.dumps(s))

def student2dict(std):
    return {
        'name': std.name,
        'age':std.age,
        'score': std.score
    }

print(json.dumps(s,default=student2dict))
print(json.dumps(s,default=lambda  obj:obj.__dict__))
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])




print(json.loads(json_str,object_hook=dict2student ))

