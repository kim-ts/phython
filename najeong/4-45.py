# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:46
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-45.py
# @Software: PyCharm

a = [1, 2, 3, 4, [5, 6], [7, 8, 9]]
s = 0
for row in a:
       if type(row)==list:
            for elem in row:
               s += elem
       else:
            s += row
print(s)