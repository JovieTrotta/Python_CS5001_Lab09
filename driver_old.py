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
    for i in range(len(chr.character_list)):
                print(str(i) + "..." + str(chr.Character(chr.character_list[i][0],chr.character_list[i][1],chr.character_list[i][2])))
    global character_selection 
    character_selection = int(input("\nMake your selection: "))
    if character_selection == 5:
        character_selection = randint(0,(len(chr.character_list)-1))

'''
User selects a weapon
Parameters: N/A
Returns: an integer
'''
def select_weapon():
    for i in range(len(wpn.weapons_list)):
                print(str(i) + "..." + str(wpn.Weapon(wpn.weapons_list[i][0],wpn.weapons_list[i][1],wpn.weapons_list[i][2])))
    global weapon_selection 
    weapon_selection = int(input("\nMake your selection: "))
    if weapon_selection == 5:
        weapon_selection = randint(0,(len(wpn.weapons_list)-1))

# This is the driver function
def main():

    while True:
        
        try:

            # Character Selection - Player One
            print("\nPlayer One: Select your Character!")
            select_character()
            c1 = chr.Character(chr.character_list[character_selection][0],chr.character_list[character_selection][1],chr.character_list[character_selection][2])
            del(chr.character_list[character_selection])

            # Weapon Selection - Player One
            print("\nPlayer One: Select your Weapon!")
            select_weapon()
            w1 = wpn.Weapon(wpn.weapons_list[weapon_selection][0],wpn.weapons_list[weapon_selection][1],wpn.weapons_list[weapon_selection][2])
            c1.giveWeapon(w1)
            del(wpn.weapons_list[weapon_selection])

            # Player One Confirmation Message
            print("\nPlayer ONE has selected " + c1.name + " armed with " + c1.weapon.name + ".")

            # Character Selection - Player Two
            print("\nPlayer Two: Select your Character!")
            select_character()
            c2 = chr.Character(chr.character_list[character_selection][0],chr.character_list[character_selection][1],chr.character_list[character_selection][2])
            del(chr.character_list[character_selection])

            # Weapon Selection - Player Two
            print("\nPlayer Two: Select your Weapon!")
            select_weapon()
            w2 = wpn.Weapon(wpn.weapons_list[weapon_selection][0],wpn.weapons_list[weapon_selection][1],wpn.weapons_list[weapon_selection][2])
            c2.giveWeapon(w2)
            del(wpn.weapons_list[weapon_selection])
                
            # Player Two Confirmation Message
            print("\nPlayer TWO has selected " + c2.name + " armed with " + c2.weapon.name + ".")

            print("\n")
            c1.fight(c2)
            break

        except ValueError:
            print("\nERROR: You must enter one of the numerical options listed.")
            break

        except IndexError:
            print("\nERROR: You must enter one of the numerical options listed.")
            break

main()

#unittest.main()
