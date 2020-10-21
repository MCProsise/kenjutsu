import sys
import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

size = 501 # Assigns the number 5 to variable "size"

def print_square(square): # defines the function "print_square" with the required parameter "square"
    print("-"*(2*5)) # prints 10 hyphens
    for y in range(len(square)): # for every element in the range of the length of "square"
       for x in range(len(square[y])): # for every element in the current element in the range of the length of "square"
           print("{:6}".format(square[x][y]), end="") #
       print() # prints a space
    print("-"*(2*5)) # prints 10 hyphens


square = [[f"{x}.{y} " for x in range(size)] for y in range(size)] 
# "Square" is formatted to print that for every number in "size", assign to "x". Before moving to the next number, print every number in "size" as "y"
#  in order up to, but not including 501. Completing the same action for each number in "size".

print_square(square) # Calls the function