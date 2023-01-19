# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 1:29
# @Author : 金泰式,3180300014
# @Site : 
# @File : 57,Pascal's triangle.py
# @Software: PyCharm
'''
4
'''
a = int(input())
x = []
for i in range(a):
    x.append(list(str(11**i)))

for i in range(len(x)):
    for j in range(i+1):
        print(x[i][j],end=' ')
    print()

