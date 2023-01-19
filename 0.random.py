# -*- coding = utf-8 -*-
# @Time : 2022-03-28오후 1:14
# @Author : 金泰式,3180300014
# @Site : 
# @File : 0.random.py
# @Software: PyCharm

import random

#(0,1)범위내 소수점 임의로 생성
a = random.random()

#(n,m)범위내 랜덤 소수점 생성
b = random.uniform(1.2,2.5)

#[n,m]범위내 랜덤으로 임의의수 하나 x생성 n,m은 모두 int형식
c = random.randint(1,10)

#[n,m)범위내 간격2 로 랜덤 임의의수 하나 x생성 n,m,x 모두 int형식
d = random.randrange(1,5,2)

#리스트 중 랜덤선택 하나수
item = [1,2,3,4,5,6,7,8,9,0]
e = random.choice(item)


print(a,b,c,d,e)

''''''
#넘피에서 랜덤생성
import numpy as np

# 랜덤수의 종자 생성
np.random.seed(112)

#n개의 (0,1)사이 임의의 수 생성
a = np.random.random(3)

#[n,m)사이의 k개 정수 생성
b = np.random.randint(1,3,6)

# 리스트중에서 랜덤으로 숫자선택
c = np.random.choice([2,5,7,8,9,11])

# 순서중 숫자 섞기
item = [2,5,7,8,9,11]
np.random.shuffle(item)

#임의의 하나이 2차원수집합 생성
np.random.rand(3,3)

print(np.random.seed(112))
print(a,b,c)
print(item)
print(np.random.rand(3,3))