# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:53
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-61.py
# @Software: PyCharm

b, c=2, 4
def g_func(d):
    global a
    a=d*c
g_func(b)
print(a)
