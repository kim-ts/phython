# -*- coding = utf-8 -*-
# @Time : 2022-03-24오전 11:45
# @Author : 金泰式,3180300014
# @Site : 
# @File : 15.迭代法.py
# @Software: PyCharm

A = [[1.3,6.3,-3.5,2.8],
     [5.6,0.9,8.1,-1.3],
     [7.2,2.3,-4.4,0.5],
     [1.5,0.4,3.7,5.9]]
b= [[1.8],
    [16.6],
    [15.1],
    [36.9]]
AA = A[2]
A[2] = A[1]
A[1] = AA
AA = A[1]
A[1] = A[0]
A[0] = AA
a =A

B = []
k = []
for i in range(len(a)):
    A = a[i]
    bb = []
    for j in range(len(a)):
        q = A[j]/A[i]
        bb.append(q)
    k.append(A[i])
    B.append(bb)


for i in range(len(B)):
    (B[i])[i] = 0

for i in range(len(k)):
    (b[i])[0] = (b[i])[0]/k[i]

x = [1.0,1.0,1.0,1.0]
xxx = [1,1,1,1]
xx = []
x_n = [10]

while abs(1-(x_n[0]/xxx[0])) > 0.000001:
    x_n = []
    for i in range(len(x)):
        bb = B[i]
        s = []
        for j in range(len(x)):
            bx = bb[j]*x[j]
            s.append(bx)
        m = 0
        for k in range(len(s)):
            m = m+s[k]
        x_i = m + (b[i])[0]
        x_n.append(x_i)
    for i in range(len(x)):
        xxx[i] = x[i]
    x = x_n
    xx = x



print(xx)
