# -*- codeing = utf-8 -*-
# @Time : 2022-01-27 오후 3:33
# @Author : taishi
# @File : 字符串.py
# @Software : PyCharm

word = '문자열'
sentence = "이건 하나의 문장"
paragraph = """
               이건 하나의 문단
               몇줄이고 쓸수 있다."""

print(word)
print(sentence)
print(paragraph)

my_str = "i`m a student"
print(my_str)

'''만약 문장안에'을 쓰려고 한다면'''
my_str1 = 'i\'m a student'
print(my_str1)
'''이와같이 '앞에\를 붙여주면 된다. 
\이것은 '를 단독으로 쓰겠다는 의미이다'''

'''이번엔 만약 큰따옴표가 들어가는 거라면 그때는'''

my_str2="jason said \"I like you\""
print(my_str2)
''' 이런식으로 두번 쓰면 된다.
당연 문자열을 '으로 쓰면 \를 쓸필요없다 '''

my_str3='jason said "I like you'
print(my_str3)


print("예1")
str = "chengdu"
print(str)
print(str[0:6]) #이건 문자열을 0부터 6까지의 위치만큼만 출력하란 의미이다.
print(str[1:4])
print(str[1:7:2]) #이건 1부터 7까지 출력하는데 매번 2만큼 다음글자를 출력하란의미다.
print("예2")
print(str[6:]) #이때 마지막에 언제끝날지를 쓰지않았는데 이는 곧 6부터 마지막까지 쭉출력하란뜻
print(str[:6]) #이것은 시작을 정하지않았으므로 처음부터 6번째까지 쭉출력의 의미가된다.
print("예3")
print(str + "hi")#str에 hi 더하기
print(str*3)#str 곱하기3 즉 3번출력됨
print("예4")
print("hello\nchengdu")#이것의 의미는 헬로랑 청도 사이에 줄띄움을 넣은것이다.
print(r"hello\ncheng   du")#이떄맨앞에r을 넣는다면 이것의 의미는 \n을 사용하지않겠단의미다.