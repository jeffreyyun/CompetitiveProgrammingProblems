# Category: Algorithms - Implementation
# Difficulty: Medium

#!/bin/python3
from math import sqrt, floor

s = input().replace(" ", "")

"""
Explanation:
Let F = floor(sqrt(len(s))), C = ceil(sqrt(len(s)))

Case where len(s) is perfect square:
F = C, then rows = cols = F, and we arrange the words in a square.

Case where len(s) is not perfect square:
The extra letters require 1 additional column, thus rows = F, cols = F + 1
"""
L = floor(sqrt(len(s)))
rows = L+1
cols = L if L*L==len(s) else L+1

for i in range(cols):
    # print the column (every j-th word in the string)
    for j in range(rows):
        ind = i+j*cols
        if ind < len(s):    # print if more letters, else leave this spot empty
            print(s[ind], end="")
    print(" ", end="")