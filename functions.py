## Clarify the different styles for defining the source code encoding at the top of a Python source file:
# This Python file uses the following encoding: utf-8
import os, sys
# --------------------------------------
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

# --------------------------------------
## Importing a module
# generic import
import math #imports math module
print math.sqrt(25)  #uses sqrt function inside math module

# function import
""" from math import sqrt """

# universal import (don't need module.function to call function)
# Careful here: you import lots of variables and lose connect to which modele they came from
""" from math import * """
# --------------------------------------
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

# --------------------------------------
# ANONYMOUS FUNCTIONS USING LAMBDA

# Passing an anonymous function into the filter() function
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

# Filter list using an anonymous function that only prints numbers divisiable by 3
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

# Make a list of squares b/wn 1 and 10, then filter those results between 30 and 70 (inclusive)
squares = [x**2 for x in range(1,11)]
print filter(lambda x: x >= 30 and x <= 70, squares)
