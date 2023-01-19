# -*- coding = utf-8 -*-
# @time : 2022-02-07 오전 2:12
# @Author : taesik
# @File : 함수.py
# @Software : PyCharm

#함수의 정의
def printinfo():
    print("----------------")
    print("djoiesf")
    print("----------------")
'''이것은 정의 일 뿐이므로 출력하지 않는다. 하지만 이 함수를 출력시키는순간 이프린트가 작동한다 예로 밑을 보자'''
#함수의 사용

printinfo()
printinfo()
#파라미터 함수
def add2Num(a,b):
    c = a+b
    print(c)

add2Num(11,22)

'''리턴 사용법'''

def add2(a,b):
    return a+b

add2(13,423)# 단순히 함수 불러오기로는 프린트가 정의되어있지않으므로 출력안댐
print(add2(11,34))
result = add2(11,32)
print(result)
'''위는 여러가지 출력법이다.'''

#여러가지 값의 함수

def divid(a,b):
    shang=  a//b
    yushu = a%b
    return shang,yushu

sh,yu=divid(5,2)  #여러가지로 함수 정의를 대입시킴

print("몫:%d,여수:%d"%(sh,yu))

#응용
print("----------응용부분---------")
def printOneLine():
    print("-"*30)

printOneLine()

print("---------응용 함수--------")
def printNumLine(num):
    i=0
    while i<num:
        printOneLine()
        i+=1

printNumLine(3)

#3개 합
print("-------------3개합-------------")

def sum3Number(a,b,c):
    return a+b+c
print(sum3Number(12,234,35))

#3개 합 평균값 계산
def average3Number(a,b,c):
    sumResult = sum3Number(234,34,23)
    aveResult = sumResult/3.0
    return aveResult

result = average3Number(1,1,1) # 위에서 이미 넘버를 숫자로 정의햇다. 그래서 여기서 a,b,c를 정의해봤자 아무런 영향이없다.
#그러나 만약 위에 sum3Number에 숫자대신 a,b,c를 넣으면 여기서 정의한 1,1,1대로 각각 들어가고 그숫자로 평균값이 구해진다.
print("평균값:%d"%result)
'''예로 이렇게 해보라'''
def s(a,b,c):
    return a+b+c
def i(a,b,c):
    n = s(a,b,c)
    k = n/3.0
    return k
l = i(2,2,2)
print("그때마다 정의해주는 수의 평균:%d"%l)
#
print("----------")
def test():
    a = 300
    print("test:a=%d"%a)
    a = 100
    print("test수정후 :a=%d"%a)

test()

def test1():
    a = 500
    print("test1:a=%d"%a)

test1()

'''각 함수 속의 변수는 그 함수에 속하므로 다른 함수에 영향을 주지 않는다.'''

a = 10 #이렇게 정의 하면 다른함수에서 이 변수를 가져다 쓰게되고 이떄의 a는 모든 함수에 영향을 준다.

def t():
    print(a)
def t2():
    a=5
    print(a)

t()
t2()
'''역시나 함수 자체에서 a를 정의하고 그 함수 자체에서 a를 출력하게되면 함수 자체의 정의를 먼저 따른다.'''

#만약 함수 자체에서 전체함수에 영향을 주는 변수를 바꾸려고 한다면

b=100

def b1():
    #print("전구 함수 수정전값:%d"%b) 왜인지는 몰라도 global 전에 어떠한 명령어도 오면 안되나보다. 오류가뜬다.
    global b
    print("전구 함수 수정전값2:%d"%b)
    b = 2
    print("함수 자체에서 수정후:%d"%b)

def b2():
    print("다른 함수에까지도 영향줌:%d"%b)

b1()
b2()