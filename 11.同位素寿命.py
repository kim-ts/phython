# -*- coding = utf-8 -*-
# @Time : 2022-03-22오전 1:09
# @Author : 金泰式,3180300014
# @Site : 
# @File : 11.同位素寿命.py
# @Software: PyCharm
from scipy.optimize import curve_fit
import numpy as np
import math
import matplotlib.pyplot as plt

a = open("C:/Users/hy371/Desktop/물리/계산물리/作业5/error_fit_data.txt",'r')
b = a.readlines()

c = np.loadtxt("C:/Users/hy371/Desktop/물리/계산물리/作业5/error_fit_data.txt",delimiter=",")


t = []
n = []
sig = []
for i in c:
    c11 = i[0]
    t.append(c11)
for i in c:
    c12 = i[1]
    n.append(c12)
for i in c:
    c12 = i[2]
    sig.append(c12)

x = np.linspace(0,500.0,100000)
def func(x,N,u):
    a = N*np.exp(-x/u)
    return a

popt , pcov = curve_fit ( func , t , n, sigma = sig ,absolute_sigma=True,p0=[1,10])

y = n
sum = 0
for i in range(len(sig)):
    sum = sum +sig[i]

chi = np.diag(pcov,k=0)**2/sum
sumc = 0
for i in range(len(pcov)):
    sumc = sumc + chi[i]

Ndf = int(len(t))-2
ss = sumc/Ndf
print(sumc)
print(Ndf)
print(ss)

plt.figure(figsize=(10,6))
plt.errorbar(t,y,yerr=sig)
plt.plot()
plt.plot(x, func(x, *popt),'r-')
plt.show()