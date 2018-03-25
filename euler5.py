#Lucia Saura 25/03/2018
# euler 5 
# source https://www.youtube.com/watch?v=EMTcsNMFS_g

def euler5 (ni): #first create a function
    for i in range (11,21): #loop trough the numbers from 11 to 21 (if it is divisible by 11 to 20 is also from 1 to 10)
        if ni % i ==0: #if the number is divisible by the number in the range 11 to 21 (remainder0)
            continue #the loops continues
        else: #if it is not divisible 
            return False #the program gives false (boolean)
    return True #the program gives true (boolean)

x= 2520 #the problem gives us the minimum common multiple of the range 1 to 10 and here it is used to increase the number just on multiples of it
while not euler5(x): #here the while loop keeps looping provided that the number is not 2520)
    x +=2520 #and actualises the number only in multiples of 2510 what makes the program very efficient
print (x) #this command prints the result of the problem

#for now this is the only way I have been able to make the program work in my code
#it is very efficient. (advanced knowledge on true and false required) 

