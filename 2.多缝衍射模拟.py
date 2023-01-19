# -*- coding = utf-8 -*-
# @Time : 2022-02-28 오후 3:31
# @Author : 金泰式，3180300014
# @File : 2.多缝衍射模拟.py
# @Software: PyCharm

import math
import numpy as np
import matplotlib.pyplot as plt

lamda,n,p,a,d,i_0 = 0.5,10,math.pi,0.4,0.8,1   #设定常数值

x = np.arange(-p/2, p/2, 0.000001)            #设定x范围，指波经过缝之后挠的角度
u = np.sin(x)*p*a/lamda
v = np.sin(x)*p*d/lamda
i = i_0*(pow(np.sin(u),2)/pow(u,2))*(pow(np.sin(n*v),2)/pow(np.sin(v),2))   #函数
y = i
plt.title("i-theta")
plt.plot(x, y)
plt.show()
