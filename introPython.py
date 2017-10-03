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
print("Hello, %s!" % name) # This prints out “Hello, Bob”

age = 23
print("%s is %d years old." % (name, age)) # This prints out "Bob is 23 years old"

# This prints out: A list: [2, 4, 6] — the list is now a string
thislist = [2, 4, 6]
print("A list: %s" % thislist)

## Basic argument specifiers
#  %s - String (or any object w/ a string representation, like a number
#  %d - Integers
#  %f - Floating point numbers
#  %.<number of digits>f - Floating point numbers w/ fixed amt of decimal places
#  %x / %X - Integers in hex representation (lowercase / uppercase)

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
