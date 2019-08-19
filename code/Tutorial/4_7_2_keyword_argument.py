#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                         # 1 positional argument
parrot(voltage=1000)                                 # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOOM')           # 2 keyword arguments
parrot(action='VOOOOOOM', voltage=1000000)           # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')        # 3 positional arguments
parrot('a thousand', state='pushing up the daisies') # 1 positional, 1 keyword