# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 3:02
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-78.py
# @Software: PyCharm

def area(r):
    assert r >= 0, "参数错误,半径小于0"
    s = 3.14159 * r * r
    return s


r = float(input())
try:
    print(area(r))
except AssertionError as msg:
    print(msg)