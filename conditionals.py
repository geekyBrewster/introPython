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

#For loops
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

#While loops

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

# Using an Else in a loop
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
