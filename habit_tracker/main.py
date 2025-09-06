habits = []

no_habits = int(input("How many habits do you want to enter today? "))

# for loop to take each input one by one and append to the list 
# using range
for h in range(no_habits):
    # after entering habit, allow user to add another one
    user_habit = input(f"Enter habit: {h + 1}")
    habits.append(user_habit)

# ask user if they've done it
print("What habits have you done today?")

# using a dictionary to store key value pairs i.e habit : done or not
status = {}

for n in habits:
    question = input(f"Have you done {n}? (Y/N) ").lower()
    # for each habit store whether it has been done or not
    status[n] = question == 'y'

# initialise the amount of tasks done
completed_tasks = 0

# returning a new view of the dictionary(status)
for n, question in status.items():
    if question == True:
        print(f"Done: {n}")
        completed_tasks = completed_tasks + 1
    elif question == False:
        print(f"Not: {n}")
    else:
        print("Input does not make sense")
    
print(f"You have completed {completed_tasks} out of {no_habits} today. Good Job")


