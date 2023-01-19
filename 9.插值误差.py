# -*- coding = utf-8 -*-
# @Time : 2022-03-13오후 11:41
# @Author : 金泰式,3180300014
# @Site : 
# @File : 9.插值误差.py
# @Software: PyCharm

import math
import numpy as np
import matplotlib.pyplot as plt
u = 50
sigma = 15
x_0 = 5.0
x_n = 95.0

x1 = []
x2 = []
x6 = []
x1.append(x_0)               #x_0
x2.append(x_0)
x6.append(x_0)
n1 = 1
n2 = 2
n6 = 6

for i in range(1,n1+1,1):            # 这时n1=1~7 但是7次是不算
    x_i1 = x_0 + i*(x_n-x_0)/float(n1)
    x1.append(x_i1)                          #计算是x_1到x_6
for i in range(1,n2+1,1):            # 这时n2=1~7 但是7次是不算
    x_i2 = x_0 + i*(x_n-x_0)/float(n2)
    x2.append(x_i2)                          #计算是x_1到x_6
for i in range(1,n6+1,1):            # 这时n6=1~7 但是7次是不算
    x_i6 = x_0 + i*(x_n-x_0)/float(n6)
    x6.append(x_i6)                          #计算是x_1到x_6

a = math.sqrt(2*np.pi)

b1 = []
b2 = []
b6 = []
for i in range(0,n1+1):
    b01 = math.pow(x1[i]-u,2)
    b1.append(b01)
for i in range(0,n2+1):
    b02 = math.pow(x2[i]-u,2)
    b2.append(b02)
for i in range(0,n6+1):
    b06 = math.pow(x6[i]-u,2)
    b6.append(b06)

c = 2*math.pow(sigma,2)

d1 = []
d2 = []
d6 = []
for i in range(int(n1)+1):
    d01 = math.pow(np.e,-b1[i]/c)
    d1.append(d01)
for i in range(int(n2)+1):
    d02 = math.pow(np.e,-b2[i]/c)
    d2.append(d02)
for i in range(int(n6)+1):
    d06 = math.pow(np.e,-b6[i]/c)
    d6.append(d06)

f1 = []
f2 = []
f6 = []
for i in range(int(n1)+1):
    f01 = a*d1[i]
    f1.append(f01)
for i in range(int(n2)+1):
    f02 = a*d2[i]
    f2.append(f02)
for i in range(int(n6)+1):
    f06 = a*d6[i]
    f6.append(f06)

xp = np.arange(0,100,0.001)
p = []


l_n_up6 = []

l_n_d6 = []

for i in range(int(n6)+1):
    lnu6 = (xp-x6[i])
    l_n_up6.append(lnu6)
po = 0
for k in range(int(n6)+1):
    for i in range(int(n6)+1):
        lnd6 = (x6[k]-x6[i])
        l_n_d6.append(lnd6)
        po = po+1

l01 = (xp - x1[1])/(x1[0]-x1[1])
l11 = (xp - x1[0])/(x1[1]-x1[0])
p1 = np.multiply(l01,f1[0]) + np.multiply(l11,f1[1])

l02 = (xp-x2[1])*(xp-x2[2])/(x2[0]-x2[1])*(x2[0]-x2[2])
l12 = (xp-x2[0])*(xp-x2[2])/(x2[1]-x2[0])*(x2[1]-x2[2])
l22 = (xp-x2[0])*(xp-x2[1])/(x2[2]-x2[0])*(x2[2]-x2[1])
p2 = np.multiply(l02,f2[0]) + np.multiply(l12,f2[1]) + np.multiply(l22,f2[2])

l0u = l_n_up6[1]*l_n_up6[2]*l_n_up6[3]*l_n_up6[4]*l_n_up6[5]*l_n_up6[6]
l0d = l_n_d6[1]*l_n_d6[2]*l_n_d6[3]*l_n_d6[4]*l_n_d6[5]*l_n_d6[6]
l0 = l0u/l0d
l1u = l_n_up6[0]*l_n_up6[2]*l_n_up6[3]*l_n_up6[4]*l_n_up6[5]*l_n_up6[6]
l2u = l_n_up6[0] * l_n_up6[1] * l_n_up6[3] * l_n_up6[4] * l_n_up6[5] * l_n_up6[6]
l3u = l_n_up6[0] * l_n_up6[1] * l_n_up6[2] * l_n_up6[4] * l_n_up6[5] * l_n_up6[6]
l4u = l_n_up6[0] * l_n_up6[1] * l_n_up6[2] * l_n_up6[3] * l_n_up6[5] * l_n_up6[6]
l5u = l_n_up6[0] * l_n_up6[1] * l_n_up6[2] * l_n_up6[3] * l_n_up6[4] * l_n_up6[6]
l6u = l_n_up6[0] * l_n_up6[1] * l_n_up6[2] * l_n_up6[3] * l_n_up6[4] * l_n_up6[5]
l1d = l_n_d6[7] * l_n_d6[9] * l_n_d6[10] * l_n_d6[11] * l_n_d6[12] * l_n_d6[13]
l2d = l_n_d6[14] * l_n_d6[15] * l_n_d6[17] * l_n_d6[18] * l_n_d6[19] * l_n_d6[20]
l3d = l_n_d6[21] * l_n_d6[22] * l_n_d6[23] * l_n_d6[25] * l_n_d6[26] * l_n_d6[27]
l4d = l_n_d6[28] * l_n_d6[29] * l_n_d6[30] * l_n_d6[31] * l_n_d6[33] * l_n_d6[34]
l5d = l_n_d6[35] * l_n_d6[36] * l_n_d6[37] * l_n_d6[38] * l_n_d6[39] * l_n_d6[41]
l6d = l_n_d6[42] * l_n_d6[43] * l_n_d6[44] * l_n_d6[45] * l_n_d6[46] * l_n_d6[47]

l1 = l1u/l1d
l2 = l2u/l2d
l3 = l3u/l3d
l4 = l4u/l4d
l5 = l5u/l5d
l6 = l6u/l6d
print(l0,l1,l2,l3,l4,l5,l6,"f6=%s"%f6)
p6 = np.multiply(l0,f6[0]) + np.multiply(l1,f6[1]) + np.multiply(l2,f6[2]) + np.multiply(l3, f6[3]) + np.multiply(l4, f6[4]) + np.multiply(l5, f6[5]) + np.multiply(l6, f6[6])


print(p6)
plt.title("f(x),n=%s,%s,%s"%(n1,n2,n6))
plt.plot(xp,p1,xp,p2,xp,p6*2500)
plt.legend(['n=1','n=2','n=6'])
plt.show()
