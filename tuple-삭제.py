# -*- coding = utf-8 -*-
# @time : 2022-02-05 오후 8:18
# @Author : taesik
# @File : tuple-삭제.py
# @Software : PyCharm

tup1 = (12,34,56)
print(tup1)
del tup1
'''여기까지는 오류가뜨지않는다. 하지만 
삭제후 tup1을 출력시키는것에서부터는 오류가발생한다.'''
print(tup1)#이부분을 주석처리하고 보면 알수있다.