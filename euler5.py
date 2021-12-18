
"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
import math as m

n = m.factorial(20)

while (n > 0):
    n = n - 1
    for i in range(11,21):
        if (n%i != 0):
            break
        elif (i == 20):
            smallest = n
            n = 0
    

print(smallest)