# -*- coding = utf-8 -*-
# @Time : 2022-06-20오후 5:50
# @Author : 金泰式,3180300014
# @Site : 
# @File : 12.py
# @Software: PyCharm

a = eval(input())
b = int(input())
for m in range(b):
    for i in range(len(a)):
        if type(a[i]) == list:
            a = a[i]
            break
print(len(a))
