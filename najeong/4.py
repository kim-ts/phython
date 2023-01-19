# -*- coding = utf-8 -*-
# @Time : 2022-06-14오후 10:23
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4.py
# @Software: PyCharm

n = int(input())
m = []
for i in range(n):
    a = int(input())
    m.append(a)
for k in m:
    c = k - 2
    p = 0
    for l in range(2, k):
        if k % l == 0:
            print("No")
            break
    else:
        print("yes")