#Lucia Saura 24/03/2018
#functions
s=0
#s is the variable for the sum

for x in range (12,17):
    #the for loop, loops in all numbers from 12 to 17 to find the sum of the numbers from 12 to 16 (does not include 17)
    s=s+x
    # s=s+x gets a new value for sum in each loop and it sums as well the next number in the range
print(s)
# prints the final value of the sum until the loops stops in 16 (wich is the sum of 12, 13, 14, 15 and 16)


# Lucia Saura 24/03/2018
# function. The function gets the greatest common divisor for the values x and y

def maxcomdivisor (x, y):
    while x != y:
        #the while loop, loops until x = y
        if x > y:
            #the if statement makes the following comand if x is a number greater than y
            x= x-y
        else:
            #when the x gets lower than y the else statement applies
            y=y-x
    return x
    #the return makes the function to return x (could be x or y)

print (maxcomdivisor (1250,3520))
#the print calls the function (by its name) and gets the Greatest common divisor of the two numbers that follow. They will be x and y
