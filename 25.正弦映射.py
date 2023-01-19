# -*- coding = utf-8 -*-
# @Time : 2022-04-15오후 8:19
# @Author : 金泰式,3180300014
# @Site : 
# @File : 25.正弦映射.py
# @Software: PyCharm

import random
import numpy as np
import matplotlib.pyplot as plt


def f(r,x):
    return r*np.sin(np.pi*x)

n = 1000
xmin = 0.0
xmax = 1.0
r = np.linspace(0,1,n)

iterations = 1000
last = 100
x = 10**-5*np.ones(n)

for i in range(iterations):
    x = f(r,x)
    if i >= (iterations - last):
        plt.plot(r,x,',k',alpha=0.1)
'''
r = random.random()
n = 50
print(r)
yp = []
x = 0.1
xp = []
for i in range(n):
    x_n = r*np.sin(np.pi*x)
    x = x_n
    yp.append(x)
    xp.append(i)
'''


plt.xlim(xmin,xmax)
plt.grid()
plt.show()