# -*- coding = utf-8 -*-
# @Time : 2022-03-05오후 7:11
# @Author : 金泰式,3180300014
# @Site : 
# @File : 贝塞尔函数下去.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0.1,20.0,0.0001)

j_50 = 1
j_49 = 1
j=[]                             #j_50是list里面在于j【0】地方，j_49是在于j【1】上
j.append(j_50)
j.append(j_49)

k = []
for i in range(2,51,1):
    #print("j[%s]=%s"%(i,j[i-1] - j[i-2]))
    k = (((2*(51-i)+1)/x)*j[i-1])-j[i-2] #先算后每个list k apeend到jlist里, 这里i是 2的时候算的是l=49，i=3时l=48 .。。。。所以51-i=l
    print("k=%s,i=%s,51-i=%s"%(k,i,51-i))
    j.append(k)                            #所以j_48是在于 j【2】里面 。。。。。 一直下去

for i in range(0,51,1):
   print("j[%s]=%s"%(i,j[i]))
j.reverse()                          #reverse的话 就j_0 = j[0],j_1=j[1], ...., j_49=j[49],j_50=j[50]
##for i in range(0,51,1):
   #print("j[%s]=%s"%(i,j[i]))

j[0] = j[0]*((np.sin(x))/x)
j[1] = j[1]*((np.sin(x)/(x**2))-(np.cos(x)/x))      #再计算j【0】和j【1】， 就是为了避免误差，乘原来j【0】，j【1】值
l=[]
m=[]                         #新定义m list  为了再j【0】到上去计算得到j【10】 的所有元素放在m list里
m.append(j[0])
m.append(j[1])
print(m)
for i in range(2,11,1):
    print("j[%s]=%s"%(i,m[i-1] - m[i-2]))
    l = (((2*i+1)/x)*j[i-1])-j[i-2]
    m.append(l)
print(j[0])
#跟前面同理

plt.subplot(3,1,1)
plt.plot(x,m[1])
plt.title("j_2")
plt.subplot(3,1,2)
plt.plot(x,m[4])
plt.title("j_5")
plt.subplot(3,1,3)
plt.plot(x,m[9])
plt.title("j_10")
plt.show()