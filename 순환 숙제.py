# -*- codeing = utf-8 -*-
# @Time : 2022-01-25 오후 2:35
# @Author : taishi
# @File : 순환 숙제.py
# @Software : PyCharm

for i in range(1,10):

    for j in range(1,i+1):
        n=i*j
        print("%d*%d=%d"%(i,j,n),end="\t")
    print(end="\n")

print(end="\n")
print(end="\n")
'''while 쓰기'''
a=0
b=1
while a<9:
    a+=1
    b=1
    while b<a+1:
        o=a*b
        print("%d*%d=%d" % (a, b, o), end="\t")
        b+=1
    print(end="\n")