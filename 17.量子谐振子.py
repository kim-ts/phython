# -*- coding = utf-8 -*-
# @Time : 2022-03-28오후 7:19
# @Author : 金泰式,3180300014
# @Site : 
# @File : 17.量子谐振子.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-7,7,0.0001)
n = input("n=?")
def f(x,u,v):
    a = ((x**2)-(2*n)-1)*u
    return a
n = int(n)
if n == 0:
    u0 = 1
    v0 = 0
if n%2 == 0:
    u0 = 1
    v0 = 0
else:
    u0 = 0
    v0 = 1


u_n = []
v_n = []
dx = 0.0001
u,v = u0,v0

for i in range(len(x)):
    u_n.append(u)
    v_n.append(v)

    kv1 = f(x[i],u,v)
    ku1 = v

    kv2 = f(x[i]+dx/2,u+(dx*ku1/2),v+(dx*kv1/2))
    ku2 = (v+(dx*kv1/2))

    kv3 = f(x[i]+dx/2,u+(dx*ku2/2),v+(dx*kv2/2))
    ku3 = (v+(dx*kv2/2))

    kv4 = f(x[i]+dx,u+(dx*ku3),v+(dx*kv3))
    ku4 = (v+(dx*kv3))

    u = u + dx*(ku1+2*ku2+2*ku3+ku4)/6
    v = v + dx*(kv1+2*kv2+2*kv3+kv4)/6
rho = []
for i in range(len(x)):
    rho1 = 1/np.sqrt(((2*n) + 1 - (x[i]**2)))
    rho.append(2*rho1*10**9)
up = []
print(rho)
for i in range(len(u_n)):
    upow = u_n[i]**2
    up.append(upow)

plt.plot(x,u_n)
plt.show()
plt.plot(x,up)
plt.plot(x,rho)
plt.show()