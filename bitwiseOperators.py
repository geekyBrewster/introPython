# Binary numbers in Python
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print 0b1000   #8
print 0b1001   #9
print 0b1010   #10
print 0b1011   #11
print 0b1100   #12
print "******"
print 0b1 + 0b11  #prints 4
print 0b11 * 0b11    #prints 9

# To print out the binary form of an int
print bin(12)

# To print out the base 8 form of an int
print oct(15)

# To print out the base 16 form of an int
print hex(16)

# To print out the int version of a string, use second option for int
print int( ‘110’, 2 )  #prints 6
print int("11001001", 2)   #prints 201

# Bitwise Shift
# Left Bit Shift (<<)
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)
# Right Bit Shift (>>)
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 (2 >> 2 = 0)

# Bitwise AND (&) - compares two numbers, returns a 1 only where both numbers have 1
print bin(0b1110 & 0b101) #prints out 0b100

# Bitwise OR ( | ) - compares two numbers, returns a 1 where either numbers are 1
print bin(0b1110 | 0b101)  #prints out 0b1111

# Bitwise Exclusive OR ( ^ ) - compares two numbers, returns 1 where either number is 1
# BUT NOT where both numbers are 1
print bin(0b1110 ^ 0b101)  #returns 0b1011

# Bitwise NOT ( ~ ) - flips the bits: adds 1 to the number and makes it negative
print ~1  #prints -2
print ~2
print ~3
print ~42
print ~123

# Bit Mask
# Use to check if a bit is on, turn bits off, collect data from an int abt which bits are on

# Check to see if the 4th bit is on using AND
def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired > 0:
    return "on"
  else:
    return "off"

print check_bit4(0b1011)  #would print "on"
print check_bit4(0b10011)   #would print "off"

#Turns the third bit on using OR
a = 0b10111011
mask = 0b111
desired = a | mask
print bin(desired)

# Flipping all the bits using XOR
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print bin(desired)   #prints out 0b00010001

# Flipping a bit using shift to move bit over to desired bit to flip
def flip_bit(number, n):
  mask = (0b1 << n-1)
  result = number ^ mask
  return bin(result)
