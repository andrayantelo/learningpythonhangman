# This is the hangman game.
import random
import sys
from hangmanascii import *
import time
import string
import textwrap

#SCREEN_SIZE = 100

#list_of_words = "words.txt"


class Hangman(object):
	
    def __init__(self, screen_size = 100):
        self.screen_size = screen_size
        self.wordlist = 'Apple Watermelon Pineapple Papaya Strawberry Blueberry Fig Durian'.split()
        self.list_of_words = "words.txt"
        self.intro_text = textwrap.dedent("""
        The year is 1750. You are a resident of England and have been charged with a crime! 
        You attempted to steal an apple at the market. You have been scheduled to be hanged 
        in the village of Tyburn UNLESS you can guess the secret word that is chosen by the
        king. """)
        self.secret_word = 'apple'
        self.guess = ''
        self.guesses = ''
        self.incorrect_guesses = []
        self.correct_guesses = []



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
        
    def clear_screen(self):
    #clear screen variable (how many blank lines to print)
        print "\n"* self.screen_size
        
    def intro(self): 
        self.cool_print(self.intro_text)
            
        raw_input("\n\nPRESS ENTER TO CONTINUE.\n> ") 
        
        self.clear_screen()
        print king
        time.sleep(1)
        self.clear_screen()
        print king_speaks
        time.sleep(1)
        self.clear_screen()
        print king
        time.sleep(1) 
        self.clear_screen()
   
    def random_word_choice(self):
        self.secret_word = random.choice(self.load_wordlist())
        print "_ "*len(self.secret_word)
        print noman
        return self.secret_word
        
        
    def game(self):
        self.intro()
        self.random_word_choice()
        

        while True: #ask about formatting
            self.incorrect_guesses = []
            self.correct_guesses = []
        
            self.guess = str(raw_input("\nGuess a letter!\n> "))
            self.guess = self.guess.lower()
            allowed_letters = 'abcdefghijklmnopqrstuvwxyz'
        
            if len(self.guess) != 1:
                self.clear_screen()
                print "Type in a single letter."
                self.secretword_spaces(self.secret_word)
                print "\n These are the guesses you have made so far:\n", self.guesses
                self.hangman_ascii()
                
                continue
            if self.guess in self.guesses:
                self.clear_screen()
                print "You already guessed that."
                self.secretword_spaces(self.secret_word)
                print "\n These are the guesses you have made so far:\n", self.guesses
                self.hangman_ascii()
               
                continue
            if self.guess not in allowed_letters:
                self.clear_screen()
                print "Please type in a single letter from the English alphabet."
                self.secretword_spaces(self.secret_word)
                print "\n These are the guesses you have made so far:\n", self.guesses
                self.hangman_ascii()
                
                continue
    
 
            self.clear_screen()
            
            self.guesses += self.guess
            
            self.incorrectguesses(self.guesses)
            print self.incorrect_guesses
            self.correctguesses(self.guesses)
            print self.correct_guesses
            
            self.secretword_spaces(self.secret_word)
            print "\n These are the guesses you have made so far:\n", self.guesses
            self.hangman_ascii()
            
            
        
        
    def secretword_spaces(self, secret_word):
        for letter in secret_word:
            if letter in self.guesses:
                print letter,
            else:
                print '_',
                
    def hangman_ascii(self):
        if len(self.incorrect_guesses) == 0:
            print noman
        if len(self.incorrect_guesses) == 1:
            print head
        if len(self.incorrect_guesses) == 2:
            print onearm
        if len(self.incorrect_guesses) == 3:
            print twoarms
        if len(self.incorrect_guesses) == 4:
            print torso
        if len(self.incorrect_guesses) == 5:
            print torso2
        if len(self.incorrect_guesses) == 6:
            print oneleg
        if len(self.incorrect_guesses) == 7:
            print hungman
            time.sleep(5)
            print laughing_king, '\n\n\n\n'
            print "The secret word was: %s.\n\n" % self.secret_word
            print "\n\nGAME OVER YOU'RE DEAD"
            ask_user_play()
            
    def incorrectguesses(self, guesses):
        for letter in self.guesses:
            if letter not in self.secret_word:
                self.incorrect_guesses.append(letter)
        return self.incorrect_guesses
        
    def correctguesses(self, guesses):
        for letter in self.guesses:
            if letter in self.secret_word:
                self.correct_guesses.append(letter)
        return self.correct_guesses

def ask_user_play():
    while True:
        print "\n Would you like to play again?"
        response = str(raw_input("y or n?\n> "))
        response = response.lower()
        if response == 'y':
            mygame = Hangman()
            mygame.game()
        if response == 'n':
            exit()
        else:
            continue

#response = "y"
#while True:
    
#    if response == "y":        
        
 #       ask_user_play()

mygame = Hangman()
mygame.game()
