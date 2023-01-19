# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:53
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-60,dic(eval).py
# @Software: PyCharm

a=10
def func():
    global a
    a=20
    print(a,end=' ')
func()
print(a)