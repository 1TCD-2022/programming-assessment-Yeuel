"""
Filename: Theme_Park_V2.py
Author: Yeuel Cunanan
Date: 28/06/2022
Description:The user will enter their height and when they do that they will know how many rides
they can go on
"""
import time
import random
import math

one_sixty_cm = ["Roller Coaster", "Pendulum Ride", "Drop Tower"]
one_fifty_cm = ["Family Carts", "Scorpion Karts", "Stratosfear"]
one_thirty_cm = ["Dodgems", "Power surge", "Alpine Slide"]
kids_rides = ["Carousel","Car Wash Convoy","The Fortress of Fun"]


def wait(mins): #function for the amount of time user has to wait
        for x in range(mins * 60 , 0, -1):
                print('{}minutes(s) {}s'.format(math.floor(x / 60), x % 60))
                time.sleep(0.001)


another_one = False

while not another_one:

        print("[1] Enter The amusment park")
        print("[2] Leave")

        enter_amusment_park = False

        while not enter_amusment_park:
                try:
                        entry = int(input())
                        if entry > 0 and entry < 3:
                            enter_amusment_park = True
                        else:
                            print("Invalid")
                            print("Try again")
                except ValueError:
                        print("Invalid")
                        print("Try again")

        if entry == 1:
                print("Welcome to our amusment park!")
                print("Please wait in line for your turn")
                print()
                if random.randint(1, 10) == 1:
                        print("Oh my goodness you have skipped the line!")
                else:
                        time_to_wait = random.randint(1, 5)
                        wait(time_to_wait)

                        
                party_validation = False

                while not party_validation:
                    try:
                        party_size = int(input("How many people are in your party?"))
                        if party_size > 0:
                            party_validation = True
                        else:
                            print("Invalid")
                    except ValueError:


                        print("Invalid")

                is_child = False

                while not is_child:
                    try:
                        kids_amount = int(input("How many kids are with you?"))
                        if kids_amount > party_size or kids_amount < 0:
                            print("Invalid")
                            
                        else:

                            is_child = True

                    except ValueError:
                        print("Invalid")

                     
                party_size = party_size - kids_amount

                        
                for index in range(party_size):
                    
                    is_valid_height = False

                    while not is_valid_height:
                        try:
                            height = int(input("How tall is adult {} in cm".format(index + 1)))
                            print()
                            if height > 0:
                                is_valid_height = True    

                            elif is_valid_height:
                                print("Invalid")
                                
                        except ValueError:
                            print("Invalid")


                        
                    temp = ''
                    if height >= 160: #checking if height is more or equal to 160
                        print("The rides person {} can go on are:".format(index + 1))
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
                        print("The rides person {} can go on are:".format(index + 1))
                        print()
                        for word in one_fifty_cm:
                            print(word)
                        print()
                        
                        for word in one_thirty_cm:
                            print(word)
                        print()

                    elif height < 150 and height >= 130: #checking that the height is less than 150 and more or equal to 130
                        print()
                        print("The rides person {} can go on are:".format(index + 1))
                        for word in one_thirty_cm:
                            print(word)
                        print()

                    else:
                        print("Sorry person {} is to short to go on any rides".format(index + 1))
                if kids_amount != 0:                    
                        child_validation = False

                        while not child_validation:
                                
                                is_child_riding = input("Is your kid/s going on any rides today? (yes or no)")

                                if is_child_riding.lower() == "yes" or is_child_riding.lower() == "y":
                                        print("here are the rides your kid/s can go on")
                                        print()
                                        for word in kids_rides:
                                                print(word)
                                                print()
                                        child_validation = True
                                        
                                elif is_child_riding.lower() == "no" or is_child_riding.lower() == "n":
                                        print("Thats fine")
                                        child_validation = True

                        else:
                                print("Invalid")
                
                else:
                             print("Thank you for using this program :D")

                validation = False
                
                while not validation:
                        again = input("Wanna go again?")

                        if again.lower() == "yes" or again.lower() == "y":
                                another_one =  False
                                validation = True
                        elif again.lower() == "no" or again.lower() == "n":
                                another_one = True
                                validation = True
                        else:
                                print("Invalid")

        else:
                another_one = True
print("Ok bye now")


























