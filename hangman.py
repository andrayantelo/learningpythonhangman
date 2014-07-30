# This is the hangman game.
import random

def intro(): 
	print "The game where your life is at stake! Guess the word right and you may live!"
	
def start():
	randomwordchoice()

	
	displayfullhangman()

def randomwordchoice():
	# using a small word list for now
	wordlist = 'Apple Watermelon Pineapple Papaya Strawberry Blueberry Fig Durian'.split()
	secretword = random.choice(wordlist)
	#printing out the secretword just to see if spaces match update
	print secretword
	print "_"*len(secretword)
	
	
	
def displayfullhangman():
	print "hangman goes here"
	
def displaynohangman():
	print "just the hanging post with no guy"

def letterspaces():
	pass
	
	
randomwordchoice()