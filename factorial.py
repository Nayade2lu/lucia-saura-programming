#lucia saura 24/03/2018
#factorial

def factor (x):
    #first a name is given to the function and a value assigned
    while x>1:
        x=x-1
        #actualizing the value of x for a smaller number
        if x >1:
        #when x is greater than 1 do the following
            x= x * (x-1)
        # actualize the value of x for the result of x multiplied per x-1
        #not working don't know the reason, maybe I need two values in the loop? one for the x and a different one for the result of the multiplication?
    return x
print (factor (5))
#not working as the loop never ends
