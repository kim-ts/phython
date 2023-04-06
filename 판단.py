# -*- codeing = utf-8 -*-
# @Time : 2022-01-23 오전 7:29
# @Author : taishi
# @File : 판단.py
# @Software : PyCharm

'''각각 결과들 기록'''
#if 100:   True
#if True:   True
#if 0:      False
#if False:   False
if 10:
    print("true")
    print("224")
else:
    print("False")
print("\n")
print("두번째 예",end="\n")
score = 77
if score >=98:
    print("성적A")
else:
    print("성적E")
print("\n")
print("세번째 예",end="\n")
score1=87
if score1 >90 and score1 <=100:
    print("성적A")
else:
    if score1 >=80 and score1<90:
        print("성적B")
    print("성적 E")

'''이때 결과의 논리는 첫번쨰if의 else는 
마지막줄과 같은 선상에 있으므로 이 마지막줄로 출력시킨다 
 즉,90~100사이가 아니니까 성적E를 출력 

또 두번쨰 if 에서 80~90사이에 있으므로 성적B를 출력
이렇게 두개가 출력되버린다.
주의!! 마지막줄의 프린트는 첫번째if와 같은선상에 있어야함
안그러면 에러뜸 '''
print("\n")
print("네번째 예")
score2=87
if score2 >90 and score2 <=100:
    print("성적A")
elif score2 >=80 and score2<90:
    print("성적B")
else:
    print("성적 E")

    '''위의 elif를 많이연속해서 써도된다.'''
    print("\n")
print("다섯번째 예")
score3=67
if score3 >90 and score3 <=100:
    print("성적A")
elif score3 >=80 and score3<90:
    print("성적B")
elif score3 >= 70 and score3 < 80:
    print("성적C")
elif score3 >= 60 and score3 < 70:
    print("성적D")
elif score3 >= 0 and score3 < 60:
    print("성적E")
else:
    print("성적 F")



'''응용숫자 바꿔가면서 익숙해지기 연습해보기'''
print("\n")
print("응용문제",end="\n")
성별 = 1 #1은 남자 0은 여자
솔로 = 0 #1은 솔로 0은 여친/남친
if 성별 == 1 :
    print("남성")
    if 솔로 ==1:
        print("남성솔로")
    else:
        print("여친있")
else:
    print("여성")
    if 솔로 == 1:
        print("여성솔로")
    else:
        print("남친있")
