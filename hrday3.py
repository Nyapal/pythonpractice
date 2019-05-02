#!/bin/python3

import math
import os
import random
import re
import sys

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

def weird(input2):
  # if (input2 % 2 != 0):
  #   return('Weird')
  # elif (input2 % 2 == 0 & 2 < input2 < 5):
  #   return('Not Weird')
  # elif (input2 % 2 == 0 & 6 < input2 <= 20):
  #   return('Weird')
  # elif (input2 % 2 == 0 & input2 < 20):
  #   return('Not Weird') 

print(weird(20))

# if __name__ == '__main__':
#     input2 = int(input(24))
#     print(No(input2))
