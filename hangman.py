# This is the hangman game.
import random

def intro(): 
	print "The game where your life is at stake! Guess the word right and you may live!"
	
def start():
	randomwordchoice()

	

def randomwordchoice():
	# using a small word list for now
	wordlist = 'Apple Watermelon Pineapple Papaya Strawberry Blueberry Fig Durian'.split()
	secretword = random.choice(wordlist)
	#printing out the secretword just to see if spaces match update
	print secretword
	print "_ "*len(secretword)
	
	while True:
		guess = raw_input("Guess a letter!\n> ")
		for letter in secretword:
			if letter in guess:
				print letter,
			else:
				print '_',
				# i want to then print a body part but i want the body parts to be printed in order
				# and i also want the order to be known by how many times the loop has been run
			
		
	
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