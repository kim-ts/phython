# -*- coding = utf-8 -*-
# @Time : 2022-12-14오후 2:21
# @Author : 金泰式,3180300014
# @Site : 
# @File : dictionary key,value 바꾸기.py
# @Software: PyCharm

# 원래의 dictionary
my_dict = {'key1': 'value1', 'key2': 'value2'}

# dictionary의 key와 value를 바꿔서 새로운 dictionary를 만듭니다.
new_dict = dict((v, k) for k, v in my_dict.items())

# 새로운 dictionary를 출력해봅니다.
print(new_dict)
# 출력: {'value1': 'key1', 'value2': 'key2'}
