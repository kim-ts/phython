# -*- coding = utf-8 -*-
# @Time : 2022-12-03오후 10:23
# @Author : 金泰式,3180300014
# @Site : 
# @File : testtest.py
# @Software: PyCharm

print("할당IP (10진수):")
a,b,c,d = input().split('.')
a,b,c,d = int(a),int(b),int(c),int(d)
def dex(a): #10진수 변환
    sum = 0
    for i in range(len(a)):
        b = int(a[i])*2**(len(a)-i-1)
        sum += int(b)
    return sum
def bin(a):  #2진수 변환
    if a == 0:
        sum = 0
    elif a == 1:
        sum = 1
    else:
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
def subneterror(e):    # 서브넷 마스크 오류판단
    n = 0
    if e == 0 :
        n = 0
    else :
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
            n = 999
        else:
            pass
    return n


if int(a) > 255 or int(b) > 255 or int(c) > 255 or int(d) > 255:
    print('ip format error')
else:
    a = bin(a)
    b = bin(b)
    c = bin(c)
    d = bin(d)
    print("subnet mask(10진수) :")
    e,f,g,h = input().split('.')
    e,f,g,h = int(e),int(f),int(g),int(h)
    if int(e) > 255 or int(f) > 255 or int(g) > 255 or int(h) > 255:
        print('subnet mask error')
    else:
        e = bin(e)
        f = bin(f)
        g = bin(g)
        h = bin(h)
        ee = subneterror(e)
        ff = subneterror(f)
        gg = subneterror(g)
        hh = subneterror(h)
        if ee ==999 or ff ==999 or gg ==999 or hh == 999:
            print('subnet mask format error1')
        else:
            print("쪼갤 개수(단위:bit수) :")
            n = input()
            n = int(n)
            k = ee + ff + gg + hh + int(n)   # 쪼갤 프리픽스 값
            if k > 30:
                print('PREFIX error')
            else:
                ip = format(a,'08')+format(b,'08')+format(c,'08')+format(d,'08')
                subnet = '1' * k
                subnet = format(subnet, '032')
                l = []
                ipip = []
                broad = []
                for m in range(2**n):
                    a = bin(m)
                    a = format(a,'0%d'%n)
                    if n == 0:
                        ip = ip[0:k-n] + a + ip[k:]
                    else:
                        ip = ip[0:k - n] + a + ip[k:]
                    ipip.append(ip)
                    kk = []
                    q = 0
                    for i in range(len(ip)):
                        print(ip,subnet)
                        a = int(ip[i]) + int(subnet[i])
                        if a == 2:
                            kk.append(1)
                        else:
                            kk.append(0)
                    for i in range(len(kk)):
                        q += int(kk[i]) * 10 ** (len(kk) - i - 1)
                    l.append(format(q,'032'))
                for i in range(2**n):
                    a = l[i]
                    c = '1'*(32-k)
                    b = a[0:k] + c
                    broad.append(b)


dexip = []
dexbroad = []
binip = []
binbroad = []


for i in range(len(l)):
    dip = l[i]
    dbr = broad[i]
    u = []
    uu = []
    for j in range(4):
        a = dip[j*8:(j+1)*8]
        b = dbr[j*8:(j+1)*8]
        u.append(a)
        uu.append(b)
    binip.append(u[0]+'.'+u[1]+'.'+u[2]+'.'+u[3])
    binbroad.append(uu[0]+'.'+uu[1]+'.'+uu[2]+'.'+uu[3])
    du = []
    duu = []
    for m in range(4):
        a = u[m]
        b = uu[m]
        a = dex(a)
        b = dex(b)
        duu.append(str(b))
        du.append(str(a))
    dexip.append(du[0] + '.' + du[1] + '.' + du[2] + '.' + du[3])
    dexbroad.append(duu[0] + '.' + duu[1] + '.' + duu[2] + '.' + duu[3])

qqqq = []
qq = []
for i in range(4):
    a = subnet[i * 8:(i + 1) * 8]
    qqqq.append(a)
    b = dex(a)
    qq.append(str(b))
subnetmask = qqqq[0] + '.' + qqqq[1] + '.' + qqqq[2] + '.' + qqqq[3]
subnetmaskdex = qq[0] + '.' + qq[1] + '.' + qq[2] + '.' + qq[3]

for i in range(len(binip)):
    print('%d번째 네트워크 : '%(i+1) + binip[i] + '-->' + dexip[i])
    print('%d번째 브로드캐스트 : '%(i+1) + binbroad[i] + '-->' + dexbroad[i])
    print('subnet mask : ' + subnetmask + '-->' + subnetmaskdex)
    print('총 ip개수 : %d'%2**(k-n-n))