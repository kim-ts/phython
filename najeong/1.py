# -*- coding = utf-8 -*-
# @Time : 2022-06-14오후 2:59
# @Author : 金泰式,3180300014
# @Site : 
# @File : 1.py
# @Software: PyCharm

a,b = input().split(';')

a = a.replace(' ','')
b = b.replace(' ','')
print(a,b)
a = a.replace(',','')
a = a.upper()
b = b.upper()
a = list(a)
b = list(b)
t = 0
i = 0
l = []
for i in range(len(b)):
    l.append(b[int(len(b)) - i - 1])
n = 0
while t <1:
    if len(a) != len(l):
        print("no")
        t += 1
        break
    else:
        for i in range(len(l)):
            if a[i] == l[i]:
                n += 1
                pass
            else:
                print("no")
                t += 1
                break
        t += 1
    if n == len(l):
        print("yes")
    else:
        pass

