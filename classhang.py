# This is the hangman game.
import random
import sys
from hangmanascii import *
import time
import string
import textwrap


class hangman(object):
	
    def __init__(self, screen_size = 100):
        self.screen_size = screen_size
        self.wordlist = 'Apple Watermelon Pineapple Papaya Strawberry Blueberry Fig Durian'.split()
        self.list_of_words = "words.txt"
        self.intro_text = textwrap.dedent("""
        The year is 1750. You are a resident of England and have been charged with a crime! 
        You attempted to steal an apple at the market. You have been scheduled to be hanged 
        in the village of Tyburn UNLESS you can guess the secret word that is chosen by the
        king. """)

#SCREEN_SIZE = 100

#list_of_words = "words.txt"

    def load_wordlist(self):
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        self.lines = open(self.list_of_words).read().decode('utf-8').split('\n')
        self.lines = [line for line in self.lines if line.isalpha()]
        self.lines = [line for line in self.lines if line.islower()]
        self.lines = [line for line in self.lines if len(line) > 6]
        self.lines = [line for line in self.lines if set(line) <= alphabet]
   
		#print self.lines
        return self.lines
        
    def cool_print(self, str):
        textwrap.dedent(str)
        for char in str:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)   # Or whatever delay you'd like
        print   # One last print to make sure that you move to a new line
        
    def intro(self): 
        self.cool_print(self.intro_text)
            
        raw_input("\n\nPRESS ENTER TO CONTINUE.\n> ") 
   

mygame = hangman()
mygame.intro()
