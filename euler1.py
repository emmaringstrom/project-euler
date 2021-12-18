#   Project Euler 1
# 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def natsum(n):
    if(n == 3):
        return 3
    else:
        if(n%5 == 0 or n%3 == 0):
            return n + natsum(n-1)
        else:
            return natsum(n-1)

n = 999

print(natsum(n))