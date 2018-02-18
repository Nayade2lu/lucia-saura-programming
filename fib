# Lucia Saura
# A program that displays the Fibonacci number of the sum of the first letter of my name and the last one
#Comment week 1 fibonacci
# My name is Lucia, so the first and last letter of my name (L + A = 12 + 1) give the number 13. 
# The 13th Fibonacci number is 233

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 13
ans = fib(x)
print("Fibonacci number", x, "is", ans)




# Lucia Saura
# A program that displays Fibonacci numbers using people's names.
# Comment week 2 
# My surname is Saura
# The first letter S is number 83
# The last letter a is number 97
# Fibonacci number 180 is 18547707689471986212190138521399707760
# The (ord) returns an integer representing the Unicode code point of the character 'S' and of the character 'a'
# Then both numbers are summed and the last part shows the Fibonacci number for the previous result (in my case 180).


def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Saura"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
