# -*- coding = utf-8 -*-
# @Time : 2022-06-15오전 3:44
# @Author : 金泰式,3180300014
# @Site : 
# @File : 9.py
# @Software: PyCharm

a,b = input().split(' ')
a = int(a)
b = int(b)
n = 0
for i in range(min(a,b),0,-1):
    if a%i == 0 and b%i ==0:
        n = i
        break
for i in range(max(a,b),(a*b)+1):
    if i%a == 0 and i%b ==0:
        b = i
        break
print(n,' ',b)