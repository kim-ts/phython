# -*- coding = utf-8 -*-
# @Time : 2022-03-04오후 8:55
# @Author : 金泰式,3180300014
# @Site : 
# @File : 5.贝塞尔函数.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0.1,20.0,0.000001)
j_0 = np.sin(x)/x
j_1 = (np.sin(x)/x**2)-(np.cos(x)/x)
j=[]
j.append(j_0)
j.append(j_1)

k = []
for i in range(2,11,1):
    #print("j[%s]=%s"%(i,j[i-1] - j[i-2]))
    k = (((2*i+1)/x)*j[i-1])-j[i-2]
    j.append(k)

for i in range(0,11,1):
   print("j[%s]=%s"%(i,j[i]))

plt.subplot(3,1,1)
plt.plot(x,j[1])
plt.title("j_2")
plt.subplot(3,1,2)
plt.plot(x,j[4])
plt.title("j_5")
plt.subplot(3,1,3)
plt.plot(x,j[9])
plt.title("j_10")
plt.show()