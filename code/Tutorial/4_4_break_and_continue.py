#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in range(10):
    if i % 2 == 0:
        continue
    for j in range(10):
        print(i, j) 
        if i == j:
            break
else:
    print('end of for loop')