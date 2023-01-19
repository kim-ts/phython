# -*- coding = utf-8 -*-
# @time : 2022-02-06 오후 9:01
# @Author : taesik
# @File : List-enumerate.py
# @Software : PyCharm

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