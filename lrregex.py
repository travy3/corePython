import re

s = 'ABC\\-001'
print(s)
s1 = r'ABC\-001'
print(s1)

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010-1234 5'))

print(re.split(r'\s+', 'a b    c'))

print(re.split(r'[\s\,\;]+', 'a,b;; c    d'))

#分组

print(re.match(r'0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]', '03'))

m  =re.match(r'^(\d{3})\-(\d{3,8})$' ,'010-1234566')

print(m.group(0))
print(m.group(1))

#贪婪匹配

print(re.match(r'^(\d+)(0*)$', '102300').groups())

print(re.match(r'^(\d+?)(0*)$' , '102300').groups())

#预先编译

re_tele = re.compile(r'^(\d{3})-(\d{3,8})$')

print(re_tele.match('010-3423').groups())