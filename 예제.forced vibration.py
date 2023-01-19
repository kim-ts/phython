# -*- coding = utf-8 -*-
# @Time : 2022-03-25오후 8:26
# @Author : 金泰式,3180300014
# @Site : 
# @File : 예제.forced vibration.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt

"""
Forced vibration
Forced vibration

"""


def f(x, v, t):
    k = 1.0
    gamma = 0.1
    return -k * x - 2 * gamma * v + 2 * np.sin(t)


M = 1.0  # mass: 1 Kg
t0 = 0.0
t1 = 50.0

N = 1000

del_t = (t1 - t0) / N  # time grid

tpoints = np.arange(t0, t1, del_t)
xpoints = []
vpoints = []

# initial condition
x0 = 0.0
v0 = 1.0

x, v = x0, v0

for t in tpoints:
    xpoints.append(x)
    vpoints.append(v)
    k1v = f(x, v, t) * del_t / M
    k1x = v * del_t

    k2v = f(x + k1x / 2, v + k1v / 2, t + del_t / 2) * del_t / M
    k2x = (v + k1v / 2) * del_t

    k3v = f(x + k2x / 2, v + k2v / 2, t + del_t / 2) * del_t / M
    k3x = (v + k2v / 2) * del_t

    k4v = f(x + k3x, v + k3v, t + del_t) * del_t / M
    k4x = (v + k3v) * del_t

    v += (k1v + 2 * k2v + 2 * k3v + k4v) / 6
    x += (k1x + 2 * k2x + 2 * k3x + k4x) / 6

plt.plot(tpoints, xpoints, 'o', label='4th order Runge-Kutta')
plt.xlabel("t", fontsize=24)
plt.ylabel("x(t)", fontsize=24)

# tt=np.arange(t0, t1, 0.01*del_t)
# plt.plot (tt, np.sin(tt), '-',label='Exact: Sin (t)',color = 'Green')
plt.legend(loc='upper right')

plt.show()

plt.plot(tpoints, vpoints, 'o', label='4th order Runge-Kutta')
plt.xlabel("t", fontsize=24)
plt.ylabel("v(t)", fontsize=24)

# tt=np.arange(t0, t1, 0.01*del_t)
# plt.plot (tt, np.cos(tt), '-',label='Exact: Cos (t)', color = 'red')
plt.legend(loc='upper right')

plt.show()