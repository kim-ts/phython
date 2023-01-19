# -*- coding = utf-8 -*-
# @Time : 2022-03-21오후 1:13
# @Author : 金泰式,3180300014
# @Site : 
# @File : 13.高斯消元法.py
# @Software: PyCharm

import math

a = [1.3,6.3,-3.5,2.8,1.8]
b = [5.6,0.9,8.1,-1.3,16.6]
c = [7.2,2.3,-4.4,0.5,15.1]
d = [1.5,0.4,3.7,5.9,36.9]

a_1 = [a[i]*(5.6/1.3) for i in range(len(a))]
b_1 = [b[i]-a_1[i] for i in range(len(a))]         #b = 0 ...
a_2 = [a[i]*(7.2/1.3) for i in range(len(a))]
c_1 = [c[i]-a_2[i]  for i in range(len(a))]    #c = 0 ...
a_3 = [a[i]*(1.5/1.3) for i in range(len(a))]
d_1 = [d[i]-a_3[i] for i in range(len(a))]         #d = 0 ...
b_21 = [b_1[i]*(c_1[1]/b_1[1]) for i in range(len(a))]
c_2 = [c_1[i]-b_21[i] for i in range(len(a))]      #c = 0 0 ..
print(c_2)
b_22 = [b_1[i]*(d_1[1]/b_1[1]) for i in range(len(a))]
print(b_22)
d_2 = [d_1[i]-b_22[i] for i in range(len(a))]        #d = 0 0 ..
print(d_2)
c_31 = [c_2[i]*(d_2[2]/c_2[2]) for i in range(len(a))]
print(c_31)
d_3 = [d_2[i]-c_31[i] for i in range(len(a))]      #d = 000.
print(d_3)

x4 = d_3[4]/d_3[3]
x3 = (c_2[4]-c_2[3]*x4)/c_2[2]
x2 = (b_1[4]-b_1[3]*x4-b_1[2]*x3)/b_1[1]
x1 = (a[4]-a[3]*x4-a[2]*x3-a[1]*x2)/a[0]

print("x1=%s,x2=%s,x3=%s,x4=%s"%(x1,x2,x3,x4))