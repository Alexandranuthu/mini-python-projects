grocery_list = []

while True:
    print("Welcome to your list\n\tEnter the items you want to add! [Type 0 when done]")
    grocery = input()

    if grocery == '0':
        break
    grocery_list.append(grocery.title())

for item in grocery_list:
        print(f"{item}")
    




    


