import itertools

natuals = itertools.count()
# for n in natuals:
#     print(n)

cs = itertools.cycle('ABC')
# for c in cs :
#     print(c)

ns = itertools.repeat('A',3)
for n in ns:
    print(n)

ns = itertools.takewhile(lambda x :x<10, natuals)
print(list(ns))

for c in itertools.chain('asd','qwe') :
    print(c)

for key,group in itertools.groupby('AAABBBCCAAA'):
    print(key,list(group))