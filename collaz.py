# Lucia Saura 17/02/2018
# Collaz Conjeture 
# https://en.wikipedia.org/wiki/Collatz_conjecture

i = 15
while i > 1:
    if i % 2 == 0:
        print(i//2)
        i = i//2
    else:
        print (i * 3 + 1)
        i = i * 3 + 1
