# -*- coding = utf-8 -*-
# @Time : 2022-04-06오후 7:39
# @Author : 金泰式,3180300014
# @Site : 
# @File : 22.二维Ising模型模拟.py
# @Software: PyCharm

import numpy as np
import random
import matplotlib.pyplot as plt
random.seed(100)
xline = np.arange(0,100,1)
kb = 1.0
T = 1.0
b = 1.0
j = 1.0
x = [-1,1]
k = []
for i in range(20):
    l = []
    for j in range(20):
        a = random.choice(x)
        l.append(a)
    k.append(l)

print(k)
s = []
E = []

for l in range(len(xline)):
    ss=[]
    for i in range(20):
        n = k[i]
        sum = 0
        for j in range(20):
            sum = sum + n[j]
        ss.append(sum)
    s1 = 0
    for i in range(len(ss)):
        s1 = s1 + ss[i]
    s.append(s1)
    e = 0
    for i in range(len(k)):
        if i == 19:
            for j in range(len(k)):
                if j == 19:
                    e += -j * (k[i])[j]
                else:
                    e += -j * (k[i])[j]*(k[i])[j+1]
        else:
            for j in range(len(k)):
                if j == 19:
                    e += -j*(k[i])[j]*((k[i+1])[j])
                else:
                    e += -j*(k[i])[j]*((k[i+1])[j]+(k[i])[j+1])
    E.append(e)
    for i in range(len(k)):
        a = k[i]
        if i == 0:
            for j in range(len(a)):
                if j == 0 :
                    E1 = a[j]*a[j+1] + a[j]*(k[i+1])[j]
                    E2 = -a[j]*a[j+1] - a[j]*(k[i+1])[j]
                    dE = E2-E1
                elif j == 19:
                    E1 = a[j]*a[j-1] + a[j]*(k[i+1])[j]
                    E2 = -a[j]*a[j-1] - a[j]*(k[i+1])[j]
                    dE = E2 - E1
                else:
                    E1 = a[j]*a[j-1] + a[j]*a[j+1] + a[j]*(k[i+1])[j] # 原来方向的能量是E1
                    E2 = -a[j]*a[j-1] -a[j]*a[j+1] - a[j]*(k[i+1])[j] # 反方向的能量是E2
                    dE = E2 - E1               # 原来能量低的话 E2 = -E1 所以 E1是-值时候能量低，那么dE是 - 值，如果原来能量高dE是+
                n = np.exp(b*dE)               # 原来能量低的话不用做方向修改，原来能量低是dE是-值，n是一定<1
                if n > random.random():        #random 0~1之间
                    (k[i])[j] = -(k[i])[j]     #random<n是 n是大于1的意思，那么dE是一定要+值，这是原来能量大的情况。
                else:
                    pass
        elif i == 19:
            for j in range(len(a)):
                if j == 0 :
                    E1 = a[j]*a[j+1]+a[j]*(k[i-1])[j]
                    E2 = -a[j]*a[j+1]-a[j]*(k[i-1])[j]
                    dE = E2-E1
                elif j == 19:
                    E1 = a[j]*a[j-1] + a[j]*(k[i-1])[j]
                    E2 = -a[j]*a[j-1] - a[j]*(k[i-1])[j]
                    dE = E2 - E1
                else:
                    E1 = a[j]*a[j-1] + a[j]*a[j+1] + a[j]*(k[i-1])[j]
                    E2 = -a[j]*a[j-1] -a[j]*a[j+1] - a[j]*(k[i-1])[j]
                    dE = E2 - E1
                n = np.exp(b*dE)
                if n > random.random():
                    (k[i])[j] = -(k[i])[j]
                else:
                    pass
        else:
            for j in range(len(a)):
                if j == 0 :
                    E1 = a[j]*a[j+1] + a[j]*(k[i-1])[j] + a[j]*(k[i+1])[j]
                    E2 = -a[j]*a[j+1] - a[j]*(k[i-1])[j] - a[j]*(k[i+1])[j]
                    dE = E2-E1
                elif j == 19:
                    E1 = a[j]*a[j-1] + a[j]*(k[i-1])[j]+a[j]*(k[i+1])[j]
                    E2 = -a[j]*a[j-1] - a[j]*(k[i-1])[j]-a[j]*(k[i+1])[j]
                    dE = E2 - E1
                else:
                    E1 = a[j]*a[j-1] + a[j]*a[j + 1] + a[j]*(k[i-1])[j] + a[j]*(k[i+1])[j]
                    E2 = -a[j]*a[j-1] -a[j]*a[j + 1] - a[j]*(k[i-1])[j] - a[j]*(k[i+1])[j]
                    dE = E2 - E1
                n = np.exp(b*dE)
                if n > random.random():
                    (k[i])[j] = -(k[i])[j]
                else:
                    pass


print("energy=%s,last=%s"%(E,E[len(xline)-1]))
print("spin=%s,last=%s"%(s,s[len(xline)-1]))
print(k)


plt.plot(xline,s)
plt.xlabel('times')
plt.ylabel('spin')
plt.show()