# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = input('Enter a number: ')
check = input('Enter a second number: ')

# num = 15, check = 5 ... if 15 % 5 == 0, it divides evenly 
# num = 8, check = 3... if 8 % 3 == 0, it doesn't divide evenly

if (int(num) % int(check) == 0):
  print('check divides evenly into num')
else: 
  print('check does not evenly divide into num')

# if (int(num) % 4 == 0):
#   print('num is divisible by 4')
# elif (int(num) % 2 == 0):
#   print('num is even')
# else: 
#   print('num is odd')