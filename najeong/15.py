# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:35
# @Author : 金泰式,3180300014
# @Site : 
# @File : 15.py
# @Software: PyCharm

students=[(3180102988,"褚好"),
                  (3170102465,"王凯亮"),
                  (3160104456,"李永"),
                  (3171104169,"陈鑫"),
                  (318400429,"徐杭诚")]

for row in students: #按行存取
    print(row[0],row[1])
print()

for index in range(len(students)):  #按索引存取
    print(students[index][0],students[index][1])