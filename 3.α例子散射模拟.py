# -*- coding = utf-8 -*-
# @Time : 2022-02-28오후 6:04
# @Author : 金泰式
# @Site : 
# @File : 3.α例子散射模拟.py
# @Software: PyCharm

import math
import numpy as np
import matplotlib.pyplot as plt

ze,x_0,y_0,v_x,v_y,r,m = 10,50,0,10,0,1,1

x = np.arange(0,1,0.1)
y = np.arange(0,1,0.1)

delta_t = np.arange(0,1,0.001)
r = math.sqrt(x**2+y**2)
a_x = 2*math.pow(ze,2)*(x-x_0)/m*math.pow(r,3)
a_y = 2*math.pow(ze,2)*(y-y_0)/m*math.pow(r,3)

v_x1 = v_x + a_x*delta_t
v_y1 = v_y + a_y*delta_t

x1 = x+v_x1*delta_t
y1 = y+v_y1*delta_t

x = x1
y = y1
plt.title("α")
plt.plot(x,y)
plt.show()

