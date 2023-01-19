# -*- coding = utf-8 -*-
# @Time : 2022-11-15오후 5:20
# @Author : 金泰式,3180300014
# @Site : 
# @File : 11.py
# @Software: PyCharm
'''
a = 123
l = int(a/2)
m = int(a%2)
print(l)
print(m)

b = 25
c = 25%8
print(c)

d = 10101
print(len(str(d)))
e = 1111
def l(e):
    n = 0
    for i in range(len(str(e))):
        e = str(e)
        if int(e[i]) == 1:
            pass
            n += 1
        else:
            if i+1 == len(e):
                break
            else:
                if int(e[i + 1]) == 1:
                    break
                else:
                    pass
    a = str(e)
    b = a.count('1')
    if b != n :
        n = 0
    else:
        pass
    return n
'''
'''
a = 1101
b = 1010

c = format(a,'08')+ format(b,'08')
print(c)
q  = 10102222
for i in range(len(str(q))+1):
    print(len(str(q))-i)
    if int(q % 10**(len(str(q))-i+1) / 10**(len(str(q))-i)) == 2:
        q += 10**(len(str(q))-i+1)
        q -= 2*10**(len(str(q))-i)

print(q)
a,b,c,d = input().split('.')
a,b,c,d = int(a),int(b),int(c),int(d)
def bin(a):  #2진수 변환
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

print(bin(a))
a = bin(a)
print(a)'''

'''
ip = '01110000001110000010011000000000'
sub = '11111111111111111111111100000000'
k = []
q = 0
for i in range(len(ip)):
    a = int(ip[i]) + int(sub[i])
    k.append(a)
print(k)
for i in range(len(k)):
    q += int(k[i])*10**(len(k)-i-1)
print(q)
print(len(str(q)))
aa = 1
while int(aa) != 0:
    bb = str(q)
    aa = bb.count('2')
    for i in range(len(str(q)) + 1):
        print(i)
        print(len(str(q)))
        if int(q % 10 ** (len(str(q)) - i + 1) / 10 ** (len(str(q)) - i)) == 2:
            q += 10 ** (len(str(q)) - i + 1)
            q -= 2 * 10 ** (len(str(q)) - i)
            print('q',q)
        else:
            pass
    print(q)
    print(aa)
print(q)''''''
k = 26
subnet = '1'*k
subnet = format(subnet,'032')
print(subnet)'''

a = '01110000'
def dex(a):
    sum = 0
    for i in range(len(a)):
        b = int(a[i])*2**(len(a)-i-1)
        sum += int(b)
    return sum