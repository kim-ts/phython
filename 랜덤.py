# -*- codeing = utf-8 -*-
# @Time : 2022-01-23 오후 9:26
# @Author : taishi
# @File : 랜덤.py
# @Software : PyCharm

import random  #랜덤 사용전 명령어

x = random.randint(0,2) #랜덤으로 0부터2사이의 정수를 생성 0,1,2

print(x)


'''가위바위보'''
c=int(x)
y=input("가위=0바위=1보=2 =>")
print(type (c))
print(c)
if c==0:
    if y==0:
        print("비김")
    elif y==1:
        print("이김")
    else:
        print("짐")
elif c==1:
    if y==0:
        print("짐")
    elif y==1:
        print("비김")
    else:
        print("이김")
else:
    if y==0:
        print("이김")
    elif y==1:
        print("짐")
    else:
        print("비김")
print("end")