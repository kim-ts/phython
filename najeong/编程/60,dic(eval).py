# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 2:08
# @Author : 金泰式,3180300014
# @Site : 
# @File : 60,dic(eval).py
# @Software: PyCharm
'''
7
/
3
'''
result={"+":"x+y","-":"x-y","*":"x*y","/":'''x/y if y!=0 else "divided by zero"'''}
x=int(input())
z=input().strip()
y=int(input())
print(result)
print(eval(result.get("+")))
r=eval(result.get(z))
print(r)
if type(r)!=str:
    print(format(r,'.2f'))
else:
    print(r)