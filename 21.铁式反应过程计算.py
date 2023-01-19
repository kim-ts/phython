# -*- coding = utf-8 -*-
# @Time : 2022-04-04오후 4:48
# @Author : 金泰式,3180300014
# @Site : 
# @File : 21.铁式反应过程计算.py
# @Software: PyCharm


import random
import numpy as np
Bi213 = 10**5
t_Bi_213 = 45.6*60
t_Tl = 2.2*60
t_pb = 3.3*60
po,Tl = 0,0
pb = 0
Bi209 = 0
for t in range(10000):
    #print("Bi213=%s,Bi209=%s,pb=%s,Tl=%s" % (Bi213, Bi209, pb, Tl))
    #print("%dh %dmin %dsec"%(t//3600,(t%3600)//60,(t%3600)%60))
    dt = 1
    p_Bi_213 = (np.log(2)*dt/t_Bi_213)*100
    for i in range(Bi213):
        p = random.randint(1, 10000000000) * 0.00000001
        a = random.randint(1, 10000)
        if p_Bi_213 >= p:
            Bi213 -= 1
            if a <= 9791:
               po +=1
               pb +=po
               po = 0
            else:
                Tl +=1
        else:
            pass
    p_Tl = (np.log(2)*dt/t_Tl)*100
    for i in range(int(Tl)):
        p = random.randint(1, 10000000000) * 0.00000001
        if p_Tl >= p:
            Tl -= 1
            pb += 1
        else:
            pass
    p_pb = (np.log(2)*dt/t_pb)*100
    for i in range(pb):
        p = random.randint(1, 10000000000) * 0.00000001
        if p_pb >= p:
            pb -= 1
            Bi209 += 1
        else:
            pass
    if Bi209 > Bi213:
        print("Bi213=%s,Bi209=%s,pb=%s,Tl=%s"%(Bi213,Bi209,pb,Tl))
        print("%dh %dmin %dsec" % (t // 3600, (t % 3600) // 60, (t % 3600) % 60))
        break
    else:
        pass

print("Bi213=%s,Bi209=%s,pb=%s,Tl=%s"%(Bi213,Bi209,pb,Tl))