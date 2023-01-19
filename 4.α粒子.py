# -*- coding = utf-8 -*-
# @Time : 2022-03-03오후 2:40
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4.α粒子.py
# @Software: PyCharm

import math
import numpy as np
import matplotlib.pyplot as plt
ze,x_0,y_0,v_x,v_y,m = 1,50,0,100,1,0.00005

d = 0.00000001
x = np.arange(-50,35,0.001)
y = 10

for t in range(0,10000,1):
    k = (x - x_0)**2 + (y - y_0)**2
    r = k**(1/2)

    a_x = (2*(ze**2)*(x-x_0))/(m*(r**3))
    a_y = (2*(ze**2)*(y-y_0))/(m*(r**3))

    v_x1 = v_x + a_x*d*t
    v_y1 = v_y + a_y*d*t

    x1 = x + v_x1*d*t
    y1 = y + v_y1*d*t

    x=x1
    y=y1
    v_x = v_x1
    v_y = v_y1
    print(x1,y1)

plt.xlim(0,80)
plt.ylim(-20,50)
plt.title("α")
plt.plot(x,y)
plt.show()