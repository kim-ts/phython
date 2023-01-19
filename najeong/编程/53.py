# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 12:56
# @Author : 金泰式,3180300014
# @Site : 
# @File : 53.py
# @Software: PyCharm
'''
4 5
1 1 1 1 1
1 3 9 3 1
1 5 3 5 1
1 1 1 1 1
'''
a,b = input().split()
a,b = int(a),int(b)
x=[]
for i in range(a):
    c = list(input().split(' '))
    x.append(c)

q = 0
for i in range(a):
    for j in range(b):
        if i == 0 or i == a-1 or j == 0 or j == b-1:
            pass
        else:
            if x[i][j] > x[i-1][j] and x[i][j] > x[i+1][j] and x[i][j] > x[i][j-1] and x[i][j] > x[i][j+1]:
                print(x[i][j],i+1,j+1)
                q += 1
if q == 0:
    print(None,a,b)