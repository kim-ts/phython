# -*- coding = utf-8 -*-
# @Time : 2022-03-28오후 1:09
# @Author : 金泰式,3180300014
# @Site : 
# @File : 0.LCG.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt

rnd1 =[]
rnd2 = []

#LCG parameters

a = 69069
c = 1
m = 41900000

# seed and iteration
rand = 100
N = 10000

for i in range(0,N):
    rand = (a*rand +c)%m
    if i%2 == 0:
        rnd1.append(rand/m)
    else:
        rnd2.append(rand/m)

plt.scatter(rnd1,rnd2,s=0.05)
plt.show()