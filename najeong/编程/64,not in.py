# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 2:46
# @Author : 金泰式,3180300014
# @Site : 
# @File : 64,not in.py
# @Software: PyCharm
"""
[4,7,5,6,8,6,9,5]
"""
a = eval(input())
b = []
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(i,end=' ')