# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:52
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-55.py
# @Software: PyCharm

dic1 = {"姓名": "xiaoming", "年龄": 27}
dic2 = {"性别": "male","年龄": 30}
dic3 = {k:v for d in [dic1, dic2] for k,v in d.items()}
a = {}
for d in [dic1,dic2]:
    print(d)
    for k,v in d.items():
        a[k] = v
        print(k,v)
print(a)
print(dic3)
print(dic3["年龄"])
