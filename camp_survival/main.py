import random

print("\n--------------- Welcome to Camp Survival ---------------")

# dic to store the initial resources
camp = {
    'day': 1,
    'food': 40,
    'survivors': 25,
    'health': 95
}

won = False



def showStatus():
    print(f"\nYou are on day {camp['day']}")
    print(f"So far you are left with \n\t Food: {camp['food']} \n\t Health: {camp['health']} \n\t Survivors: {camp['survivors']}")


def gatherfood():
    print("You have decided to gather food. You need to choose the number of survivors you want to go gather food")
    no_survivors = int(input("How many? "))
    # randomly choosing the number of food brought back, the more people sent the more food returned
    food_found = sum(random.randint(0,5) for _ in range(no_survivors))
    camp['food'] = camp['food'] + food_found
    # each time they gather food they lose health
    camp['health'] = max(0, camp['health'] - 10)

    print(f"The {no_survivors} survivors brought back {food_found} food.\nYou now have {camp['food']}")
    print(f"Your health got depleted though. Rem: {camp['health']} ")

def rest():
    print("You have decided to rest.")
    # this adds 5 to the health key value once they've rested and making sure health doesn't go past 100
    camp['health'] = min(100, camp['health'] + 5)
    print(f"Camp's health is now at {camp['health']}")

def feedsurvivors():
    print(f"You need to feed the people.You have {camp['food']} in store")
    # check if food is more than the survivors,if not else block runs
    if camp['food'] >= camp['survivors']:
        # each person can get 1 food remainder is assigned back to the food store
        divide_food = camp['food'] - camp['survivors']
        camp['food'] = divide_food
        # this adds 15 to the health key value once they've eaten
        camp['health'] = min(100, camp['health'] + 15)
        print(f"Camp has eaten. Health has been added: {camp['health']}.")
    elif camp['food'] < camp['survivors']:
        rations = camp['food'] / camp['survivors']
        print(f"Only {camp['food']} food for {camp['survivors']} survivors  ")
        print(f"Each person gets at least {rations:.2f} food.")
        # re initialize to 0
        camp['food'] = 0
        camp['health'] = max(0, camp['health'] - 15)
        print(f"Camp was underfed. Health dropped to {camp['health']}.")

# main menu for the options
def menu():
    print(f"\t1. Gather food \n\t2. Rest")

def gameover():
    if not won and (camp['health'] <= 0 or camp['food'] <= 0 or camp['survivors'] <= 0):
        print("Damn, Your camp did not survive! Game over.")
    
# main loop - as long the health key value is more than 0
while camp['health'] > 0 and camp['food'] > 0 and camp['survivors'] > 0:
    print("\n--------------- Camp Survival - Day", camp['day'], "---------------")
                            
    showStatus()
    print("This is what you can do:")
    menu()
    user_choice = input("Your choice? ")

    if user_choice == "1":
        gatherfood()
    elif user_choice == "2":
        rest()

    if camp['health'] < 40:
        camp['survivors'] = max(0, camp['survivors'] - 2)
        print("Health is less than 40. You just killed 2 survivors")
    

    if camp['survivors'] <= 0:
        print("You just killed everyone. Damn!")
        break
    
    feedsurvivors()
    camp['day'] += 1

    if camp['day'] >= 15:
        won = True
        print("You just survived more than 15 days. You win the game!!")
        break
    
gameover()



