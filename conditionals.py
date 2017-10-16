## Clarify the different styles for defining the source code encoding at the top of a Python source file:
# This Python file uses the following encoding: utf-8
import os, sys

## Conditionals
# Comparison (==), Not equal (!=)

# IF statement (If, Else If (elif), Else)
if name == "Bob" and age == 23 :
    print("Bob is 23")
if name == "Bob" or name == "Rick" :
    print("Your name is either John or Rick")

# 'In' operator
if name in ["John", "Rick", "Mary"]:
    print("Your name is either John, Rick or Mary")

# 'Is' operator
#Unlike ==, does not match the values of the variables but the instances of themselves
x = [1, 2, 3]
y = [1, 2, 3]
print( x == y)    #prints out True
print( x is y )    #prints out False

# 'Not' operator -- flips meaning of boolean

# --------------------------------------
## Loops

# FOR loops
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

# Ask user for a hobby and appends input to a list
hobbies = []
for x in range(3):
  hobby = raw_input("Enter a hobby: ")
  hobbies.append(hobby)
print hobbies

# Print out the characters in the phrase (, after print keeps all the chars on the same line)
phrase = "A bird in the hand..."
for char in phrase:
	if char == "A" or char == "a":
		print "X",
	else:
		print char,
print

# Using a For loop to loop over a dictionary
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in d:
  print key + " " + d[key]

# Built-in Function: Enumerate - supplies a corresponding index to each element in the list that you pass it
choices = ['pizza', 'pasta', 'salad', 'nachos']
print 'Your choices are:'
for index, item in enumerate(choices):
  print index+1, item

# Using two (or three) lists w/ ZIP
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
    if a > b:
        print a
    else:
        print b

# FOR-ELSE loop
# The Else will NOT execute if you use a break statement
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
    break
  print 'A', f
else:
  print 'A fine selection of fruits!'


# WHILE loops

# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# Break & Continue
# Break exits a loop; Continue skips the current block

# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# Using an While-Else in a loop
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"
