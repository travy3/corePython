#错误，调试，测试

#断言
import logging
import unittest

logging.basicConfig(level=logging.INFO)


def foo(s):
    n  = int(s)
    assert  n != 0,'n is zero!'
    return 10/n

def main():
    foo('0')

# main()

s = '1'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

class Dict(dict):

    def __init__(self,**kw):
        super().__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value


class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

if __name__ == '__main__':
    unittest.main()


#文档测试

