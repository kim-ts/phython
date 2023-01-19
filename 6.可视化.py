# -*- coding = utf-8 -*-
# @Time : 2022-03-09오후 4:49
# @Author : 金泰式,3180300014
# @Site : 
# @File : 6.可视化.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np

a = open("C:/Users/hy371/Desktop/물리/계산물리/作业3/SN_d_tot_V2.0.txt",'r')
b = a.readlines()
'''for line in b:
    print(line)
'''
data = np.loadtxt("C:/Users/hy371/Desktop/물리/계산물리/作业3/SN_d_tot_V2.0.txt",float)


c4 = []
c5 = []
c6 = []
c7 = []                  #设list
for i in data:
    column4 = i[3]
    c4.append(column4)               #data里面的第4列数据
for i in data:
    column5 = i[4]
    c5.append(column5)               #data里面的第5列数据
for i in data:
    column6 = i[5]
    c6.append(column6)              #6列
for i in data:
    column7 = i[6]
    c7.append(column7)              #7列

for i in range(len(c5)):
    if c5[i] == -1.0:
        c5[i] = 0.0                 #c5里元素中-1的数据都换成0
    else:
        pass
print(c5)
x = c4
y = c5

'''column4 = np.array(a).T[3]
column5 = np.array(a).T[4]
column6 = np.array(a).T[5]
print(column4)
y = column5*column6
x = column4'''

plt.plot(x,y)
plt.show()