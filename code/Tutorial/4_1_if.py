#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = input("input a number:")
n = int(n)
if 0 < n:
    print('positive')
elif 0 == n:
    print('zero')
elif 0 > n:
    print('negative')
else:
    print('???')