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


def val_loop(message): #function for most of my validation loops 
    validation = False
    while not validation:
                    try:
                        valid_input = int(input(message))
                        if valid_input > 0:
                            validation = True
                        else:
                            
                            print("Invalid")
                    except ValueError:
                        print("Invalid")
    return valid_input



another_one = False

while not another_one:

    print("[1] Enter The amusment park")
    print("[2] Leave")
    print("Please enter 1 or 2")
    
    enter_amusment_park = False
    entry = 3
    while not enter_amusment_park:
            try:
                    entry = int(input()) #checking if the user entered a valid number
                    if entry > 0 and entry < 3:
                        enter_amusment_park = True
                    else:
                        print("Invalid")
                        print("Try again")
            except ValueError:
                    print("Invalid")
                    print("Try again")

            if entry == 1:

                has_membership = False 
                normal_pass = False
                gold_pass = False
                platinum_pass = False
                
                while not has_membership: #different membership changes the experience of the user
                    print("What pass do you have\n1,2,3?")
                    print()
                    try: #checking for valid answer
                        membership = int(input("[1] Normal Pass\n[2] Gold Pass\n[3] Platinum Pass"))
                        if membership > 0 and membership < 4:
                            print("great!")
                            has_membership = True
                            
                            if membership == 1:
                                normal_pass = True
                                
                            elif membership == 2:
                                gold_pass = True

                            elif membership == 3:
                                platinum_pass = True
                        else:
                            print("invalid")
                    except ValueError:
                        print("Invalid")
                
                print("Welcome to our amusment park!")
                print("Please wait in line for your turn")
                print()
                if platinum_pass == True: #if you have a platinum pass you have a 20% chance to skip the line
                    if random.randint(1,5) == 1:
                        print("Oh my goodness you have skipped the line!")
                    else:
                        time_to_wait = random.randint(1, 1)
                        wait(time_to_wait)
                        
                elif gold_pass == True: #if you have a gold pass you skip the line with a 10% chance
                    if random.randint(1,10) == 1: 
                        print("Oh my goodness you have skipped the line!")
                    else:
                        time_to_wait = random.randint(1, 3)
                        wait(time_to_wait)
                        
                elif normal_pass == True: #if you have a normal pass you skip the line with a 2% chance
                    if random.randint(1,50) == 1:
                        print("Oh my goodness you have skipped the line!")
                    else:
                        time_to_wait = random.randint(1, 5)
                        wait(time_to_wait)

                                                  
                adult_limit = False
                while not adult_limit: #validating input for the party size
                    adult_amount = val_loop("How many people are in your party")
                    if adult_amount > 15:#party limit so people dont enter to much people
                        print("Sorry we have a limit of 15 people per party")
                    else:
                        adult_limit = True
                        
                is_child = False

                while not is_child:
                    try:
                        kids_amount = int(input("How many kids are with you?")) #validating input
                        if kids_amount > adult_amount or kids_amount < 0:
                            print("Invalid")
                            
                        else:
                            is_child = True

                    except ValueError:
                        print("Invalid")

                     
                party_size = adult_amount - kids_amount #to calculate party size

                        
                for index in range(party_size):
                    height_limit = False
                    while not height_limit:
                        adult_height = val_loop("How tall is adult {} in cm".format(index + 1)) #Asking user for the height of each party member
                        if adult_height > 250 or adult_height < 60: #height limit for when number is to low or to high
                            print("no way you're that tall")
                            height_check = input("Are you sure?\nyes or no")
                            if height_check == "yes" or height_check == "y":
                                print("Alright then?")
                                height_limit = True
                            elif height_check == "no" or height_check == "n":
                                print("Be serious this time please")
                            else:
                                print("Invalid")
                                
                        else:
                            height_limit = True
                            
                            


                        
                    temp = ''
                    if adult_height >= 160: #checking if height is more or equal to 160
                        print("The rides person {} can go on are:".format(index + 1))
                        print()
                        time.sleep(0.5)
                        for word in one_sixty_cm: #For loop to print out each word in the list
                            print(word)
                        print()
                        time.sleep(1.5)
                        for word in one_fifty_cm:#For loop to print out each word in the list
                            print(word)
                        print()
                        time.sleep(1.5)
                        for word in one_thirty_cm:#For loop to print out each word in the list
                            print(word)
                        print()
                        time.sleep(1.5)
                        
                    elif adult_height < 160 and adult_height >= 150: #checking that the height is less than 160 and more or equal to 150
                        print("The rides person {} can go on are:".format(index + 1))
                        print()
                        time.sleep(0.5)
                        for word in one_fifty_cm:
                            print(word)
                        print()
                        time.sleep(1.5)
                        for word in one_thirty_cm:
                            print(word)
                        print()
                        time.sleep(1.5)
                        
                    elif adult_height < 150 and adult_height >= 130: #checking that the height is less than 150 and more or equal to 130
                        print()
                        print("The rides person {} can go on are:".format(index + 1))
                        time.sleep(0.5)
                        for word in one_thirty_cm:
                            print(word)
                        print()
                        time.sleep(1.5)
                    else:
                        print("Sorry person {} is to short to go on any rides".format(index + 1))
                        
                if kids_amount != 0:
                        
                        child_validation = False
                        
                        while not child_validation:
                                
                                is_child_riding = input("Is your kid/s going on any rides today? (yes or no)").lower()

                                if is_child_riding == "yes" or is_child_riding == "y":
                                        print("here are the rides your kid/s can go on")
                                        print()
                                        for word in kids_rides: #for loop to show kids rides
                                            print(word)
                                            print()
                                            child_validation = True
                                        
                                elif is_child_riding == "no" or is_child_riding == "n":
                                        print("Thats fine")
                                        child_validation = True

                                else:
                                    print("Invalid")

                                    
                                
                bill = party_size*5
                if platinum_pass == True:
                    bill = bill
                    
                if kids_amount != 0:
                    if is_child_riding == "yes" or is_child_riding == "y": #payment for entering the amusment park
                        bill = bill + kids_amount*3
                        
                print("Thank you for using this program :D")
                print("your bill is",bill,"dollars")

                             
                validation = False
                
                time.sleep(1)
                while not validation:
                        again = input("Do you want to enter another party?\nyes or no").lower() #asking the user if they want to restart the program

                        if again == "yes" or again == "y":
                                another_one =  False
                                validation = True
                        elif again == "no" or again == "n":
                                another_one = True
                                validation = True
                        else:
                                print("Invalid")

            else:
                another_one = True
print("Ok bye now")



























