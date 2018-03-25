# Lucia Saura 24/03/2017
# factorial
# source of information https://www.youtube.com/watch?v=D6qpjk48U6U

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
print(factorial3(10))
# in this statement we call the function and assign a value to (num)
    
