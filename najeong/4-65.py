# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:53
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-65.py
# @Software: PyCharm

def bubble(List):
    for j in range(len(List)-1,0,-1):
        print(j)
        for i in range(0,j):
            print(i)
            if List[i]>List[i+1]:
                List[i],List[i+1]=List[i+1],List[i]
            return List

testlist = [49, 38, 65, 97, 76, 13, 27, 49]
print(testlist)
print( bubble(testlist))
print(testlist)