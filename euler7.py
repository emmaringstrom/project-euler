"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""
import math as m

n = 0
s = 0


while True:
    n = n + 1
    if all([n%i != 0 for i in range(1,m.floor(m.sqrt(n)),2)]):
        s = s + 1
    if s == 10001:
        break
    
print(n): 
