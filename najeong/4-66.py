# -*- coding = utf-8 -*-
# @Time : 2022-06-22오후 2:54
# @Author : 金泰式,3180300014
# @Site : 
# @File : 4-66.py
# @Software: PyCharm

def selSort(nums):
    n = len(nums) #n =8
    for bottom in range(n - 1): #0~7
        mi = bottom             # 0,1,2,3,4,5,6,7
        for i in range(mi, n):  #0~8,1~8,2~8,...
            if nums[i] < nums[mi]:
                mi = i
        nums[bottom], nums[mi] = nums[mi], nums[bottom]
        print(nums)
    return nums


numbers = [49, 38, 65, 97, 76, 13, 27, 49]
print(selSort(numbers))