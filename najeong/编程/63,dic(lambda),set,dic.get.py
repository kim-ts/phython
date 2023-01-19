# -*- coding = utf-8 -*-
# @Time : 2022-06-24오전 2:31
# @Author : 金泰式,3180300014
# @Site : 
# @File : 63,dic(lambda),set,dic.get.py
# @Software: PyCharm
'''
8
10 2 0 5 7 2 5 2
'''
'''a = int(input())
b = list(input().split())
x = {}
for i in b:
    n = 0
    for j in b:
        if i == j:
            n += 1
    x[int(i)] = n
x = sorted(x.items(), key = lambda x:x[0])
for i in range(len(x)):
    print("%d:%d"%(x[i][0],x[i][1]))'''

n = int(input())
dic = {}
work_year = [int(year) for year in input().split()]

for year in work_year:
    dic[year] = dic.get(year, 0) + 1

year = set(work_year)

for i in year:
    print(f"{i}:{dic[i]}")