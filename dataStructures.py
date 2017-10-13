## Clarify the different styles for defining the source code encoding at the top of a Python source file:
# This Python file uses the following encoding: utf-8
import os, sys

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

# Find the length of a list
len(mylist) #returns the length of the list

# Slicing a list (or a string)
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]  #returns 'sunglasses' & 'hat'

# Third and fourth items (index two and three)
middle = suitcase[2:4]  #returns 'passport' & 'laptop'

animals = "catdogfrog"
# The first three characters of animals
cat = animals[:3]
# The fourth through sixth characters
dog = animals[3:6]
# From the seventh character to the end
frog = animals[6:]

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
# Find the index where "duck" is in the list
duck_index = animals.index("duck")

# Insert "cobra" at that index
animals.insert(duck_index, "cobra")

print animals # Observe what prints after the insert operation

# Sort a list
start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
  square_list.append(number ** 2)

square_list.sort() #sorts numerically ascending (or alphabetically for strings)

print square_list

#To Remove an item from a list
start_list.remove(5)

# --------------------------------------
## Dictonaries -- like lists but w/ key-value pairs, defined by { }
#Example:
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Add some dish-price pairs to menu!
menu['Pizza'] = 11.25
menu['Meatballs'] = 9.95
menu['Spaghetti'] = 12.75

print "There are " + str(len(menu)) + " items on the menu."
print menu

# To delete a key-value pair
del menu['Pizza']

# Using a For loop to step through a dictionary
for key in dict :
    print dict[key]

#Example of dictionary w/ multiple types of data:
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', ‘gemstone'],
    # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
# Sorting the list found under the key 'pouch'
inventory[‘pouch'].sort()
# Add new item to inventory
inventory['pocket'] = ["seashell", "strange berry", “lint"]
# Sort the items in ‘backpack’
inventory[‘backpack'].sort()
inventory[‘backpack'].remove('dagger')
# Add 50 gold to the gold already in the inventory
inventory['gold'] = inventory['gold'] + 50
