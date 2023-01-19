# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:53
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-64.py
# @Software: PyCharm
def basic_lis(seq):
    l=[1]*len(seq)
    for cur ,val in enumerate(seq):           #enumerate返回元素的"索引和值"
        print(cur,val)
        for pre in range(cur):
            print(pre,seq[pre],val)
            if seq[pre]<val:
                l[cur]=max(l[cur],1+l[pre])
                print(l,seq)
    return max(l)

L=[49, 64, 17, 100, 86, 66, 78, 68, 87, 96, 19, 99, 35]
print(basic_lis(L))