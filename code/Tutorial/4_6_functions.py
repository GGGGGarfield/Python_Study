#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(1000)