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

for nu in range (25200000,243290200817664):
  # this loop sets the range from the minimum common divisor from 1 to 10 and the factorial of 20
  for s in range (11,21):
    # this loop sets the range of numbers from 1 to 20
    if nu % s ==0:
      #the if statement shows the numbers (from 2520,to 20 factorial) that are divisible from the numbers from 1 to 20
      #prints all the numbers that are divisible (it doesn't stop in the first one)
      break 
      #the break is supposed to end the loop 
      #not working because it prints lots of numbers that are divisible not only the first one
      nu=nu+1
print (nu)

