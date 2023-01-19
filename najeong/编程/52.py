# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 12:38
# @Author : 金泰式,3180300014
# @Site : 
# @File : 52.py
# @Software: PyCharm
'''
4
'''
a = int(input())

for i in range(1,a+1):
    for j in range(1,i+1):
        print("%d*%d=%d"%(j,i,i*j),end='  ')
    print()