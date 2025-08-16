import random


music = {
    'is this it': 2001,
    'bizarre ride II the pharcyde': 1992,
    'the anthology': 2001,
    'Madvillainy': 2004,
    'To Pimp a Butterfly': 2015,
    'Blonde': 2016,
    'Channel Orange': 2012,
    'Yeezus': 2013

}

album, year = random.choice(list(music.items()))
guesses = 3


# r_albums = random.choices(list(music.values()))

start_game = input('Do you want to start the game(type yes or 0 to enter)? ')
while True: 
    if start_game != "no":
        f_question = print(f"First album you have to guess is: {album}")
        ans = int(input("What year do you think it came out? "))

    if ans == year:
        print("That is correct!")
    elif ans != year:
        guesses = guesses - 1
        print("Damn that was wrong")
        print(f"You have {guesses} more guesses")

    if guesses <= 0:
            print("You have run out of guesses")
            break


        