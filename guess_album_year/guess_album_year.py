import random


albums = ['is this it',  'bizarre ride II the pharcyde', 'the anthology','Madvillainy','To Pimp a Butterfly','Blonde','Channel Orange','Yeezus']
release_year = [2001, 1992, 2001, 2004, 2015, 2016, 2012, 2013]

music = {
    
}

r_albums = random.choice(albums)
start_game = input('Do you want to start the game(type yes or 0 to enter)?')
# while start_game == 'yes' or start_game == 0:
while True: 
    if start_game == 'yes' or start_game == 0:
        f_question = print(f"First album you have to guess {r_albums}")
        ans = input("When year do you think it came out? ")
        