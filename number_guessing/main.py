#import modules
from random import randint
#take lower and upper range from user
print("Number Guessing Game")
print("\tPlease enter a the maximum value and minimum value")

upper_number = int(input("Please enter maximum value: "))
lower_number = int(input("Please enter minimum value: "))

#generate a random number from selected range
selected = randint(upper_number, lower_number)

print(selected)


