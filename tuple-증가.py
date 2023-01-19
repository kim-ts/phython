# -*- coding = utf-8 -*-
# @time : 2022-02-05 오후 8:12
# @Author : taesik
# @File : tuple-증가.py
# @Software : PyCharm

'''먼저 tuple 은 수정이 불가하다
밑의 주석처리된 부분을 실행시켜보면 오류가 뜬다.'''
'''tup=(12,34,56)
tup[0] = 1000'''

#그러므로 tuple 을 증가시키고 싶다면 다른 tuple을 만들어 둘을 합친다.
tup1 = (12,34,56)
tup2 = ("abc","def")
tup = tup1+tup2
print(tup)
'''이부분이 list와 다른부분 원래 tup1자체를 증가시키는 것이 아니라 완전히 새로운 
변량을 만들고 그것에 원래 tup1과 증가시키고싶은것을 합치는것이다.'''
