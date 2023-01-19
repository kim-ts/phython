# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:41
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-43.py
# @Software: PyCharm

i=5
while i>=1:
    num=1
    for j in range(1,i+1):
        print(num,end="xxx")
        num*=2
    print()
    i-=1