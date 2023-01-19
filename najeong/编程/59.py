# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 1:57
# @Author : 金泰式,3180300014
# @Site : 
# @File : 59.py
# @Software: PyCharm

'''
4
{'a':{'b':10,'c':6}}
{'b':{'c':2,'d':7}}
{'c':{'d':10}}
{'d':{}}
'''
a = int(input())

x = []
for i in range(a):
    b = eval(input())
    x.append(b)
s = []
l = []
for i in x:
    for j,k in i.items():
        for n,m in k.items():
            s.append(n)
            l.append(m)
s = len(s)
q = 0
for i in range(len(l)):
    q += int(l[i])

print(a,s,q)