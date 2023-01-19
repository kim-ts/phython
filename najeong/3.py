# -*- coding = utf-8 -*-
# @Time : 2022-06-14오후 4:31
# @Author : 金泰式,3180300014
# @Site : 
# @File : 3.py
# @Software: PyCharm
'''AEIOU
HELLO World!'''
a = list(input())
b = list(input())
n = 0
for i in a:
    for j in b:
        if i in j:
            n +=1
print(n)