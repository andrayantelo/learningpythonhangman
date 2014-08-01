# This is the hangman game.
import random
import sys
from hangmanascii import *

def intro(): 
	print "The game where your life is at stake! Guess the word right and you may live!"
	
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
		else:
			pass
						
		
			
		
	
# bodyparts = ['head', 'arm', 'twoarms', 'torso', 'oneleg', 'full body']
# head = hangman w/ head
# arm = hangman w/ head + arm
# twoarms = hangman w/ heat + 2 arms
# torso = hangman w/ head +2 arms + torso
# oneleg = hangman w/ head + 2 arms + torso + 1 leg
# fullbody = hangman w/ head + 2 arms + torso + 2 legs
	
def displaynohangman():
	print "just the hanging post with no guy"

def letterspaces():
	pass
	
	
randomwordchoice()