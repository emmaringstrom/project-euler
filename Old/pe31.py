"""In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?"""

num = 0

for a in range(0,3):
    for b in range(0,1+(200-100*a)//50):
        for c in range(0,1+(200-100*a-50*b)//20):
            for d in range(0,1+(200-100*a-50*b-20*c)//10):
                for e in range(0,1+(200-100*a-50*b-20*c-10*d)//5):
                    for f in range(0,1+(200-100*a-50*b-20*c-10*d-5*e)//2):
                        num += 1


print(num+1)