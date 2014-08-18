# This is the hangman game.
import random
import sys
from hangmanascii import *
import time
import string


class hangman(object):
	
	def __init__(self, screen_size = 100):
		self.screen_size = screen_size
		self.wordlist = 'Apple Watermelon Pineapple Papaya Strawberry Blueberry Fig Durian'.split()
		self.list_of_words = "words.txt"

#SCREEN_SIZE = 100

#list_of_words = "words.txt"

	def load_wordlist(self):
		alphabet = set('abcdefghijklmnopqrstuvwxyz')
		self.lines = open(self.list_of_words).read().decode('utf-8').split('\n')
		self.lines = [line for line in self.lines if line.isalpha()]
		self.lines = [line for line in self.lines if line.islower()]
		self.lines = [line for line in self.lines if len(line) > 6]
		self.lines = [line for line in self.lines if set(line) <= alphabet]
   
		print self.lines
		return self.lines
   

mygame = hangman()
mygame.load_wordlist()
