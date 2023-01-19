# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 2:56
# @Author : 金泰式,3180300014
# @Site : 
# @File : 65.py
# @Software: PyCharm
'''
1000  100000
'''
a,b =input().split()
a =int(a)
b = int(b)
n =0
for i in range(a,b+1):
    if i%3 == 0 and i%5 == 0 and i%7 == 0:
        n += 1
print(n)