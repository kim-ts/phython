# -*- coding = utf-8 -*-
# @Time : 2022-06-15오후 2:17
# @Author : 金泰式,3180300014
# @Site : 
# @File : 10.py
# @Software: PyCharm

import  re
a = []
while len(a) < 10:
    x = 0
    n = []
    while x < 1:
        a = input()
        for i in a:
            if i == '#':
                x += 1
            else:
                pass
        n.append(a)


    for i in range(len(n)):
        n[i] = re.sub(r"[^a-zA-Z0-9 _]","",n[i])
    n.remove('')
    n.remove('')
    for i in range(len(n)):
        n[i] = n[i].upper()


    a = []
    for i in range(len(n)):
        a.extend(n[i].split(' '))
    a.remove('')

'''p = []
for i in range(len(a)):
    if len(a[i]) <= 1 :
        p.append(a[i])
for i in range(len(p)):
    a.remove('%s'%p[0])''' #1글자는 단어로 안치는줄 알았는데 1글자도 단어로 포함

if len(a)<10:
    pass
else:
    for i in range(len(a)):
        if len(a[i]) > 15:
            if 80> len(a[i]) > 15:
                a[i] = a[i][:15]
            elif len(a[i]) > 80:
                a.remove(a[i])
            else:
                pass
        else:
            pass
    n = {}
    for i in a:
        m = 0
        for j in range(len(a)):
            if i == a[j]:
                m += 1
            else:
                pass
            n[i] = m
    aa = 0
    print(n,a,aa)
    for i in n.keys():
        aa += 1

    key = []
    value = []
    for i,j in n.items():
        key.append(i)
        value.append(j)

    aaa = round(aa*0.1)
    v = []
    for i in range(aaa):
        x = max(value)
        mm = 0
        for j in range(len(value)):
            if value[j] == x:
                mm = j
                break
        y = key[mm]
        z = [x,y]
        v.append(z)
        value.remove(x)
        key.remove(y)
    print(aa)
    for i in range(len(v)):
        print("%s:%s"%(v[i][0],v[i][1]))