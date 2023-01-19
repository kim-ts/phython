# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 3:02
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-77.py
# @Software: PyCharm
try:
    x = float("abc123")
    print("数据类型转换完成")
except IOError:
    print("This code caused an IOError")
except ValueError:
    print("This code caused an ValueError")