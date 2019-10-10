#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

#选择排序
# 选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，
# 存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
# 以此类推，直到所有元素均排序完毕。
def ze(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    print(arr)
a = [21,4,31,5,6]
ze(a)
