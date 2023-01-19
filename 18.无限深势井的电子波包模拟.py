# -*- coding = utf-8 -*-
# @Time : 2022-03-28오후 10:35
# @Author : 金泰式,3180300014
# @Site : 
# @File : 18.无限深势井的电子波包模拟.py
# @Software: PyCharm

import  numpy
import numpy as np
import matplotlib.pyplot as plt
L = 10**-8
sig = 10**-10
k = 5*10**10
h_bar = 1.0546*10**-34
Me = 9.109*10**-31
ht = 10**-18
x0 = L/2
i = complex(0,1)
N = 999
hx = L/N
x = np.arange(0,L,hx)

psi = np.exp(-(((x-x0)**2)/(2*sig**2))+(i*k*x))


a1 = 1 + (i*h_bar*ht/2*Me*hx**2)
a2 = -(i*h_bar*ht/4*Me*hx**2)
b1 = 1 - (i*h_bar*ht/2*Me*hx**2)
b2 = i*h_bar*ht/4*Me*hx**2


a0 = []
b0 = []
for i in range(999):
    a = []
    b = []
    for i in range(999):
        a.append(0)
        b.append(0)
    a0.append(a)
    b0.append(b)


a = a0
b = b0
'''
a = numpy.zeros(shape=(999,999),dtype =complex)
b = numpy.zeros(shape=(999,999),dtype = complex)
'''
for i in range(1,998):
    (a[i])[i] = a1
    (a[i])[i-1] = a2
    (a[i])[i+1] = a2
    (b[i])[i] = b1
    (b[i])[i-1] = b2
    (b[i])[i+1] = b2
(a[0])[0] = a1
(a[0])[1] = a2
(a[998])[998] = a1
(a[998])[997] = a2
(b[0])[0] = b1
(b[0])[1] = b2
(b[998])[998] = b1
(b[998])[997] = b2

A = np.array(a)
B = np.array(b)

k = input("t=?")
k = int(k)
psi_n0 = []
'''
A1 = np.linalg.inv(A)
dot = np.dot(A1,B)
det = np.linalg.det(dot)
'''



if k == 0 :
    psi_n0.append(psi)
else:
    for t in range(k):
        Bpsi = np.dot(B, psi)
        psi_n = np.linalg.solve(a,Bpsi)
        psi = psi_n
        print(psi[500])
    psi_n0.append(psi)
    print((psi_n0[0])[500])



psi_real = []
psi_image = []

for i in range(len(x)):
    psi_real.append((psi_n0[0])[i].real)
    psi_image.append((psi_n0[0])[i].imag)

psi_pro = []
for i in range(len(psi_real)):
    l = np.sqrt(psi_real[i]**2+psi_image[i]**2)
    psi_pro.append(l)




plt.subplot(3,1,1)
plt.plot(x,psi_real)
plt.subplot(3,1,2)
plt.plot(x,psi_image)
plt.subplot(3,1,3)
plt.plot(x,psi_pro)
plt.show()