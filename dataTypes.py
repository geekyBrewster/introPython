## Clarify the different styles for defining the source code encoding at the top of a Python source file:
# This Python file uses the following encoding: utf-8
import os, sys

## Declaring variables (variables are objects & you don't have to declare type)
mynumber = 6
myfloat = 7.5
name = "Bob"
greeting = "Hello World"

# Note: Python 2 does "classic" division
3 / 2   # In Python 2, this would equal 1, where Python 3 gives you 1.5

# To cast data type in Python 2 to get the decimal answer:
float(3) / 2

print("Hello " + name)  #prints "Hello Bob"

## Simple operators (can operate on both numbers and strings)
print (mynumber * myfloat)
print (3 ** 4)  # is 3 to the 4th power, ** = exponent (or root)
print (4 ** 0.5)  # is the square root of 4
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
#------------------------------

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

# Grab everything, but go in steps size of 1
mystring[::1]
# Grab everything, but go in steps size of 2
mystring[::2]

#Immutablity - you cannot change a character in the string after you make it
# Error: mystring[0] = "Z" -- produces TypeError

#Concatenation
mystring + ' isn\'t it?'
#You can also reassign the string mystring = "Holy Cow!"



# --------------------------------------
## The % operator & argument specifiers
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

# --------------------------------------
