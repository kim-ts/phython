# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:23
# @Author : 金泰式,3180300014
# @Site : 
# @File : 14.py
# @Software: PyCharm

def func(a):
    if a == 0:
        raise ValueError
    elif a == 1:
        raise ZeroDivisionError


i = int(input())
try:
    func(i)
    print("ok")
except Exception as e:
    print(type(e))

