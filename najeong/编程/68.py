# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 3:44
# @Author : 金泰式,3180300014
# @Site : 
# @File : 68.py
# @Software: PyCharm

a = eval(input())
b = eval(input())


for i,j in a.items():
    q = 0
    for k,l in b.items():
        if i == k:
            n = j+l
            a[i] = n

b.update(a)
x = []
y = []
for i,j in b.items():
    x.append(i)
    y.append(j)
print(x,y)
for i in range(len(x)):
    k = x[i]
    print(k)
    if k == int:
        pass
    else:
        x[i] = ord(k)
print(x,y)

