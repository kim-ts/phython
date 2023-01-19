# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:51
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-54.py
# @Software: PyCharm

text="four score and 7 years"
lenwords={s:len(s) for s in text.split()}
print(lenwords["score"])
print(lenwords)