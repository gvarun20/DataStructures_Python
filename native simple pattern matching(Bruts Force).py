# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:10:08 2024

@author: varung
"""
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            print("Pattern found at index", i)

# Example usage:
text = "ABABDABACDABABCABAB"
pattern = "ABD"
naive_search(text, pattern)

