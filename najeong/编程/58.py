# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 1:51
# @Author : 金泰式,3180300014
# @Site : 
# @File : 58.py
# @Software: PyCharm
'''
1
'''
'''a = {1:"Mon",2:"Tue",3:"Wed", 4: "Thu",5: "Fri",6 :"Sat",7 :"Sun"}
b = int(input())
print(a[b])'''

num = int(input("Enter the number of rows:"))

for n in range(1, num + 1):
    for m in range(0, num - n + 1):
        print(' ', end='')
    B = 1
    for m in range(1, n + 1):
        print(' ', B, sep='', end='')
        BC = B * (n - m) // m
    print()
