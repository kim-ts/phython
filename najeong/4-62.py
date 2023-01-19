# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:53
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-62.py
# @Software: PyCharm

import math
def factors(x):
    y=int(math.sqrt(x))
    print("?")
    for i in range(2,y+1):
        print(i)
        if (x%i ==0):
            print(x//i)
            factors(x//i)
            break
        else:
            print(x%i)
            print(x,end=' ')
        return
factors(38)

print(int(math.sqrt(38)))