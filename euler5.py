# lucia saura 24/03/2018
# first step euler 5
# identifying prime numbers (code source python tutorial)


for n in range(2, 20):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # loop fell through without finding a factor
         print(n, 'is a prime number')
         #attempt to multiply the prime numbers, not working: it is multiplying the prime number by itself


def factorial3 (num):
#first a name is given to the function and a name to the value that we will be calling at the end (when calling the function)
#in the video source they are doing that asking a number on the shell (don't apply here) 
    x=1
# create a value and assigning to 1 to work with in the for loop
    for i in range (num):
    # loop in the range from 0 to the (num) 
        x=x * num
        # multiply the x for the number given and we obtain the number 
        num = num -1
        #then actualise the number for one less than itself and repeat the process in the for loop wilth all numbers less than the (num) until arriving to 1
    print (x)
    #print the final result of the loop (x)
print(factorial3(20))
# in this statement we call the function and assign a value to (num)
# a 'None' appearing in the terminal after the result (To be investigated)            

