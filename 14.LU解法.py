# -*- coding = utf-8 -*-
# @Time : 2022-03-22오후 8:37
# @Author : 金泰式,3180300014
# @Site : 
# @File : 14.LU解法.py
# @Software: PyCharm

import numpy as np
a = [[1.3,6.3,-3.5,2.8],
     [5.6,0.9,8.1,-1.3],
     [7.2,2.3,-4.4,0.5],
     [1.5,0.4,3.7,5.9]]
b= [[1.8],
    [16.6],
    [15.1],
    [36.9]]
l = [[1.3,0,0,0],
     [5.6],
     [7.2],
     [1.5]]
u = [[1],
     [0,1],
     [0,0,1],
     [0,0,0,1]]


for i in range(1,len(a)):
    a1,l1 = a[0],l[0]
    u_1i = a1[i]/l1[0]
    u[0].append(u_1i)
for i in range(1,len(a)):
    a_i = a[i]
    l_i = l[i]
    u_1 = u[0]
    l_i2 = a_i[1]-l_i[0]*u_1[1]
    l[i].append(l_i2)
for i in range(2,4):
    a2 = a[1]
    l2 = l[1]
    u1 = u[0]
    u_2i = (a2[i]-l2[0]*u1[i])/l2[1]
    u[1].append(u_2i)
l33=(a[2])[2]-(l[2])[0]*(u[0])[2]-(l[2])[1]*(u[1])[2]
l[2].append(l33)
u34 = ((a[2])[3]-(u[0])[3]*(l[2])[0]-(l[2])[1]*(u[1])[3])/(l[2])[2]
u[2].append(u34)
l43 = ((a[3])[2]-(u[0])[2]*(l[3])[0]-(l[3])[1]*(u[1])[2])
l[3].append(l43)
l44 = ((a[3])[3]-(l[3])[0]*(u[0])[3]-(l[3])[1]*(u[1])[3]-(l[3])[2]*(u[2])[3])
l[3].append(l44)
l[1].append(0)
l[1].append(0)
l[2].append(0)
y = []
#ldet = np.linalg.det(l)
linv = np.linalg.inv(l)
for i in range(4):
    l1 = linv[i]
    yy = []
    s = 0
    for j in range(4):
        B = b[j]
        yi = B[0]*l1[j]
        yy.append(yi)
    for k in range(4):
        s = s+ yy[k]
    y.append(s)

uinv = np.linalg.inv(u)
x = []
for i in range(4):
    ui = uinv[i]
    xx = []
    sum = 0
    for j in range(4):
        s = ui[j]*y[j]
        xx.append(s)
    for k in range(4):
        sum = sum + xx[k]
    x.append(sum)

print(x)