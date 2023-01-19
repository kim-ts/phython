# -*- coding = utf-8 -*-
# @time : 2022-01-29 오후 4:31
# @Author : taesik
# @File : List-삭제.py
# @Software : PyCharm
movieName = ["해리포터","캐리비안해적","뭐가있지또","모르겠다","????"]
print("-------증가전 영화 리스트-------")
for name in movieName:
    print(name)

del movieName[2] #2의 자리 즉 세번쨰요소를 제거하라는의미

print("-------삭제후 명단리스트-------")
for name in movieName:
    print(name)

movieName.pop()  #이 리스트의 마지막 요소를 없애버린다는 의미
print("-------마지막 요소 버린후 명단 리스트-------")
for name in movieName:
    print(name)

movieName.remove("해리포터")
print("-------내가 선택한 요소 삭제 후 명단 리스트-------")
for name in movieName:
    print(name)

'''이때 remove 주의할점: 리무브로 선택한요소가 반복되는거면 제일 먼저나오는거 부터 삭제 시킨다.
예!!'''
print("리무브 예시")
a=["가","나","다","라","다"]
a.remove("다")
for i in a:
    print(i)