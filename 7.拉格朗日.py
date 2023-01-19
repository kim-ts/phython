# -*- coding = utf-8 -*-
# @Time : 2022-03-10오후 1:54
# @Author : 金泰式,3180300014
# @Site : 
# @File : 7.拉格朗日.py
# @Software: PyCharm

import math
import numpy as np
import matplotlib.pyplot as plt
u = 50
sigma = 15
x_0 = 5.0
x_n = 95.0

x = []
x.append(x_0)               #x_0
n = input("n=?")

for i in range(1,int(n)+1,1):            # 这时n=1~7 但是7次是不算
    x_i = x_0 + i*(x_n-x_0)/float(n)
    x.append(x_i)                          #计算是x_1到x_6

a = math.sqrt(2*np.pi)

b = []
for i in range(0,int(n)+1):
    b0 = math.pow(x[i]-u,2)
    b.append(b0)

c = 2*math.pow(sigma,2)

d = []
for i in range(int(n)+1):
    d0 = math.pow(np.e,-b[i]/c)
    d.append(d0)

f = []
for i in range(int(n)+1):
    f0 = a*d[i]
    f.append(f0)

xp = np.arange(0,100,0.001)
p = []

l_n_up = []
l_n_d = []
for i in range(int(n)+1):
    lnu = (xp-x[i])
    l_n_up.append(lnu)
po = 0
for k in range(int(n)+1):
    for i in range(int(n)+1):
        lnd = (x[k]-x[i])
        l_n_d.append(lnd)
        print(k, i,po,lnd)
        po = po+1
if int(n) == 1:
    l0 = (xp - x[1])/(x[0]-x[1])
    l1 = (xp - x[0])/(x[1]-x[0])
    p = np.multiply(l0,f[0]) + np.multiply(l1,f[1])
else:
    if int(n) == 2:
        l0 = (xp-x[1])*(xp-x[2])/(x[0]-x[1])*(x[0]-x[2])
        l1 = (xp-x[0])*(xp-x[2])/(x[1]-x[0])*(x[1]-x[2])
        l2 = (xp-x[0])*(xp-x[1])/(x[2]-x[0])*(x[2]-x[1])
        p = np.multiply(l0,f[0]) + np.multiply(l1,f[1]) + np.multiply(l2,f[2])
    else:
        if int(n) == 6:
            l0u = l_n_up[1]*l_n_up[2]*l_n_up[3]*l_n_up[4]*l_n_up[5]*l_n_up[6]
            l0d = l_n_d[1]*l_n_d[2]*l_n_d[3]*l_n_d[4]*l_n_d[5]*l_n_d[6]
            l0 = l0u/l0d
            l1u = l_n_up[0]*l_n_up[2]*l_n_up[3]*l_n_up[4]*l_n_up[5]*l_n_up[6]
            l2u = l_n_up[0] * l_n_up[1] * l_n_up[3] * l_n_up[4] * l_n_up[5] * l_n_up[6]
            l3u = l_n_up[0] * l_n_up[1] * l_n_up[2] * l_n_up[4] * l_n_up[5] * l_n_up[6]
            l4u = l_n_up[0] * l_n_up[1] * l_n_up[2] * l_n_up[3] * l_n_up[5] * l_n_up[6]
            l5u = l_n_up[0] * l_n_up[1] * l_n_up[2] * l_n_up[3] * l_n_up[4] * l_n_up[6]
            l6u = l_n_up[0] * l_n_up[1] * l_n_up[2] * l_n_up[3] * l_n_up[4] * l_n_up[5]
            l1d = l_n_d[7] * l_n_d[9] * l_n_d[10] * l_n_d[11] * l_n_d[12] * l_n_d[13]
            l2d = l_n_d[14] * l_n_d[15] * l_n_d[17] * l_n_d[18] * l_n_d[19] * l_n_d[20]
            l3d = l_n_d[21] * l_n_d[22] * l_n_d[23] * l_n_d[25] * l_n_d[26] * l_n_d[27]
            l4d = l_n_d[28] * l_n_d[29] * l_n_d[30] * l_n_d[31] * l_n_d[33] * l_n_d[34]
            l5d = l_n_d[35] * l_n_d[36] * l_n_d[37] * l_n_d[38] * l_n_d[39] * l_n_d[41]
            l6d = l_n_d[42] * l_n_d[43] * l_n_d[44] * l_n_d[45] * l_n_d[46] * l_n_d[47]
            l1 = l1u/l1d
            l2 = l2u/l2d
            l3 = l3u/l3d
            l4 = l4u/l4d
            l5 = l5u/l5d
            l6 = l6u/l6d
            p = np.multiply(l0, f[0]) + np.multiply(l1, f[1]) + np.multiply(l2, f[2]) + np.multiply(l3, f[3]) + np.multiply(l4, f[4]) + np.multiply(l5, f[5]) + np.multiply(l6, f[6])


print(p)
plt.subplot(2,1,1)
plt.title("f(x),n=%s"%(n))
plt.plot(x,f)
plt.subplot(2,1,2)
plt.title("p(x),n=%s"%n)
plt.plot(xp,p)
plt.show()