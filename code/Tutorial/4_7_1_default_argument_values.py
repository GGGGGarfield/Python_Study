#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ask_ok(prompt, retries=4, reminder='please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        elif ok in ('n','no','nop','nope'):
            return False
        else:
            retries = retries-1
            if retries < 0:
                raise ValueError('invalid user response')
            print(reminder)

try:
    ask_ok('Do you really want to quit?')
except ValueError as e:
    print(e.__str__())