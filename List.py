# -*- coding = utf-8 -*-
# @time : 2022-01-29 오후 3:45
# @Author : taesik
# @File : List.py
# @Software : PyCharm

namelist = [] # 정의: 비어있는 리스트표
namelist1 = ["ss","dd","ff"]
print(namelist1[0])
print(namelist1[-2])#-로 불러낼 수 있다. 제일 앞이 0의자리이고 -1의자리면 맨마지막이된다 즉,ff 그럼 -2는 dd이다.
print(namelist1[2])
print(namelist1[1:5])#1의 자리부터 5의자리까지 출력하는데 2의자리까지밖에없으므로 1,2의자리만출력하고 그뒤는 출력안된다. 하지만 오류는 안뜬다.
testlist = [1,"sdf"]
print(type(testlist[0]))
print(type(testlist[1]))   #이 결과를 보면 리스트는 여러형태를 혼합으로 쓸 수 있다. int,str

for name in namelist1:
    print(name)#이것은 각각 네임리스트에있는것들을 전부  for순환으로 출력하는 법이다.

print(len(namelist1)) #그 리스트의 길이를 의미한다 총3개이므로 길이는 3이다.

length = len(namelist1)

i=0
while i<length:
    print(namelist1[i])
    i+=1
    '''이것은 네임리스트 길이가 총 3이고 그걸이용해서 임의의 변량을 만들어 3을 길이로 넣고
    그다음 while을 이용하여 그 길이만큼의 범위에서 그 네임리스트를 각각 출력하는 방법이다.'''

