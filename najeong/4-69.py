# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 3:01
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-69.py
# @Software: PyCharm

def perm(choice,selected=[]):
    if len(choice)==1:
        print("".join(selected+choice))
    else:
        for i in range(len(choice)):
            t=choice[i]
            choice.remove(t)
            selected.append(t)
            perm(choice,selected)
            choice.insert(i,t)
            selected.pop()

first=["1","2","3"]
perm(first,selected=[])