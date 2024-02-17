# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 22:43:48 2024

@author: varung
"""

def search(arr, N, x):
    for i in range(0, N):
        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40, 28, 89, 34, 44]
    x = 44
    N = len(arr)

    result = search(arr, N, x)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
