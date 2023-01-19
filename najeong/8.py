# -*- coding = utf-8 -*-
# @Time : 2022-06-15오전 3:31
# @Author : 金泰式,3180300014
# @Site : 
# @File : 8.py
# @Software: PyCharm

n,s = input().split(' ')
n = int(n)
s = int(s)
if s < 250:
    pass
elif 250<= s <500:
    s = s*0.98
elif 500<= s <1000:
    s = s*0.95
elif 1000<= s <2000:
    s = s*0.92
elif 2000<= s <3000:
    s = s*0.90
else:
    s = s*0.85

a = int(s*n)
print(a)