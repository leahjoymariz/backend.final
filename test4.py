

def print_total():
    print("your total is: 123")


def can_drink(age):
    if age < 21:
        print("You can't drink")
    else:
        print("You may drink")



def users():
    people = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35},
        {'name': 'Dave', 'age': 40},
        {'name': 'Emily', 'age': 45},
    ]

    # 1 print every dict form the list
    for user in people:
        print(user)
    
    print("2 - only names")
    for user in people:
        print(user["name"])

    
    print("3 - users over 30")
    #name - age
    for user in people:
        if  user["age"] > 30:
            print(user["name"] + " - " + str (user["age"]) )

    
    print("4 - total ages")
    # print the sum of all ages
    total = 0
    for user in people:
        total += user["age"]

    print(f"Total is: {total}")


    
    print("5 - find by name")
    name = input("Type the user name:")
    # find the user with that name and print: name => age
    # otherwise print "User not found"

    found = False
    for user in people:
        if user["name"].lower() == name.lower():
            found = True
            print(f"{user['name']} => {user['age']}")

    if not found:
        print("Error: User not found")
    



    # travel the list with a for
    # if the user name is equal to name
    #   print the result






print_total()
can_drink(19)
can_drink(24)
users()