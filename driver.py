'''
Jovienne Trotta
CS 5001 | Fall 2022
5001 Lab : 9 Epic Battle Simulator

The goal of this lab is to explore class creation by creating a battle application.
The application allows the user to choose two characters, two weapons, and have the characters fight each other.
'''

# Basic Imports
import character as chr
import weapon as wpn
from random import randint

# Testing Imports
import unittest
from test import * 

'''
User selects a character
Parameters: N/A
Returns: an integer
'''
def select_character():

    global character_selection 

    # Prints the menu
    for i in range(len(chr.character_list)):
                print(str(i) + "..." + str(chr.Character(chr.character_list[i][0],chr.character_list[i][1],chr.character_list[i][2])))
    print("5...WILD CARD BITCHES: A random character is selected! Yeeeeeeehaw!")

    while True:
        try:

            character_selection = int(input("\nMake your selection: "))

            # Creates random option
            if character_selection == 5:
                character_selection = randint(0,(len(chr.character_list)-1))
                return character_selection

            elif (character_selection >= len(chr.character_list)) or (character_selection < 0):
                raise IndexError
            
            else:
                return character_selection

        # Throws an error if input is not a number
        except ValueError:
            print("\nERROR: You must enter a number.")
            continue
        
        # Throws an error if input is not in the list range
        except IndexError:
            print("\nERROR: You must enter one of the numerical options listed.")
            continue

'''
User selects a weapon
Parameters: N/A
Returns: an integer
'''
def select_weapon():

    global weapon_selection 

    # Prints the menu
    for i in range(len(wpn.weapons_list)):
                print(str(i) + "..." + str(wpn.Weapon(wpn.weapons_list[i][0],wpn.weapons_list[i][1],wpn.weapons_list[i][2])))
    print("5...WILD CARD BITCHES: A random weapon is selected! Yeeeeeeehaw!")

    while True:
        try:

            weapon_selection = int(input("\nMake your selection: "))

            # Creates random option
            if weapon_selection == 5:
                weapon_selection = randint(0,(len(wpn.weapons_list)-1))
                return weapon_selection

            elif (weapon_selection >= len(wpn.weapons_list)) or (weapon_selection < 0):
                raise IndexError
            
            else:
                return weapon_selection

        # Throws an error if input is not a number
        except ValueError:
            print("\nERROR: You must enter a number.")
            continue
        
        # Throws an error if input is not in the list range
        except IndexError:
            print("\nERROR: You must enter one of the numerical options listed.")
            continue

# This is the driver function
def main():

    # Character Selection
    print("\nSelect your Character!")
    select_character()
    c1 = chr.Character(chr.character_list[character_selection][0],chr.character_list[character_selection][1],chr.character_list[character_selection][2])
    del(chr.character_list[character_selection])

    # Weapon Selection
    print("\nSelect your Weapon!")
    select_weapon()
    w1 = wpn.Weapon(wpn.weapons_list[weapon_selection][0],wpn.weapons_list[weapon_selection][1],wpn.weapons_list[weapon_selection][2])
    c1.giveWeapon(w1)
    del(wpn.weapons_list[weapon_selection])

    # Player Confirmation Message
    print("\nYou have selected " + c1.name + " armed with " + c1.weapon.name + ".\n")

    while len(chr.character_list) >= 1:

        # Opponent Selection
        print("\nSelect your Opponent!")
        select_character()
        c2 = chr.Character(chr.character_list[character_selection][0],chr.character_list[character_selection][1],chr.character_list[character_selection][2])
        del(chr.character_list[character_selection])

        # Opponent Weapon Selection
        print("\nSelect your Opponent's Weapon!")
        select_weapon()
        w2 = wpn.Weapon(wpn.weapons_list[weapon_selection][0],wpn.weapons_list[weapon_selection][1],wpn.weapons_list[weapon_selection][2])
        c2.giveWeapon(w2)
        del(wpn.weapons_list[weapon_selection])
                    
        # Opponent Confirmation Message
        print("\nYou have selected " + c2.name + " armed with " + c2.weapon.name + " as your opponent.\n")

        winner = c1.fight(c2)

        if winner != c1:
            print("\nYou lose! Play again?\n")
            break
        
        else:
            continue
        
    if (len(chr.character_list) == 0) and (c1.alive == True):
        print("\nCongratulations! You've beaten the gang!\n")

main()

#unittest.main()