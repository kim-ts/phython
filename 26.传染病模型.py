# -*- coding = utf-8 -*-
# @Time : 2022-04-18오후 7:49
# @Author : 金泰式,3180300014
# @Site : 
# @File : 26.传染病模型.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt


#k = np.arange(0,0.0007,0.000001)
k = np.arange(0,1.4*10**-7,10**-14)
l = 0.01
x0 = 10**6
z0 = 0
N = x0 + 1
dt = 1
z=0
#z = np.arange(-0.0001,0.0001,0.0000001)
zz = []
#k = 0.01

for i in range(len(k)):
    k0 = k[i]
    zn = l*(N - x0*np.exp(-k0*z/l)-z)*dt
    z += zn
    zz.append(z)


print(zz)

#plt.ylim(0,10**6)
plt.plot(k,zz)
#plt.grid()
plt.show()