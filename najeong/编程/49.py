# -*- coding = utf-8 -*-
# @Time : 2022-06-23오후 7:22
# @Author : 金泰式,3180300014
# @Site : 
# @File : 49.py
# @Software: PyCharm

n = int(input())
x = []
for i in range(n):
    z = list(input().split(' '))
    x.append(z)
s = 0
for i in range(len(x)):
    for j in range(len(x[i])):
        if i == j:
            s += float(x[i][j])
        elif i == len(x[i])-j-1:
            s += float(x[i][j])
        else:
            pass

print("{:.2f}".format(s))