import numpy as np
import matplotlib.pyplot as plt 

# set parameters
row=2
col=3

def plot_lis(t,n,phi,k):
    plt.subplot(row,col,k)
    x=np.cos(t)
    y=np.cos(n*t+phi)
    plt.plot(x,y,'r.')
    return

t=np.linspace(0,20*np.pi,4000)

# set initial conditions
n=np.array([1, 1, 1, 2, 4, 8, 2/3.0, 4/3.0, 4/5.0])
phi=np.array([0, np.pi/4, np.pi/2, np.pi/2, np.pi/2, -1.0*np.pi/3, np.pi/2, np.pi/2, np.pi/2])

# plot all six graphs
for i in range(6):
    plot_lis(t,n[i],phi[i],i+1)

plt.savefig('plot_lissajous.png',dpi=120)
plt.show()
