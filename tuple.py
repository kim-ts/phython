# -*- coding = utf-8 -*-
# @time : 2022-02-05 오후 7:59
# @Author : taesik
# @File : tuple.py
# @Software : PyCharm

'''tuple 은 list와 비슷하지만 그성질이 더 큰 범위를 포괄한다.
tuple 은 그 안에 list를 포함할 수 있다.'''

tup = ()
print(type(tup))
tup1 = (50)
print(type(tup1))# 이떄 이건 tuple이 아니다. 그냥 50하나는 그저 50을가지는 하나의 변량표현일 뿐이다.
'''만약 원소조tuple 형태로 쓰려면'''
tup2 = (50,)
print(type(tup2))

tup3 = ("abc","def",2020,22,33,44,55,66,77)
print(tup3[0])
print(tup3[-1])
print(tup3[1])
print(tup3[-2])
print(tup3[1:5])#1의자리부터 5의자리까지면 1,2,3,4,5 이렇게 5개가 나와야할 것 같지만 왼쪽은 열려있고
#오른쪽은 닫혀있는 것이 파이썬 특징이어서 1,2,3,4의자리까지만 출력된다.
print(tup3[1:10])# 범위가 초과되도 오류는 안뜨고 마지막자리까지 출력