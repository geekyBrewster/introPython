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
def anti_vowel(text):
  word = ""
  for i in range(0,len(text)):
    if text[i] in "aeiouAEIOU":
      word = word
    else:
      word = word + text[i]
  return word

# Compute Scrabble score using provided score list
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
def scrabble_score(word):
  word = word.lower()
  total = 0
  for letter in word:
    for key in score:
      if letter == key:
        total = total + score[key]
  return total

# Replace a given word in a string with *****
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result

# Count how many times an item appears in a list
def count(sequence, item):
    counter = 0
    for i in sequence:
        if i == item:
            counter += 1
    return counter

# Remove the odd numbers from a list of numbers
def purify(numList):
    newList = []
    for ele in numList:
        if ele % 2 == 0:
            newList.append(ele)
    return newList

# Multiply all the intergers in a number together
def product(numlist):
  result = 1
  for i in range(0, len(numlist)):
    result = result * numlist[i]
  return result

# Remove duplicates from a list of numbers
def remove_duplicates(inputlist):
    if inputlist == []:
        return []
    # Sort the input list from low to high
    inputlist = sorted(inputlist)
    # Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

    # Go through the values of the sorted list and append to the output list any unique values
    for i in inputlist:
        if i not in outputlist:
            outputlist.append(i)
    return outputlist

# Find the median value of a list of numbers
def median(inputlist):
    sorted_list = sorted(inputlist)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean

print median([2, 4, 5, 9])
