# Lucia Saura 24/03/2017
# factorial

def factorial(y):
    #naming the fucntion and the value I will call later
    x=1
    # assigning a value to x
    while x < y-1:
    # loop provided that the x is less than y-1 (I thought the fatorial did not include the multiplication by itself, this is why I was substracting a 1 to the y)
        x=x+1
        #actualise the value of x each time (from 1 to y-1)
        print(x-1)
        #printing the numbers to see that it's looping as expected
    return x
print(factorial(5))
#calling the function and giving y a value
    
