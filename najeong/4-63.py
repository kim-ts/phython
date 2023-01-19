# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:53
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-63,dic(lambda),set,dic.get.py
# @Software: PyCharm
def ins_sort_rec(seq, i):
    print(len(seq))
    print(i)
    if i == 0: return print("nn")
    print("i1",i)
    ins_sort_rec(seq, i - 1)
    print("i2",i)
    j = i
    print(j)
    while j > 0 and seq[j - 1] > seq[j]:
        seq[j - 1], seq[j] = seq[j], seq[j - 1]
        j -= 1
        print("j",j)
        print(seq)

seq = [3,-6,79,45,8,12,6,8]
ins_sort_rec(seq, len(seq)-1)
print(seq[5])
print(seq)