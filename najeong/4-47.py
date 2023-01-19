# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:47
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-47.py
# @Software: PyCharm

l3=[[(i,j) for i in range(1,6)] for j in range(1,6)]
y = []
for i in range(1,6):
    x = []
    for j in range(1,6):
        a = (i,j)
        x.append(a)
    y.append(x)

print(y)
print(l3)
print(l3[2][1][0])