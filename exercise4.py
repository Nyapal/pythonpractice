# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


user_num = int(input('Enter a number: '))

og_list = range(2, user_num)
divisors_list = []

for elem in og_list:
  if (user_num % elem == 0):
    divisors_list.append(elem)

# i = 2
# while i < user_num: 
#   if(user_num % i == 0):
#     divisors_list.append(i)
#   i += 1

print(divisors_list)
