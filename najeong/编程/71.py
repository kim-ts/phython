# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 4:44
# @Author : 金泰式,3180300014
# @Site : 
# @File : 71.py
# @Software: PyCharm

a = int(input())
x = []
for i in range(a):
    b = input().split()
    x.append(b)

y = []
z = []
for i in range(len(x)):
    if int(x[i][0]) == 0:
        y.append(x[i])
    else:
        z.append(x[i])
k = []
for i in range(len(x)):
    l = []
    l.append(x[i][1])
    if int(x[i][1]) == 0:
        l.append(z[len(z)-1-i])
    else:
