# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 22:52:40 2024

@author: varung
"""
"""  Sequence: 5, 9, 3, 8

(5, 9, 3, 8) -> (3, 9, 5, 8) [Swap 5 and 3]

(3, 9, 5, 8) -> (3, 5, 9, 8) [Swap 9 and 5]

(3, 5, 9, 8) -> (3, 5, 8, 9) [Swap 9 and 8]

After the third iteration, the sequence becomes sorted: (3, 5, 8, 9). """


def insertion_sort(list1):
    for i in range(1, len(list1)):
        a = list1[i]
        j = i - 1

        while j >= 0 and a < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1

        list1[j + 1] = a

    return list1

# Driver code
list1 = [5, 9, 3, 8]
print("The unsorted list is:", list1)
print("The sorted new list is:", insertion_sort(list1))

