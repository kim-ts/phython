# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 3:00
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-68.py
# @Software: PyCharm

lst=[(1,"one"),(2,"two"),(3,"three"),(4,"four")]
print(lst)
lst.sort(key=lambda x:x[1], reverse=True)
print(lst)
print(lst[3][1][2])