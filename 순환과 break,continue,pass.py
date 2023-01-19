# -*- codeing = utf-8 -*-
# @Time : 2022-01-24 오후 4:33
# @Author : taishi
# @File : 순환과 break,continue,pass.py
# @Software : PyCharm

for letter in 'Room':
    if letter == 'o':
        pass
        print('pass')
    print(letter)
    '''이떄 pass는 아무것도 안한다 
    그냥 공간차지할뿐다. for순환문은 pass가있던없던 똑같이작동하고
    결과물에 출력된 pass문자는 print의 작용때문에 나온것일뿐
    pass는 결과에 아무런 영향을 안준다.'''

i=0
while i<10:
    i=i+1
    print("-"*30) #30개의-를 출력하란의미다.
    if i==5:
        break
    print(i)
'''예상대로 5에서 멈추라는 의미가 된다. 
분명 while 문에서 i 가9까지 출력되어야 하는데
중간에 i가 5면멈추게되어있으므로 비록 범위가 9까지일지라도
5에서 멈추게된다.'''
print(end="\n")
print("continue는??")
i=0
while i<10:
    i=i+1
    print("-"*30)
    if i==5:
        continue
    print(i)
    '''결과를 보면 알 수 있듯이 컨티뉴가 나온 그시점부터
    그뒤의 모든 명령을 건너뜀을 알 수 있다.
    원래대로라면 -30개이후 5를 출력해야하지만 컨티뉴때문에
    뒤의 프린트 i 가 건너뛰어지면서 5를 출력안하게되었다
    단,while자체를 건너뛴것은 아니다.
    즉,컨티뉴 이후의 while 순환해야할 것들을 건너뛰는것이다.'''

    '''break는 순환자체를 멈추는것
       continue는 그 차수의 순환을 멈추는것'''
