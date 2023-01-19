# -*- coding = utf-8 -*-
# @Time : 2022-06-23오후 11:05
# @Author : 金泰式,3180300014
# @Site : 
# @File : 51.py
# @Software: PyCharm

T = int(input())
s = []
for i in range(T):
    a = int(input())
    z = []
    for j in range(a):
        b = list(input().split())
        z.append(b)
    s.append(z)


for i in s:
    n = 0
    q = 0
    z = 0
    for j in range(len(i)):
        for k in range(len(i[j])):
            if j != k:
                if j < k:
                    if int(i[j][k]) == 0:
                        n += 1
                    else:
                        pass
                elif j > k:
                    if int(i[j][k]) == 0:
                        q += 1
                    else:
                        pass
                else:
                    pass
            else:
                pass
    if n == (int(len(i))**2-int(len(i)))/2:
        print("lower triangular matrix")
    elif q == (int(len(i))**2-int(len(i)))/2:
        print("upper triangular matrix")
    else :
        print("no")