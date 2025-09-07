print("\n--------------- Welcome to Camp Survival ---------------")

camp = {
    'day': 1,
    'food': 20,
    'survivors': 25,
    'health': 95
}

def showStatus():
    print(f"\nYou are on day {camp['day']}")
    print(f"So far you are left with \n\t Food: {camp['food']} \n\t Health: {camp['health']} \n\t Survivors: {camp['survivors']}")
