# lucia saura 24/03/2018
# first step euler 5
# identifying prime numbers (code source python tutorial)


for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # loop fell through without finding a factor
         print(n * n, 'multiplication of prime numbers')
         #attempt to multiply the prime numbers, not working: it is multiplying the prime number by itself

