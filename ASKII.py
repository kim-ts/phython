# -*- coding = utf-8 -*-
# @Time : 1/6/20239:27 AM
# @Author : 金泰式,3180300014
# @Site : 
# @File : ASKII.py
# @Software: PyCharm

def dex(a): #10진수 변환
    sum = 0
    for i in range(len(a)):
        b = int(a[i])*2**(len(a)-i-1)
        sum += int(b)
    return sum
def bin(a):  #2진수 변환
    if a == 0:
        sum = 0
    elif a == 1:
        sum = 1
    else:
        k = []
        l = 0
        while l != 1:
            l = int(a/2)
            m = int(a%2)
            a = l
            k.append(m)
        k.append(1)
        n=1
        sum = 0
        for i in range(len(k)):
            sum += n*k[i]
            n = n*10
    return sum
