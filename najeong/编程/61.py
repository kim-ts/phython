# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 2:16
# @Author : 金泰式,3180300014
# @Site : 
# @File : 61.py
# @Software: PyCharm
'''
1,5,9,3,9,1,1,7,5,7,7,3,3,1,5,7,4,4,5,4,9,5,10,9
'''
a = input().split(",")
k = []
for i in range(1,11):
    n = 0
    for j in a:
        if i == int(j):
            n += 1
    if n == 0 and i > 5:
        k.append(i)
for i in range(len(k)):
    print(k[i],end=' ')