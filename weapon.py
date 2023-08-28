'''
Jovienne Trotta
CS 5001 | Fall 2022
5001 Lab : 9 Epic Battle Simulator

This contains the methods and attributes for my weapon object.
'''

# Basic Imports
from random import randint 

# This is the list of available weapons for the user to select from.
weapons_list = [("An egg for these trying times",20,1), ("Fight Milk",5,20), ("Frank's Gun",20,3), ("Toe Knife",10,10), ("Kitten Mittens",2,100)]

# This creates a class called Weapon
class Weapon:

    '''
    Initializes a weapon class
    Parameters: name as a string, an integer for strength, and an integer for durability
    Returns: N/A
    '''
    def __init__(self, name = "generic dagger", strength = 1, durability = 2):
        self.name = name
        self.strength = strength
        self.durability = durability
        self.broken = False

    '''
    Prints weapon values
    Parameters: N/A
    Returns: name as a string, an integer for strength, and an integer for durability
    '''
    def __str__(self):
        return self.name + " - " + str(self.strength) + " strength point(s) and " + str(self.durability) + " durability point(s)"

    '''
    Function that randomly selects a damage amount based off the weapon's strength
    Parameters: N/A
    Returns: a Boolean value; an integer
    '''
    def attack(self):
        self.durability -= 1

        if self.durability <= 0:
            self.durability = 0 
            self.broken = True
            return 0

        # Creates the "Toe Knife" random event; 25% chance of double damage
        else:

            if self.name == "Toe Knife":

                botched_toe = randint(1,4)

                if botched_toe == 1:
                    print("Uh oh! Botched toe! x2 damage!")
                    damage_added = randint(0,self.strength)
                    return (damage_added*2)
                    
                else:
                    damage_added = randint(0,self.strength)
                    return damage_added
                    
            else:
                damage_added = randint(0,self.strength)
                return damage_added
