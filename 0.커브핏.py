# -*- coding = utf-8 -*-
# @Time : 2022-03-23오후 3:09
# @Author : 金泰式,3180300014
# @Site : 
# @File : 0.커브핏.py
# @Software: PyCharm

import  math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = np.arange(-10,10,0.1)
y = 2*(x**3)-50
noise = 50*np.random.normal(size=x.size)
y = y +noise


def func(x,a,b):
    return a*(x**3)+b

popt, pcov = curve_fit(func, x, y)
print(popt)
print(pcov)

plt.plot(x,y,label="original")
plt.plot(x,func(x,*popt),label="fitting")
plt.legend()
plt.show()