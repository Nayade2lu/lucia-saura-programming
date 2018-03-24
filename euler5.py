# lucia saura 24/03/2018
# first step euler 5
# identifying prime numbers but not fully working because I need a list instead a single value for a (now says that any number not divisible by two is prime)

a=2
num=24
while num > a :
  if num%a==0 & a!=num:
    print('not prime')
    break
    a=a+1
  else:
    print('prime')
    a=(num)+1
