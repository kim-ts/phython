# -*- coding = utf-8 -*-
# @time : 2022-02-07 오전 2:01
# @Author : taesik
# @File : 집합-종결.py
# @Software : PyCharm

'''[]는 열표로 list고 순서가 있고,형태가 변할 수 있다.
()는 원소조이고 순서가 있고 형태변화가불가
{}는 사전이고 순서가없고 key는 변할 수 없고 value는 변할 수 있다.
집합은 ([])로 쓰고 결과는{}로나온다. 순서가없고 중복되지않는한 변화가능'''


s=  set([1,2,3,6,7,8])
print(s)
s1=set([1,1,2,2,3,3])
print(s1) #보는바와같이 중복이 안된다.
t = ([1,2,3,4,5])
print(t)

t.append(s)
print(t)
del t #이거 이러고 프린트하면 오류뜬다 왜냐면 t자체를 없애버렸기떄문
#print(t) 그러므로 봉인
t = ([1,2,0])
print(t)
t.clear()
print(t)#빈공간으로 만듦
t.extend(s)
print(s)

t[1]=0
print(t) #수정도 아주 잘 된다.
