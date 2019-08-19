#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('single quotes')
print("double quotes")
print('use \\\' to escape the sigle quote')
print(r'C:\user\username')
print('\u4e2d\u6587\u000d\u000a')
print("""\
Usage: thingy [OPTIONS]
    -h
    -H hostname\
""")
print(3*'abc'+'def')
print('this is a long text'
        'long text long text long text')

s = 'Life is short, you need Python!'
print(s[0])
print(s[0:5])
print(s[0:10:2])
print(s[-1])
print(s[-1:-8])
print(s[-8:-1])
print(s[-8:-1:2])
print(s[-1:-8:-2])
print(s[::-1])
print(len(s))