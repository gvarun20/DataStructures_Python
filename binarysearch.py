# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 22:48:00 2024

@author: varung
"""

def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
