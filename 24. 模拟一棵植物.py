# -*- coding = utf-8 -*-
# @Time : 2022-04-11오후 10:27
# @Author : 金泰式,3180300014
# @Site : 
# @File : 24. 模拟一棵植物.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np
import random

A1 = np.array([[0.00,0.00],
              [0.00,0.16]])
B1 = np.array([[0.00],[0.00]])

A2 = np.array([[0.85,0.04],
              [-0.04,0.85]])
B2 = np.array([[0.00,1.60]])

A3 = np.array([[0.20,-0.26],
               [0.23,0.22]])
B3 = np.array([[0.00,0.16]])

A4 = np.array([[-0.15,0.28],
               [0.26,0.24]])
B4 = np.array([[0,0.44]])
xy = np.array([0,0])
f = []
for i in range(100000):
    print(i)
    a = random.randint(0,100)
    if 0 < a <= 1:
        f1 = A1.dot(xy)+B1
        f.append(f1)
        xy = np.array(f1[0])
    elif 1< a <= 86:
        f2 = A2.dot(xy)+B2
        f.append(f2)
        xy = np.array(f2[0])
    elif 86< a <= 93:
        f3 = A3.dot(xy)+B3
        f.append(f3)
        xy = np.array(f3[0])
    else:
        f4 = A4.dot(xy)+B4
        f.append(f4)
        xy = np.array(f4[0])


xpoint = []
ypoint = []
for i in range(len(f)):
    fx = ((f[i])[0])[0]
    fy = ((f[i])[0])[1]
    xpoint.append(fx)
    ypoint.append(fy)

plt.scatter(xpoint,ypoint,c='g',s=1)
plt.show()