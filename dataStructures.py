## Clarify the different styles for defining the source code encoding at the top of a Python source file:
# This Python file uses the following encoding: utf-8
import os, sys

## LISTS - are like arrays
# Building a List
mylist = [ ]
mylist.append(1)
mylist.append(2)
mylist.append(3)    #mylist = [1, 2, 3]
print(mylist[0])    #prints 1

# Iterating over a List
# Method 1: uses items to step through the list
# Cannot modify items in the list
for item in mylist:
    print(item)

# Method 2: uses index to step through the list so you can modify elments in list
for i in range(len(mylist)):
    print(mylist(i))

#Iterating across a list of lists
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results

print flatten(n)

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

#To Remove an item from a list using item's name
start_list.remove(5)

#To Pop an item from a list using its index & return the item
start_list.pop(1)

#To Delete an item and not return the value
del(start_list(2))

#LIST COMPREHENSION - Building lists according to logic
# Remember, in the range, the last end number is non-inclusive!!
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

even_squares = [x ** 2 for x in range(2, 11) if (x ** 2) % 2 == 0]

print even_squares

# --------------------------------------
## DICTIONARIES -- like lists but w/ key-value pairs, defined by { }
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
    print key, dict[key]

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
