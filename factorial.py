#lucia saura 24/03/2018
#factorial

def factor (x):
    #first a name is given to the function and a value assigned
    while x !=0:
        #when x is greater than 0 do the following
        x= x * (x-1)
        # actualize the value of x for the result of x multiplied per x-1
        #not working because the loop never gets to x=0 (the number is bigger and bigger each time and never ends)
    return x
print (factor (4))
#not working as the loop never ends
