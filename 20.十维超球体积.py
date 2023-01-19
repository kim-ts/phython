# -*- coding = utf-8 -*-
# @Time : 2022-03-29오후 9:22
# @Author : 金泰式,3180300014
# @Site : 
# @File : 20.十维超球体积.py
# @Software: PyCharm
import random

import numpy as np
import matplotlib.pyplot as plt

v = 0
N = input("n=?")
N = int(N)
for i in range(N):
    rnd1 = random.random()
    rnd2 = random.random()
    rnd3 = random.random()
    rnd4 = random.random()
    rnd5 = random.random()
    rnd6 = random.random()
    rnd7 = random.random()
    rnd8 = random.random()
    rnd9 = random.random()
    rnd10 = random.random()
    r = rnd1**2+rnd2**2+rnd3**2+rnd4**2+rnd5**2+rnd6**2+rnd7**2+rnd8**2+rnd9**2+rnd10**2
    if r <= 1:
        v = v + 1
'''
rnd1 = []
rnd2 = []
rnd3 = []
rnd4 = []
rnd5 = []
rnd6 = []
rnd7 = []
rnd8 = []
rnd9 = []
rnd10 = []


#LCG parameters

a = 1103515245
c = 12345
m = 2**31

# seed and iteration
rand = 100
N = 1000000

for i in range(0,N):
    rand = (a*rand +c)%m
    if i%10 == 0:
        rnd1.append(rand/m)
    elif i%10 == 1:
        rnd2.append(rand/m)
    elif i%10 == 2:
        rnd3.append(rand/m)
    elif i%10 == 3:
        rnd4.append(rand/m)
    elif i%10 == 4:
        rnd5.append(rand/m)
    elif i%10 == 5:
        rnd6.append(rand/m)
    elif i%10 == 6:
        rnd7.append(rand/m)
    elif i%10 == 7:
        rnd8.append(rand/m)
    elif i%10 == 8:
        rnd9.append(rand/m)
    else:
        rnd10.append(rand/m)

#print(len(rnd1),len(rnd2),len(rnd3),len(rnd4),len(rnd5),len(rnd6),len(rnd7),len(rnd8),len(rnd9),len(rnd10))
v = []
for i in range(len(rnd1)):
    r = np.sqrt(rnd1[i]**2+rnd2[i]**2+rnd3[i]**2+rnd4[i]**2+rnd5[i]**2+rnd6[i]**2+rnd7[i]**2+rnd8[i]**2+rnd9[i]**2+rnd10[i]**2)
    if r <= 1:
        v.append(r)
'''
print((v/N)*2**10)
