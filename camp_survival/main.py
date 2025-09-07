import random

print("\n--------------- Welcome to Camp Survival ---------------")

# dic to store the initial resources
camp = {
    'day': 1,
    'food': 20,
    'survivors': 25,
    'health': 95
}

def showStatus():
    print(f"\nYou are on day {camp['day']}")
    print(f"So far you are left with \n\t Food: {camp['food']} \n\t Health: {camp['health']} \n\t Survivors: {camp['survivors']}")


def gatherfood():
    print("You have decided to gather food. You need to choose the number of survivors you want to go gather food")
    no_survivors = int(input("How many? "))
    # randomly choosing the number of food brought back
    food_found = random.choice(range(0,15))
    camp['food'] = camp['food'] + food_found
    # each time they gather food they lose health
    camp['health'] -= 10

    print(f"The {no_survivors} survivors brought back {food_found} food.\nYou now have {camp['food']}")
    print(f"You are also left with {camp['health']} ")



