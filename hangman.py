# This is the hangman game.
import random
import sys
from hangmanascii import *

def intro(): 
    print """The year is 1835. You are a resident of England and have been charged with a crime! 
            You attempted to steal an apple at the market. You have been scheduled to be hanged 
            in the village of Tyburn UNLESS you can guess the secret word that is chosen by the
            king. """

def start():
    randomwordchoice()



def randomwordchoice():
    # using a small word list for now
    wordlist = 'Apple Watermelon Pineapple Papaya Strawberry Blueberry Fig Durian'.split()
    lowerwordlist = [letter.lower() for letter in wordlist] # make everything lower case
    
    secretword = random.choice(lowerwordlist)
    #printing out the secretword just to see if spaces match update


    print "_ "*len(secretword)

    guesses = ''

    while True: #ask about formatting
        guess = str(raw_input("\nGuess a letter!\n> "))
        guess = guess.lower()


        guesses += guess
        
        
        #trying to figure out a way to keep track of how many times a letter has been guessed.
        if guess in guesses:
            print "You already guessed this."
            
        # trying out a list for the incorrectguesses to use later when programming the hangman appearance
        incorrectguesses = []
        for letter in guesses:
            if letter not in secretword:
                incorrectguesses.append(letter)
            else:
                pass
          
        # keeping track of correct guesses
        correctguesses = []
        for letter in guesses:
            if letter in secretword:
                correctguesses.append(letter)
            else:
                pass
        print correctguesses
        # I want it to appear like I'm not just printing the same things over and over	
        print "\n"*50
        
        for letter in secretword:
            if letter in guesses:
                print letter,
            else:
                print '_',
        print "\n These are the guesses you have made so far:\n", guesses
        # i want to then print a body part but i want the body parts to be printed at the right time

        hangmanascii(incorrectguesses)
        
        youwin = guessed_all_letters(secretword, correctguesses)

        if youwin == True:
            play_more()
            
def hangmanascii(incorrectguesses):
    if len(incorrectguesses) == 0:
        print noman
    if len(incorrectguesses) == 1:
        print head
    if len(incorrectguesses) == 2:
        print onearm
    if len(incorrectguesses) == 3:
        print twoarms
    if len(incorrectguesses) == 4:
        print torso
    if len(incorrectguesses) == 5:
        print torso2
    if len(incorrectguesses) == 6:
        print oneleg
    if len(incorrectguesses) == 7:
        print hungman
        print "GAME OVER YOU'RE DEAD"
        sys.exit()
                
def play_more():
    print "You win!"
    print "Play again? Y or N?"
    while True:
        play_again = str(raw_input("> "))
        play_again.upper()
        if play_again == "Y":
            start()
        if play_again == "N":
            print "Goodbye."
            sys.exit()
        else:
            print "Please type Y or N."


def guessed_all_letters(secretword, correctguesses): 
    for letter in secretword:
        if letter not in correctguesses:
            return False
    return True


randomwordchoice()
