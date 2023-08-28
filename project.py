'''
Jovienne Trotta
CS 5001 | Fall 2022
Final Synthesis Project
Chapter 7: While Loops

This is the answer key for Chapter 7's assignment. 
'''

# Imports the randint function
from random import randint

# This is the word list.
word_list = ["happy","music","territory","bandit","wonderful","yuzu","garbage","python","motorbike","catfish"]

# Creates a variable that will count the incorrect attempts to guess a letter.
wrong_count = 0

'''
This function will randomly select a word from the list
Parameters: N/A
Returns: a list
'''
def pick_word():
    word = word_list[randint(0,(len(word_list) - 1))]
    return list(word)
    
'''
This function will take a letter from the user, check if it exists in the word, and either remove that letter or add to the wrong_count
Parameters: a list, a string
Returns: a string
'''
def get_letter(word,letter):

    # Declares variable as global, so it can be accessed later
    global wrong_count

    # If the user's input letter is in the chosen word...
    if letter in word:

        # Removes multiple instances of the letter if it appears more than once in the word
        instances = word.count(letter)
        for i in range(instances):
            word.remove(letter)
        
        # Print statement to help the user track how the game is going 
        print("Correct!")
        print("Attempts left:",(10 - wrong_count))

    # If the user's input letter is NOT in the chosen word...  
    else:

        # Raise the wrong_count by 1
        wrong_count += 1

        # Print statement to help the user track how the game is going 
        print("Incorrect!")
        print("Attempts left:",(10 - wrong_count))
    
# This is the driver function
def main():

    # Gets the random word
    word = pick_word()

    # While there are both letters left in the word and the wrong_count is less than 5
    while (len(word) != 0) and (wrong_count < 10):

        # Run the get_letter function
        get_letter(word,input("Guess a letter: "))

        # If the user guesses all the right letters...
        if (len(word) == 0):
            print("You win!")

        # If the wrong_count reaches the max...
        elif (wrong_count == 10):
            print("You lose!")
    
main()


