
"""A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

import math as m

def isPalindrome(n):
    s = str(n)
    for i in range(0,m.floor(len(s)/2)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

p = 0

for i in range(100,998):
    for j in range(i+1,999):
        if isPalindrome(i*j) and i*j > p:
            p = i*j

print(p)