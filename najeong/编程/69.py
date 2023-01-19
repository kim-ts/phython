# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 4:36
# @Author : 金泰式,3180300014
# @Site : 
# @File : 69.py
# @Software: PyCharm

a = int(input())
b = input()
a = list(hex(a))
s = 0
for i in range(len(a)):
    if a[i] == b:
        s += 1
print(s)