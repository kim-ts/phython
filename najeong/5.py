# -*- coding = utf-8 -*-
# @Time : 2022-06-15오전 1:56
# @Author : 金泰式,3180300014
# @Site : 
# @File : 5.py
# @Software: PyCharm

n = []
a = int(input())
for i in range(a):
    b = list(input())
    n.append(b)
'''for i in range(len(n)):
    for j in range(len(n[i])):
        print(j)
        if n[i][j] == '1':
            n[i][j] = 0
        elif n[i][j] == '0':
            n[i][j] = 1
        elif n[i][j] == '9':
            n[i][j] = 3
        elif (n[i][j]) == '8':
            n[i][j] = 4
        elif (n[i][j]) == '7':
            n[i][j] = 5
        elif (n[i][j]) == '5':
            n[i][j] = 7
        elif (n[i][j]) == '4':
            n[i][j] = 8
        elif (n[i][j]) == '3':
            n[i][j] = 9
        elif (n[i][j]) == '2':
            n[i][j] = 10
        else:
            n[i][j] = 2
print(n)
k = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
for i in range(len(n)):
    for j in range(len(k)):
        n[i][j] = int(n[i][j])+int(k[j])
m = []
for i in range(len(n)):
    a = 0
    for j in range(len(n[i])-1):
        a += n[i][j]
    m.append(a)
print(n)
print(m)'''
k = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
for i in range(len(n)):
    for j in range(len(n[i])):
        if n[i][j] == 'X':
            n[i][j] = 10
print(n)
for i in range(len(n)):
    for j in range(len(k)):
        n[i][j] = int(n[i][j])+int(k[j])
m = []
for i in range(len(n)):
    a = 0
    for j in range(len(n[i])-1):
        a += n[i][j]
    m.append(a)
print(n)
print(m)