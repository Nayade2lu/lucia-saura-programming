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
        r= x * (x+1)
        #show the result of the multiplication of the numbers I got in the loop
    return r
    #return the result
print(factorial(5))
#calling the function and giving y a value
    
