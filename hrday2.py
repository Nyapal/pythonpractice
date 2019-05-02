import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
  tip = round(meal_cost * (tip_percent/100), 2)
  tax = round(meal_cost * (tax_percent/100), 2)
  
  total_cost = meal_cost + tip + tax 
  checking = str(total_cost)
  #11.71

  if (int(checking[3]) >= 5):
    print(math.ceil(total_cost))
  else: 
    print(round(total_cost))

print(solve(12.00, 20, 8))
print(solve(10.25,17, 5))