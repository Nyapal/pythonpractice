#  write a program that prints out all the elements of the list that are less than 5.


def less_than(lis):
  user_num = input('Enter a number between 1 - 100: ')
  output = []
  for num in lis:
    if num < int(user_num):
      output.append(num)
  return output

a = less_than([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

print(a)