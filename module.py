# -*- coding: utf-8 -*-

'a test module'
import sys

from PIL import Image

__author__ = 'zyu'

def test():
    args = sys.argv
    if len(args)==1:
        print('hello')
    elif len(args)==2:
        print('hello, %s' % args[1])

    else:
        print('too mant arg')

if __name__=='__main__':
    test()

im = Image.open('C:\\Users\\chenjie\\Desktop\\mac.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('C:\\Users\\chenjie\\Desktop\\mac2.jpg','JPEG')

print(sys.path)

