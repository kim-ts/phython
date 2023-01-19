# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:52
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-59.py
# @Software: PyCharm

l=[1]
def scope1():
    l.append(6)
    print(*l)
scope1()