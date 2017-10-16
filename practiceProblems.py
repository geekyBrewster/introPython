# Check to see if a number is even
def is_even(x):
  if x%2 == 0:
    return True
  else:
    return False

# Check to see if a number is an interger, including 7.0 as an integer
def is_int(x):
  if x > 0:
    if x - round(x) > 0:
    	return False
    else:
      return True
  else:
    if x - round(x) < 0:
    	return False
    else:
      return True

# Sum the digits of a number, where n is a positive integer
def digit_sum(n):
  num_str = str(n)
  total = 0
  for i in range(0, len(num_str)):
    total = total + int(num_str[i])
  return total

# Calculate the Factorial of X
def factorial(x):
  total = 1
  while x > 0:
    total = total * x
    x -= 1
  return total

# Check to see if a number is Prime
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

# Print a string in reverse without using 'reversed' or [::-1]
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

# Remove all the vowels from a string
