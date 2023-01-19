# -*- coding = utf-8 -*-
# @time : 2022-02-06 오후 8:41
# @Author : taesik
# @File : dictionary-대입,key,value,items.py
# @Software : PyCharm

info = {"id":1,"name":"sref","age":234}
print(info.keys())  #이것은 info안의모든 변량이름을 출력한다.
print(info.values()) #이것은 info안의 모든 정보를 출력시킨다.

print(info.items()) #매 한 단 마다 출력시킨다.

for key in info.keys():
    print(key)
    '''이렇게 하면 info 안의 모든 변량이름들을 하나하나 
    그때마다 key에 집어넣어지고 그 순환떄 그 키가 출력 되므로
    하나씩 변량이름을 출력하게 된다.'''
for i in info.values():
    print(i)
    '''알 수 있듯이 이렇게 하면 
    위와같은 방식으로 모든 정보를
    하나하나 출력하게 될 것이다.'''

for key,value in info.items():
    print("key=%s,value=%s"%(key,value))

'''이것은 items 의 중요한 성질로서 아이템 자체가
각각 한 문단씩 나눠서 출력되는것을 응용하여
이런식으로 한묶음씩 key와value에 들어가서 
각각 출력되게 된다.'''
mylist = ["a","b","c","d"]
for x in mylist:
    print(x)
'''이런 식으로 리스트 각각을 출력 시킬 수 있는데
만약 각각의 위치를 같이 출력시키고싶다면 
'''
print(enumerate(mylist))#이것을 쓰는데

for i,x in enumerate(mylist):
    print(i+1,x)

'''이렇듯 매 위치와 정보를 같이 출력시키게 된다.'''