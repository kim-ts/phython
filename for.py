# -*- codeing = utf-8 -*-
# @Time : 2022-01-24 오후 3:38
# @Author : taishi
# @File : for.py
# @Software : PyCharm

for i in range(5):
    print(i)
    '''i는 임의의 순환변량을 정의한것
    range(5)는 5라는 범위를 정해준것 
    컴퓨터는 0부터시작하고 그렇기때문에
    0,1,2,3,4의 결과가 나온다.'''
print("예 2",end="\n")
for j in range(0,10,3):
    print(j)
    '''이떄는 range(0,10,3)의 의미는
    각각 0부터시작
    10에서 끝남 
    각각순환마다 3을 더함 의의미이다
    그러므로 결과는 0,3,6,9 를 얻는다.'''

print("예 3",end="\n")
for k in range(-10,-100,-30):
    print(k)

    '''마이너스로 가는 순환도 가능
    이제 문자를 순환시켜보자 '''
name = "chengdu"

for x in name:
    print(x)

    '''글자를 하나하나 출력한다. 이제 이거 한칸씩띄어서 출력시키려면'''

for y in name:
    print(y,end="\t") #이렇게 하면 된다.

print("또다른예",end="\n")

a=["aa","bb","cc","dd"]
for n in range(len(a)):
    print(n, a[n])
    '''이때 이것의 의미는 길이가a이고 
범위는 그 길이만큼이란 뜻 즉, a는 총 4개가 있고 
len(a)는 4이다 그럼 range(4) 가되고 즉,n은 0부터 3까지 출력하게된다.
그럼 이때 a[n]이 의미하는것은 a의 각각 n번째 원소라는 뜻으로
a[1]은 컴퓨터는 0부터 인식하므로 2번째 즉, bb를 출력하는것이다.
그러므로 n이1일때 a[1]은 bb이고 그렇게 출력됨을 볼수 있다.'''
