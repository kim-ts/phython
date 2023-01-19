# -*- coding = utf-8 -*-
# @Time : 2022-03-22오전 2:12
# @Author : 金泰式,3180300014
# @Site : 
# @File : 0.에러바 예제.py
# @Software: PyCharm

import matplotlib.pyplot as plt

## color code
# b: blue
# g: green
# r: red
# c: cyan
# m: magenta
# y: yellow
# k: black
# w: white

## marker style
# ================ ===============================
# character description
# ================ ===============================
# - solid line style
# -- dashed line style
# -. dash-dot line style
# : dotted line style
# . point marker
# , pixel marker
# o circle marker
# v triangle_down marker
# ^ triangle_up marker
# < triangle_left marker # > triangle_right marker
# 1 tri_down marker
# 2 tri_up marker
# 3 tri_left marker
# 4 tri_right marker
# s square marker
# p pentagon marker
# * star marker
# h hexagon1 marker
# H hexagon2 marker
# + plus marker
# x x marker
# D diamond marker
# d thin_diamond marker
# | vline marker
# _ hline marker
# ================ ===============================

## Drawing each lines
# plot first line graph
plt.errorbar(
    [0.3, 1, 2, 3],  # X
    [1000, 400, 90, 16],  # Y
    yerr=[54, 12, 41, 4],  # Y-errors
    fmt="ro-",  # format line like for plot()
    linewidth=2,  # width of plot line
    elinewidth=0.5,  # width of error bar line
    ecolor='k',  # color of error bar
    capsize=3,  # cap length for error bar
    capthick=0.5  # cap thickness for error bar
)
# plot second line graph
plt.errorbar(
    [0.3, 1, 2, 3],  # X
    [1120, 340, 49, 46],  # Y
    yerr=[134, 124, 21, 9],  # Y-errors
    fmt="bo-",  # format line like for plot()
    linewidth=2,  # width of plot line
    elinewidth=0.5,  # width of error bar line
    ecolor='k',  # color of error bar
    capsize=3,  # cap length for error bar
    capthick=0.5  # cap thickness for error bar
)
# plot Third line graph
plt.errorbar(
    [0.3, 1, 2, 3],  # X
    [619, 674, 359, 126],  # Y
    yerr=[44, 34, 21, 13],  # Y-errors
    fmt="ko-",  # format line like for plot()
    linewidth=2,  # width of plot line
    elinewidth=0.5,  # width of error bar line
    ecolor='k',  # color of error bar
    capsize=3,  # cap length for error bar
    capthick=0.5  # cap thickness for error bar
)

## Settings
# plt.legend() # show figure legend
plt.ylabel('Concentration(ng/ml)')
plt.xlabel('Hours')
plt.title('Python plot')
plt.yscale('log')  # Set y-axis scale
# plt.xlim((0.5,4.5)) #Set X-axis limits
# plt.ylim((0,100)) #Set Y-axis limits
# plt.xticks([1,2,3,4]) #get only ticks we want
# plt.yticks([0,5,10,15,20])

## showing plot
plt.show()