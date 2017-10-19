# To open a file: fileObject = open("output.txt", “w")
# “r+” — read and write, “w” — write-only, “r” — read only, “a” — append mode, which adds new data to the end of the file
# To write to a file, use f.write()
# To close the file, use f.close() - Be sure to include this, or Python won’t write to the file properly

## Example of write to file:
my_list = [i ** 2 for i in range(1, 11)]
my_file = open("output.txt", "w")
for item in my_list:
  my_file.write(str(item) + "\n")
my_file.close()

# To read from a file, use .read( ) & still include .close()
my_file = open("output.txt", "r")
print my_file.read( )
my_file.close( )

# To read a file one line at a time, use .readline()
# Each tiem you call the command, it grabs the next line in the file
my_file = open("text.txt", "r")

print my_file.readline()  #returns first line
print my_file.readline()  #returns second line
print my_file.readline()  #returns third line

my_file.close()

# Using “with” and “as” keywords to evoke built-in methods: _ _enter_ _( ) and _ _exit_ _( )
# __exit__( ) it automatically closes the file object

# Format: with open("file", "mode") as variable:
with open("text.txt", "w") as textfile:
  textfile.write("Success!")


# Testing to see if a file is closed with .closed attribute, which is True when file is closed
with open("text.txt", "w") as my_file:
  my_file.write("Invaders must die!")
if my_file.closed != False:
  my_file.close( )
