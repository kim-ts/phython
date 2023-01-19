# -*- coding = utf-8 -*-
# @time : 2022-01-29 오후 4:06
# @Author : taesik
# @File : List-증가,확장.py
# @Software : PyCharm
''''''

namelist = ["ss","dd","ff"]
print("-------증가전 명단리스트-------")
for name in namelist:
    print(name)
''''''

nametemp = input("이름 입력하시오")
namelist.append(nametemp)        #하나의 요소를 추가
print("-------증가후 명단리스트-------")
for name in namelist:
    print(name)

'''즉 append 는 원래 우리가 정해놓은 리스트에 다른 요소를 추가할 떄 쓴다.'''

'''또 다른예'''

print(end="\n")

a=[1,2]
b=[3,4]
a.append(b)
print(a)

'''이렇게 a에 다른 리스트인 b를 집어넣을수있다. 그러나 b자체 전체를 하나의 요소로 보고 a에 넣어버린다.'''
c=[5,6]
d=[7,8]
c.extend(d)
print(c)         #이것의 의미는 d의 전체를 요소로 보는 것이 아니라 d의 매요소를 c에 넣는다는 의미

''''''
e=[0,1,2]
e.insert(1,3)  #이것의 의미는 두번쨰 위치에 3을 넣으라는 의미 (왜냐면 0부터자리를세므로 1의 자리는 두번쨰칸이다.
print(e)

''''''
'''
'''
''''''''''''


