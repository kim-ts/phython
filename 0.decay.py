import matplotlib.pyplot as plt 
import numpy as np
from random import random

# time step
h = 1 

# initial numbers
Bi213 = 100000
Pb209 = 0
Tl209 = 0
Bi209 = 0

# decay probability in time h
pBi = 1 - 2**(-h/45.6/60)
pTl = 1 - 2**(-h/2.2/60)
pPb = 1 - 2**(-h/3.3/60/60)

# 213Bi decay ratio
pPbratio = 0.9791

# list for elements
Bi213_list = []
Tl209_lsit = []
Pb209_list = []
Bi209_list = []

t = np.arange(0,1e4,h)
bit = 0

# loop in time
for ti in t:
	Bi213_list.append(Bi213)
	Tl209_lsit.append(Tl209)
	Pb209_list.append(Pb209)
	Bi209_list.append(Bi209)

    # random number to determine if each element will decay
	for i in range(Pb209):
		if random()<pPb:
			Pb209-=1
			Bi209+=1
	
	for i in range(Tl209):
		if random()<pTl:
			Tl209-=1
			Pb209+=1
	
	for i in range(Bi213):
		if random()<pBi:
			Bi213 -=1
			if random()<pPbratio:
				Pb209+=1
			else:
				Tl209+=1
    # print when Bi isotope are equal(in minumtes)
	if Bi213<Bi209 and bit==0:
		print("Equal Time: ",ti/60.0)
		bit += 1

# plot evolve of all the elements
plt.plot(t,Bi213_list,label='Bi213')
plt.plot(t,Tl209_lsit,label='Tl209')
plt.plot(t,Pb209_list,label='Pb209')
plt.plot(t,Bi209_list,label='Bi209')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Number of Atoms')
plt.show()

