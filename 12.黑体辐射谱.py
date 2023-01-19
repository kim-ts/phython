# -*- coding = utf-8 -*-
# @Time : 2022-03-22오전 2:42
# @Author : 金泰式,3180300014
# @Site : 
# @File : 12.黑体辐射谱.py
# @Software: PyCharm


import numpy as np
import matplotlib.pyplot as plt

c1 = 1.0
c2 = 1.44*(10**4)
l = np.arange(0.1,5,0.01)
B = []
l_max = []
for t in range(2000,6050,50):
    b = (c1/(l**5))*(1/(np.exp(c2/(l*t))-1))
    B.append(b)



for i in range(len(B)):
    a = B[i]
    for i in range(len(B[i])-1):
        aa = (a[i+1]-a[i])/0.01
        if aa < 0 :
            l_max.append(a[i])
            break
        else:
            pass
print(len(l_max))
print(l_max)
print(l_max[80])
for i in range(len(l_max)):
    tt=[]
    for t in range(2000,6050,50):
        ttt=t
        tt.append(t)
    print("t=%s,l_max=%s"%(tt[i],l_max[i]))

plt.plot(l,b)
plt.show()