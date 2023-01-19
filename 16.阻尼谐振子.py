# -*- coding = utf-8 -*-
# @Time : 2022-03-25오후 7:58
# @Author : 金泰式,3180300014
# @Site : 
# @File : 16.阻尼谐振子.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,100,0.001)
w = 1.0
k = 0.1

def f(psi,phi,t):
    z = -w**2*phi - k*psi
    return z

phi0 = 0
psi0 = 1
phi_n = []
psi_n = []
phi,psi = phi0,psi0
dt = 0.001
for tt in range(len(t)):
    phi_n.append(phi)
    psi_n.append(psi)

    kpsi1 = f(psi,phi,tt)*dt
    kphi1 = psi*dt

    kpsi2 = f(psi+kpsi1/2,phi+kphi1/2,tt+dt/2)*dt
    kphi2 = (psi+kpsi1/2)*dt

    kpsi3 = f(psi+kpsi2/2,phi+kphi2/2,tt+dt/2)*dt
    kphi3 = (psi+kpsi2/2)*dt

    kpsi4 = f(psi+kpsi3,phi+kphi3,tt+dt)*dt
    kphi4 = (psi+kpsi3)*dt

    psi = psi + (kpsi1+2*kpsi2+2*kpsi3+kpsi4)/6
    phi = phi + (kphi1+2*kphi2+2*kphi3+kphi4)/6

plt.plot(t,phi_n)
plt.show()

