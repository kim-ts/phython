# -*- coding = utf-8 -*-
# @Time : 2022-03-16오후 1:50
# @Author : 金泰式,3180300014
# @Site : 
# @File : 10.高斯信号寻找.py
# @Software: PyCharm

from scipy.optimize import curve_fit
import numpy as np
import math
import matplotlib.pyplot as plt

a = open("C:/Users/hy371/Desktop/물리/계산물리/作业5/new_particle_data.txt",'r')
b = a.readlines()

c = np.loadtxt("C:/Users/hy371/Desktop/물리/계산물리/作业5/new_particle_data.txt",delimiter=",")


c1 = []
c2 = []
for i in c:
    c11 = i[0]
    c1.append(c11)
for i in c:
    c12 = i[1]
    c2.append(c12)

x = np.linspace(0,30,10000)
t = np.e

def func(x,A,B):
    bkg = A*math.pow(t,-x/B)
    return bkg

def func2(x,A,B,C,D,E):
    y = A*np.exp(-x/B)+C*np.exp(-(x-E)**2/(2*D**2))/(D*np.sqrt(2*np.pi))
    return y

ff = []
for i in range(len(c2)):
    f2 = c2[i] - func(c1[i],1000,10)
    ff.append(f2)


popt, pcov = curve_fit(func2, c1,c2,p0=[1000,10,400,5,10])
print(popt)

plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(c1,c2)
plt.plot(x, func2(x, *popt),'r-')
plt.subplot(3,1,3)
plt.plot(c1,ff)
plt.show()