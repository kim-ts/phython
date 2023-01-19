# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 3:01
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-70.py
# @Software: PyCharm


def func1():
    print("11", end=" ")


def func2():
    print("22", end=" ")


def func3():
    print("33", end=" ")


funclist = [func1, func2, func3]
for func in funclist:
    func()