# -*- coding = utf-8 -*-
# @time : 2022-02-06 오후 8:30
# @Author : taesik
# @File : dictionary-삭제,del,clear.py
# @Software : PyCharm

info = {"name":"sfe","age":234}
print("del전:%s"%info["name"])

del info["name"]

#print("del후:%s"%info["name"]) #이부분은 없으면 del까지는 가능하다.
#즉 del로 인하여 name자체가 사라졌고 다시불러올 수 없다.

info1 = {"name":"ef","age":234}
print("전부 del로 삭제시키면:%s"%info1)
del info1
#print("전부삭제후:%s"%info1)
#역시 안된다.

'''그럼 clear 은? 어떨까'''

info2 = {"name":"dfes","age":324}

print("claer전:%s"%info2)
info2.clear()
print("claer후:%s"%info2)
#이렇게 claer은 내용물을 없애고 출력이 가능하다.

