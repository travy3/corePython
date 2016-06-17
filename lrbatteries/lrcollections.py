from collections import namedtuple, deque ,defaultdict, Counter

p =(1,2)

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

Point = namedtuple('Point', ['x', 'y'])
p = Point(2,3)
print(p.x)

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')

print(q)

# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的

dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

c= Counter()
for ch in 'programming':
    c[ch] = c[ch]+1

print(c)

