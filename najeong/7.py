# -*- coding = utf-8 -*-
# @Time : 2022-06-15오전 2:58
# @Author : 金泰式,3180300014
# @Site : 
# @File : 7.py
# @Software: PyCharm

a = int(input())
z = 2
x = 1
c = 3
v = 2
n = [2,3/2]
for i in range(a-2):
    k = z + c
    p = x + v
    z = c
    c = k
    x = v
    v = p
    l = k/p
    n.append(l)
m = 0
for i in range(len(n)):
    m += n[i]

print(m)