# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 3:29
# @Author : 金泰式,3180300014
# @Site : 
# @File : 67.py
# @Software: PyCharm
'''
2,7,11,15
9
또는
3,6,9
10
'''
a = input().split(',')
b = int(input())
k = 0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        s = int(a[i])+int(a[j])
        if s == b:
            print(i,j)
            k  += 1
            break
if k == 0:
    print("no answer")