
# 摘要算法 md5 sha1
import hashlib

md5 = hashlib.md5()

md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())

# 由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
# 这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”

def calc_md5(password):
    return get_md5(password + 'salt')

def get_md5(str):
    md5.update(str.encode('utf-8 '))
    print(md5.hexdigest())

if __name__=='__main__':
    calc_md5('zy890228')

