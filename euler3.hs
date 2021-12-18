
{--
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
--}

largestPrime :: Integer -> Integer
largestPrime n = maximum $ filter ((== 0).(n `mod`)) (getPrimes n)

isPrime :: Integer -> Bool
isPrime n | n < 4 && n > 0 = True 
isPrime 4 = False 
isPrime 5 = True 
isPrime n = all ((/= 0) . (n `mod`)) [3..(n `div` 2)]

getPrimes :: Integer -> [Integer]
getPrimes n = filter isPrime [2..n]
