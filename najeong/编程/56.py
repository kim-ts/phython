# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 1:13
# @Author : 金泰式,3180300014
# @Site : 
# @File : 56.py
# @Software: PyCharm
'''
11
'''
n=int(input())
for i in range(n//2+1):
    print(int((n-(2*i+1))/2)*" "+(2*i+1)*"*"+int((n-(2*i+1))/2)*" ")
for i in range(n//2-1,-1,-1):
    print(int((n-(2 * i + 1)) / 2) * " " + (2 * i + 1) * "*" + int((n - (2 * i + 1)) / 2) * " ")