# -*- coding = utf-8 -*-
# @Time : 2022-04-11오후 7:28
# @Author : 金泰式,3180300014
# @Site : 
# @File : 23. 模拟退火方法.py
# @Software: PyCharm
import random

import numpy as np
import matplotlib.pyplot as plt

random.seed(50)
x = np.arange(0,50,0.001)
y = np.cos(x)+np.cos(np.sqrt(2)*x)+np.cos(np.sqrt(3)*x)
def f(x):
    return np.cos(x)+np.cos(np.sqrt(2)*x)+np.cos(np.sqrt(3)*x)

xi = 1.0
E1 = f(10)
for i in range(20):
    E2 = 0
    a = random.choice(x)
    E2 = f(a)
    k = 0.98
    if E2<E1:
        p = np.exp((E1-E2)/(k*(20-i)))
    else:
        p = 1
    if p > random.random():
        E11 = E1+1
        while E11 > E1:
            xi = random.choice(x)
            E11 = f(xi)
            if E11 == E1:
                break
    print(E1)
    E1 = E11

print(E1,E2)
x1 = [0,50]
y1 = [E1,E1]
plt.plot(x1,y1, c='g')
plt.plot(x,y)
plt.show()