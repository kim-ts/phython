# -*- coding = utf-8 -*-
# @Time : 2022-03-29오후 5:15
# @Author : 金泰式,3180300014
# @Site : 
# @File : 19.随机行走模拟.py
# @Software: PyCharm

import random
import numpy as np
import matplotlib.pyplot as plt
t = input("t")
t = int(t)
k = []
N = 10**6
for j in range(N):
    x = 0
    for i in range(t):
        a = random.randint(1,6)
        if a == 1:
            x = x-1
        elif 1<a<4:
            x = x
        else:
            x = x+1
    k.append(x)


sumx = []
for i in range(-t,t,1):
    a = k.count(i)
    sumx.append(a)

print(100*1/6,100*2/6,100*3/6)


x = np.arange(-t,t,1)
plt.plot(x,sumx)
plt.show()

'''
여기서 2/6확률로 멈춰있으니 0
1/6확률로 -1이므로 확률이 16.6이니 반올림해서 17이라치고
1/2확률로 +1 이니까 50이면 
확률상 가장높은위치는 대략 50-17 로 33부근이여야함
소름돋게도 그래프 꼭대기부근은 정확히 33부근이다.
'''