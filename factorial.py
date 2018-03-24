#lucia saura 24/03/2018
#factorial 

def factorial (x): 
    #first a name is given to the function and a value assigned
    x = (x-1) * (x-2) * (x-3) * (x-4)
    #here I actualize the number sustracting each time one number more and multiplying them
    return x 
# return the x   
print (factorial (5))
# and in the print statement I call the name of the function and give the value to the x
#I have realized that this function is valid only to number 5
