#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : ${DATE} ${TIME}
@Author  : Soner
@version : 1.0.0 
@license : Copyright(C), Your Company
'''

'''
rows = int(input('边长：'))

for i in range(0,rows):
    for k in range(0,rows):
        print(" * ", end='')
        i+= 1
    k+= 1
    print('\n')

'''

'''
# 写回字
rows = int(input('边长：'))
for i in range(0, rows):
    for k in range(0, rows):
        if i !=0 and i !=rows-1 and i !=1 and i !=rows-2:
            if k ==0 or k ==rows-1 or k ==1 or k ==rows-2:
                print(" * ", end='')
            else:
                print("   ", end='')
        else:
            print(" * ", end='')
        k+=1
    i+=1
    print('\n')
'''

# 空心正方形
rows = int(input('边长：'))
for i in range(0, rows):
    for k in range(0, rows):
        if i !=0 and i !=rows-1:
            if k ==0 or k ==rows-1:
                print(" * ", end='')
            else:
                print("   ", end='')
        else:
            print(" * ", end='')
        k+=1
    i+=1
    print('\n')


