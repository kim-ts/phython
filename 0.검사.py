# -*- coding = utf-8 -*-
# @Time : 2022-03-04오후 5:12
# @Author : 金泰式,3180300014
# @Site : 
# @File : 0.검사.py
# @Software: PyCharm
import sys
import matplotlib.pyplot as plt
import numpy as np

a = 0
k =[]
while a != 1:
    a = input()
    if a == 'q':
        break
    elif a == '':
        pass
    else:
        k.append(a)
print(len(k))
'''
globals()['s1'] = 1
print(globals()['s1'])
'''
'''
for i in range(len(k)):
    b = []
    for j in range(len(k[i])):
        n = k[i][j]
        for l in globals():
            if l[1] == n:
                k[i][j] += 1
'''
m = []
for i in range(45):
    a = i+1
    m.append(a)

b = {}
for i in range(len(m)):
    b[i+1] = m[i]

c = dict((v, k) for k, v in b.items())

for i in range(len(c)):
    for j in range(45):
        a = j + 1
        c[a] = 0

b = []
for i in range(len(k)):
    a = k[i].split(',')
    bb = []
    for j in range(len(a)):
        cc = int(a[j])
        bb.append(cc)
    b.append(bb)

ll = 0
m = 0
for i in b:
    ll += 1
    for j in i:            #j는 숫자하나
        for n in c.keys():
            m = int((1045-ll)/100)
            if n == j:
                c[n] += m
            else:
                pass

print(c)
x = c.keys()
y = c.values()
a1 = 0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
a8=0
a9=0
a10=0
for i in b:
    for j in i:
        j = str(j)
        if j[0] == "1":
            a1 += 1
        if j[0] == "2":
            a2 += 1
        if j[0] == "3":
            a3 += 1
        if j[0] == "4":
            a4 += 1
        if j[0] == "5":
            a5 += 1
        if j[0] == "6":
            a6 += 1
        if j[0] == "7":
            a7 += 1
        if j[0] == "8":
            a8 += 1
        if j[0] == "9":
            a9 += 1
        if j[0] == "10":
            a10 += 1

q = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
tot = 0
for i in range(len(b)):
    v = b[i]
    for j in range(len(v)):
        tot += 1
ratio = []
for i in range(len(q)):
    rv = float(q[i]/tot)*100
    ratio.append(rv)
'''            
num_with_first_digit_one = len([x for x in data if str(x)[0] == "1"])

# 입력 데이터 세트의 총 길이를 계산합니다.
total_num = len(data)

# 첫 번째 숫자가 1인 숫자의 비율을 계산합니다.
ratio = num_with_first_digit_one / total_num
'''
print(q,tot)
k = [1,2,3,4,5,6,7,8,9,10]
plt.plot(k,q)
plt.show()
plt.plot(k,ratio)
plt.show()
plt.scatter(x,y,s=5,c='r' )
plt.plot(x,y,)
plt.show()

