# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:46
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-46.py
# @Software: PyCharm
x = []
l3=[i+j for i in range(1,6) for j in range(1,6)]
for i in range(1,6):
    for j in range(1,6):
        a = i+j
        x.append(a)

print(x)
print(l3)
print(sum(l3))