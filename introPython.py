## Clarify the different styles for defining the source code encoding at the top of a Python source file:
# This Python file uses the following encoding: utf-8
import os, sys

## Declaring variables (variables are objects & you don't have to declare type)
mynumber = 6
myfloat = 7.5
name = "Bob"
greeting = "Hello World"

print("Hello " + name)  #prints "Hello Bob"

## Simple operators (can operate on both numbers and strings)
print (mynumber * myfloat)
print (3 ** 4)  # is 3 to the 4th power, ** = exponent
print (greeting * 3)  #prints 'Hello World' three times

## Datetime Library
from datetime import datetime   #imports datetime library
now = datetime.now()
print now
print now.year
print now.month
print now.day
print '%s / %s / %s' % (now.month, now.day, now.year)
print '%s : %s : %s' % (now.hour, now.minute, now.second)

## Lists - are like arrays
# Building a List
mylist = [ ]
mylist.append(1)
mylist.append(2)
mylist.append(3)    #mylist = [1, 2, 3]
print(mylist[0])    #prints 1

# Iterating over a List
#prints out 1, 2, 3
for x in mylist:
    print(x)

# The % operator & argument specifiers
print("Hello, %s!" % name)

age = 23
print("%s is %d years old." % (name, age)) # This prints out "Bob is 23 years old"

# This prints out: A list: [2, 4, 6] — the list is now a string
thislist = [2, 4, 6]
print("A list: %s" % thislist)

## Basic argument specifiers
"""
%s - String (or any object w/ a string representation, like a number
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers w/ fixed amt of decimal places
%x / %X - Integers in hex representation (lowercase / uppercase
"""

## Manipulating strings
mystring = "What a wonderful world"
len(mystring) #length of the string, including spaces & punctuation
mystring.index('e') #index of first occurence of 'e' (zero-indexed!!)
mystring.count('a') #number of times 'a' occurs in the string
mystring[6:16] #slice returns ' wonderful' (index 6 thru 15)
mystring[::-1] #reverses the string
mystring.upper() #returns string in uppercase
mystring.lower() #returns string in lowercase
mystring.startswith("wonder") #will print true if the string starts w/ 'wonder'
mystring.endswith("asdffgh")  #will print true if the string ends w/ 'asdffgh'
mystring.split(" ") #splits the string at ' ' and places each piece in a list

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

## Functions
# Declaring and calling a function
	def tax(bill):
  	  """Adds 8% tax to a restaurant bill."""
	  bill *= 1.08
	  print "With tax: %f" % bill
	  return bill
	def tip(bill):
	  """Adds 15% tip to a restaurant bill."""
	  bill *= 1.15
	  print "With tip: %f" % bill
	  return bill
	meal_cost = 100
	meal_with_tax = tax(meal_cost)
	meal_with_tip = tip(meal_with_tax)

## Importing a module
# generic import
import math #imports math module
print math.sqrt(25)  #uses sqrt function inside math module

# function import
""" from math import sqrt """

# universal import (don't need module.function to call function)
# Careful here: you import lots of variables and lose connect to which modele they came from
""" from math import * """

## Built in Functions
# Find min / max values
print min(23, 35, 12, 45)  #would return 12
print max(23, 35, 12, 45)  #would return 45

# Find absolute value
print abs(-36)  #world return 36

# Find type of data
print type(67)  #would return <type 'int'>
print type(9.8)  #would return <type 'float'>
print type("taco")  #would return <type 'str'>
