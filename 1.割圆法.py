# -*- coding = utf-8 -*-
# @Time : 2022-02-28 오후 1:01
# @Author : 金泰式，3180300014
# @File : 1.割圆法.py
# @Software: PyCharm

import math

l1=1                     #圆内部的n角形（n=6开始）的一个边的长度，六角形的一个边是跟r的长度一样
l2=math.sqrt(3)/2        #n角形切到n个三角形之后把那个三角形再切成两个三角形的时候切的那个线长度
r=1                      #圆半径
pi_different = 0.1       #随意定义了一个内外pi值的差
t = math.pow(10,-11)     #精密度要求
n=6                      #开始六角形

while t < pi_different:
    a=l1*l2/2             #圆里面的n角形切到n个三角形之后一个三角形面积
    pi_1=a*n/pow(r,2)     #里面三角形面积乘以n就是里面n角形的面积，这是可以近似圆的面积，这来算pi值（pi*半径^2=圆里面n角形面积）
    l3=l1*r/(2*l2)        #圆外面的n角形的一个边长的一半长度
    b=l3*r                #圆外面的n角形切到n个三角形之后一个三角形面积
    pi_2=b*n/r            #外面三角形面积乘以n就是里面n角形的面积，这是可以近似圆的面积，这来算pi值（pi*半径^2=圆外面n角形面积）
    print("第%s角形，pi里面：%s，pi外面：%s，pi=%s"%(n,pi_1,pi_2,(pi_1+pi_2)/2))
    pi_different=pi_2-pi_1        #圆内外n角形的面积之差，这是表示所求到的圆的精密度
    l1_1=math.sqrt(pow(l1/2,2)+pow(r-l2,2))    #一个边切成2个边之后新l1
    l2_1=math.sqrt(pow(r,2)-pow(l1_1/2,2))     #一个边切成2个边之后新l2
    n=n*2                                      #所边切成2个所以总边数两倍了
    l1=l1_1
    l2=l2_1



