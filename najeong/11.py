# -*- coding = utf-8 -*-
# @Time : 2022-06-15오후 7:23
# @Author : 金泰式,3180300014
# @Site : 
# @File : 11.py
# @Software: PyCharm

import itertools
a = input()
b = []
for i in range(1,int(a)+1):
    b.append(i)
b = list(itertools.permutations(b, int(a)))
for i in range(len(b)):
    x = []
    for j in range(len(b[i])):
        x.append(b[i][j])
    y = []
    for n in range(len(x)):
        y.append((10**(len(x)-n-1))*x[n])
    s = 0
    for i in range(len(y)):
        s += y[i]
    print(s)