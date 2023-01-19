# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:42
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-44.py
# @Software: PyCharm

i=1
while i<=5:
    num=1
    for j in range(1,i+1):
        print(num,end="G")
        num+=2
    print()
    i+=1