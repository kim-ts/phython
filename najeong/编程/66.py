# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 3:03
# @Author : 金泰式,3180300014
# @Site : 
# @File : 66.py
# @Software: PyCharm
'''
4
1 7 4 1
4 8 3 6
1 6 1 2
0 7 8 9
또는
2
1 7
4 1
또는
3
4    7    8
1    3    3
2    3    1
행에서는 가장크고
열에서는 가장작은 수
'''

a = int(input())
x = []
for i in range(a):
    b = list(input().split())
    x.append(b)
s = 0
for i in range(len(x)):
    for j in range(len(x[i])):
        column = 0
        row = 0
        nc = []
        nr = []
        for k in range(a):
            nc.append(int(x[i][k]))
        nn = max(nc)
        if nn == int(x[i][j]):
            column += 1
        for k in range(a):
            nr.append(int(x[k][j]))
        nrr = min(nr)
        if nrr == int(x[i][j]):
            row += 1
        if row == 1 and column == 1:
            s += 1
print(s)