# -*- codeing = utf-8 -*-
# @Time : 2022-01-23 오전 6:37
# @Author : taishi
# @File : demo3.py
# @Software : PyCharm
'''
password = input("password")
실행하고 패스워드뜨면 아무거나입력하고 엔터하면 그비번 프린트됨 인풋
print("방금입력한비번은:",password)'''

a=10
print("10:",type(a))
b="abc"
print("abc:",type(b))
c=input("입력:")
print("input된것은:",type(c))
'''이떄 인풋의 타입은 숫자를입력하더라도 str이나온다 
이는 중요한 성질이다 즉.만약 프린트를하는데 인풋한 글자를 프린트하려면 
%s를 써야한다 밑예시'''
print("입력한것이숫자여도형식은str입니다:%s" %c)
'''그러나 만약 c자체를 int로 바꿔버리면 숫자로 인식한다.
비슷한예로 만약 문자형식의 변량을 int로쓰면 그것은 숫자로 인식된다'''

d=("123")
print("d:",type(d))
e = int("123")
print("e:",type(e))
'''여기서 d는 str e는 int인걸 알 수 있다 
그럼 응용하면'''

f = int(input("입력:"))
print("f:",type(f))
print("입력한것은숫자로 인식된다:%d" %f)