# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

# Get users name: 
name = input('What is your name? ')
# Get users age: 
age = input('How old are you? ')
# Number of times message will repeat
num = int(input('Enter a number between 1 - 25: '))
# Get year of birth 
dob = 2019 - int(age) 
# Year of birth + 100 = Year user turns 100
year_user_turns_100 = dob + 100

message = name + ' you will turn 100 in ' + str(year_user_turns_100) + "\n"

while num > 0: 
  print(message)
  num = num - 1
