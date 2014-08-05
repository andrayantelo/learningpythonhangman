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
		
		# I want it to appear like I'm not just printing the same things over and over	
        print "\n"*50
		
        for letter in secretword:
            if letter in guesses:
                print letter,
            else:
                print '_',
        print "\n These are the guesses you have made so far:\n", guesses
		# i want to then print a body part but i want the body parts to be printed at the right time
		
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
        if len(correctguesses) == len(secretword):
            print "YOU WIN! Play again?"
            # start() once I have the design figured out. 
        else:
            pass
		
        				
		
			
		
	

	
def displaynohangman():
	print "just the hanging post with no guy"

def letterspaces():
	pass
	
	
randomwordchoice()
