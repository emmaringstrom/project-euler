"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

import math as m

def isPrime(n):
    all([n%i != 0 for i in range(2,m.floor(n/2))])

n = 1
s = 1

while s < 10001:
    n = n + 2 
    if isPrime(n):
    	s = s + 1

print(n) 
