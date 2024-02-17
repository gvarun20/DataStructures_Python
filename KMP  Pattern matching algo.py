# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:10:50 2024

@author: varung
"""

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    # Compute LPS (Longest Proper Prefix which is also Suffix) array
    lps = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j

    # Pattern matching
    j = 0
    i = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                print("Pattern found at index", i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Example usage:
text = "ABABDABACDABABCABAB"
pattern = "AB"
kmp_search(text, pattern)
