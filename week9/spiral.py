import sys
import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

size = 5 # Assigns the number 5 to variable "size"
square = 10
def print_square(square): # defines the function "print_square" with the required parameter "square"
    print("-"*(2*size)) # prints 10 hyphens
    for y in range(len(square)): # for every element in the range of the length of "square"
       for x in range(len(square[y])): # for every element in the current element in the range of the length of "square"
           print("{:6}".format(square[x][y]), end="")
       print()
    print("-"*(2*size))


square = [[f"{x}.{y}" for x in range(size)] for y in range(size)]

print_square(square)