# -*- coding = utf-8 -*-
# @Time : 2022-03-22오전 5:37
# @Author : 金泰式,3180300014
# @Site : 
# @File : 12-1.黑体辐射谱.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt

c1 = 1.0
c2 = 1.44*(10**4)
l = np.arange(0.1,5,0.01)
t = 5000
def func(l):
    b = (c1/(l**5))*(1/(np.exp(c2/(l*t))-1))
    return b

a = input("n=")
b = float(a)

h =  (0.8-0.3)/b
fa = func(0.3)
fb = func(0.8)
f = []
for i in range(int(b)):
    n = 0.3+(i*h)
    ff = func(n)
    f.append(ff)
sum = 0
for i in range(int(b)):
    sum = sum+f[i]

print(sum)

integ = h*(fa + sum + fb)
print("积分结果=%s"%integ)