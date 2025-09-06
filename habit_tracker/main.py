habits = []

no_habits = int(input("How many habits do you want to enter today? "))

# for loop to take each input one by one and append to the list 
# using range
for h in range(no_habits):
    # after entering habit, allow user to add another one
    user_habit = input(f"Enter habit: {h + 1}")
    habits.append(user_habit)

