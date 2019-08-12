#coding: utf-8

from __future__ import print_function

row = 1
column = 1

while row <=9:
	while column <= row:
		print('%d*%d=%d '%(column,row,column*row),end='')
		column += 1
	print('')
	column = 1
	row += 1
