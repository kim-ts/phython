# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:51
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-52.py
# @Software: PyCharm

mat=[[i*3+j+1 for j in range(3)] for i in range(5)]
mattrans=[[row[col] for row in mat] for col in range(3)]
print(mat,mattrans)
print(mattrans[1][3])