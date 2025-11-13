#import modules
from random import randint
#take lower and upper range from user
print("Number Guessing Game")
print("\tPlease enter a the maximum value and minimum value")

upper = int(input("Please enter maximum value: "))
lower = int(input("Please enter minimum value: "))

#generate a random number from selected range
selected = randint(upper, lower)

print(selected)

#maximum allowed chances to guess and tracking the amount of guesses
print(f"\n You have 7 chances to guess the number between {upper} and {lower}")

chances = 7
g_counter = 0

#if number of guesses are less than the chances 
while g_counter < chances:
    #increment the counter at each guess
    g_counter += 1
    guess  = int(input("\tPlease enter your guess: "))

    #once the guess is correct stop the game
    if guess == selected:
        print(f"That is correct!You only guessed in {g_counter} tries. Nice :)")
        break

    # if the number of guesses are more than the chances and the user still hasn't guessed correctly end it
    elif g_counter >=  chances and guess != selected:
        print(f"You unfortunately did not guess the number.It was: {selected}")
        print("Better luck next time!")
        print("Play again? ")
    
    elif guess > selected:
        print("That is not correct, Your guess is too high!")
        print("Try a lower number.")
    elif guess < selected:
        print("That is not correct, Your guess is too low.")
        print("Try a higher number.")



   







