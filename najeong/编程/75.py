# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 6:55
# @Author : 金泰式,3180300014
# @Site : 
# @File : 75.py
# @Software: PyCharm
'''
[1,2,[3,4,[5,6],7],8]
'''
a = input()
b = ''.join(a)
#print(b)
#print(len(b))
num= 0
sum=0

for i in range(0,len(b)):
    if(b[i]=='['):
        num+=1
    elif(b[i]==']'):
        num-=1
    if b[i].isdigit() and (i!='[') and (i!=']') and b[i]!=',' and b[i+1].isdigit()==False:
        sum = sum+num
       # print(i)
       # print(b[i].isdigit())
print(sum)
