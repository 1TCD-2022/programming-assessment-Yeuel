
"""
Filename: Theme_Park_V1.py
Author: Yeuel Cunanan
Date: 28/06/2022
Description:The user will enter their height and when they do that they will know how many rides
they can go on
"""


one_sixty_cm = ["Roller Coaster", "Pendulum Ride", "Drop Tower"]
one_fifty_cm = ["Family Carts", "Scorpion Karts", "Stratosfear"]
one_thirty_cm = ["Dodgems", "Power surge", "Alpine Slide"]

is_valid_1 = False

while not is_valid_1:
    try:
        party_size = int(input("How many people are in your party?"))
        if party_size > 0:
            is_valid_1 = True
        else:
            print("Invalid")
    except ValueError:

        print("Invalid")
        
for index in range(party_size):
    
    is_valid_2 = False

    while not is_valid_2:
        try:
            height = int(input("How tall are you in cm?"))
            if height > 0:
                is_valid_2 = True

            else:
                print("Invalid")
        except ValueError:
            print("Invalid")
                  
        
    temp = ''
    if height >= 160: #checking if height is more or equal to 160
        print("The rides you can go on are:")
        print()
        for word in one_sixty_cm: #For loop to print out each word in the list
            print(word)
        print()
        for word in one_fifty_cm:#For loop to print out each word in the list
            print(word)
        print()
        for word in one_thirty_cm:#For loop to print out each word in the list
            print(word)
        print()
        
    elif height < 160 and height >= 150: #checking that the height is less than 160 and more or equal to 150
        print("The rides you can go on are:")
        print()
        for word in one_fifty_cm:
            print(word)
        print()
        
        for word in one_thirty_cm:
            print(word)
        print()

    elif height < 150 and height >= 130: #checking that the height is less than 150 and more or equal to 130
        print()
        print("The rides you can go on are:")
        for word in one_thirty_cm:
            print(word)
        print()

    else:
        print("Sorry you're to short to go on any rides")
