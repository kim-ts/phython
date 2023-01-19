# -*- coding = utf-8 -*-
# @Time : 2022-06-23오후 10:36
# @Author : 金泰式,3180300014
# @Site : 
# @File : 50.py
# @Software: PyCharm

l=list(input().split(" "))
for i in range(len(l)):
    l[i] = int(l[i])

s1=int(l[0])+int(l[1])+int(l[2])
s2=int(l[3])+int(l[4])+int(l[5])
s3=int(l[6])+int(l[7])+int(l[8])
s4=l[0]+l[3]+l[6]
s5=l[1]+l[4]+l[7]
s6=l[2]+l[5]+l[8]
s7=l[0]+l[4]+l[8]
s8=l[2]+l[4]+l[6]
print(l)
print(s1)
print(max(s1,s2,s3,s4,s5,s6,s7,s8))