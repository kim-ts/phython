# -*- coding = utf-8 -*-
# @time : 2022-02-01 오후 2:24
# @Author : taesik
# @File : List-숙제.py
# @Software : PyCharm

products=[["iphone,",6888],["MacPro",14800],["xiaomi",2499],["coffee",31],["book",60],["Nike",699]]

s=[]
for l in range(6):
    a = input("물건번호:")
    for i in products:
        k="%s"%i[1]
        if a == k:
            s.append(a)
        if a == "q":
            break
        else:
            continue
print("------ 상품배열방법 ------", end="\n")
o=int(len(s))
m=[]
for d in range(o):
    print(d)
    for n in range(6):
        print("n",n)
        product = products[n][1]
        print("product",product,type(product))
        u="%s"%product

        print("s[d]",s[d],type(s[d]))
        if s[d] == u:
            m.append(products[n][0])
            print(products[n][0])
        else:
            continue
print(m)
print("------ 상품배열 ------", end="\n")
for b in range(o):
    print(b, end="\t")
    print(m[b],end="\t")
    print(s[b], end="\n")