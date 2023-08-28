'''
Jovienne Trotta
CS 5001 | Fall 2022
5001 Lab : 9 Epic Battle Simulator

This contains the methods and attributes for my character object.
'''

# Basic Imports
from random import randint

# This is the list of available characters for the user to select from.
character_list = [("Aluminum Monster",50,5), ("Golden God",20,5), ("Pepe Silvia",30,10), ("Trashman",20,15), ("Vic Vinegar",30,15)]

# This creates a class called Character
class Character:

    '''
    Initializes a character class
    Parameters: name as a string, an integer for strength, and an integer for hitPoints
    Returns: N/A
    '''
    def __init__(self, name = "Ward", hitPoints = 5, strength = 5, weapon = None):
        self.name = name
        self.hitPoints = hitPoints
        self.strength = strength
        self.weapon = weapon
        self.alive = True

    '''
    Prints character values
    Parameters: N/A
    Returns: name as a string, an integer for strength, and an integer for health (hitPoints)
    '''
    def __str__(self):
        return self.name + " - " + str(self.strength) + " strength point(s) and " + str(self.hitPoints) + " health point(s) | WEAPON: " + str(self.weapon)

    '''
    Sets character weapon
    Parameters: an integer
    Returns: weapon name as a string, an integer for strength, and an integer for durability
    '''
    def giveWeapon(self,weapon_selection):
        self.weapon = weapon_selection

    '''
    Function that allows a character or opponent to take damage until one dies
    Parameters: damage as an integer
    Returns: a Boolean value; an integer
    '''
    def take_damage(self, damage):
        self.hitPoints -= damage
        if self.hitPoints <= 0:
            self.hitPoints = 0
            self.alive = False
    
    '''
    Function that allows a character or opponent to deal damage until one dies
    Parameters: an opponent character (string)
    Returns: a string
    '''
    def fight(self, opponent):
        while (self.alive == True) and (opponent.alive == True):

            #Initiative will randomize the fighting since the gang doesn't fight fair :) 
            initiative = randint(0,1)

            if initiative == 0:
                damage_taken = (randint(0,opponent.strength)) + (randint(0,opponent.weapon.attack()))
                print(self.name + " has taken " + str(damage_taken) + " points of damage.")
                self.take_damage(damage_taken)
                if not self.alive: 
                    break

            elif initiative == 1:
                damage_taken = (randint(0,self.strength)) + (randint(0,self.weapon.attack()))
                print(opponent.name + " has taken " + str(damage_taken) + " points of damage.")
                opponent.take_damage(damage_taken)
                if not opponent.alive:
                    break
        
        if self.alive:
            print("\n" + self.name + " has defeated " + opponent.name + "!")
            return self

        elif opponent.alive:
            print("\n" + opponent.name + " has defeated " + self.name + "!")
            return opponent