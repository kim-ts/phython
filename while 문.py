# -*- codeing = utf-8 -*-
# @Time : 2022-01-24 오후 4:05
# @Author : taishi
# @File : while 문.py
# @Software : PyCharm

i=0
while i<5:#i가 5보다작을때 까지 순환이란 의미므로 4까지만 출력된다.
    print("이번은%d차실행순환"%(i+1))#여기i에더하기1한것은 당연히 i가0부터시작인데 그 0이첫번째니까 그렇게 1차실행이라 말하기위해서이다.
    print("i=%d"%i)
    i+=1 #이것의 의미는 매번 순환마다 i자기자신에 +1하란뜻

print(end="\n")
print("1부터100까지의 합은?")
n=1
k=1
sum=1
while k<100:
    n+=1
    print("첫번째",n)
    sum=sum+n
    k+=1
print(sum)

print(end="\n")
print("1부터100까지의 합은?두번째 방법")
n=100
sum=0
counter=1
while counter<=n:
    sum = sum +counter
    counter +=1

print("1부터 %d 까지의 합은:%d"%(n,sum))


print(end="\n")
print("while과else동시사용")
count=0
while count<5:
    print(count,"5보다작다")
    count +=1
else:
    print(count,"5보다크거나같다.")
'''즉 while에서의else는 while이 만족하지않는순간에 사용된다.
예로 카운트 10을 해보라'''