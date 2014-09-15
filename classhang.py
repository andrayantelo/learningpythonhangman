# This is the hangman game.
import random
import sys
from hangmanascii import *
import time
import string
import textwrap

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
        
def clear_screen(self):
#clear screen variable (how many blank lines to print)
    print "\n"* self.screen_size
        

HANGMAN_WIN = 'HANGMAN_WIN'
HANGMAN_LOSE = 'HANGMAN_LOSE'
HANGMAN_ALREADYGUESSED = 'ALREADY_GUESSED'
HANGMAN_CONTINUE = 'HANGMAN_CONTINUE'
HANGMAN_ONELETTER = 'HANGMAN_ONELETTER'
HANGMAN_ALPHABET = 'HANGMAN_ALPHABET'


class Hangman(object):
	
    def __init__(self, screen_size = 100):
        self.screen_size = screen_size
        self.allowed_letters = 'abcdefghijklmnopqrstuvwxyz'
        self.wordlist = 'Apple Watermelon Pineapple Papaya Strawberry Blueberry Fig Durian'.split()
        self.list_of_words = "words.txt"
        self.intro_text = textwrap.dedent("""
        The year is 1750. You are a resident of England and have been charged with a crime! 
        You attempted to steal an apple at the market. You have been scheduled to be hanged 
        in the village of Tyburn UNLESS you can guess the secret word that is chosen by the
        king. """)
        self.secret_word = 'apple'
        self.guess = ''
        self.guesses = []
        self.trimmed_incorrect_guesses =[]
        self.incorrect_guesses = []
        self.correct_guesses = []

    def choose_random_word(self):
         self.secret_word = random.choice(self.wordlist)   
         return self.secret_word
        
    def construct_billboard(self):
        
        self.billboard = list(self.secret_word)
        for i, letter in enumerate(self.billboard):
            if letter not in self.guesses:
                self.billboard[i] = "_"
        print ' '.join(self.billboard)    
        return ' '.join(self.billboard)
        
    def validate_guess(self, guess):
        if len(guess) != 1:
            return HANGMAN_ONELETTER
        if guess in self.guesses:
            return HANGMAN_ALREADYGUESSED
        if guess not in self.allowed_letters:
            return HANGMAN_ALPHABET
        self.guesses.append(guess)
        
        
    def guess_status(self):
        for letter in self.guesses:
            if letter not in self.secret_word:
                self.incorrect_guesses.append(letter)
    
            elif letter in self.secret_word:
                self.correct_guesses.append(letter)
       
    def game_status(self):
        guesses = self.guesses
        for letter in self.incorrect_guesses:
            if letter not in self.trimmed_incorrect_guesses:
                self.trimmed_incorrect_guesses.append(letter)
        missed = self.trimmed_incorrect_guesses
        hit = set(self.correct_guesses)
        if len(missed) >= 7:
            print HANGMAN_LOSE
            return HANGMAN_LOSE
        if hit >= set(self.secret_word):
            print HANGMAN_WIN
            return HANGMAN_WIN
        else:
            print HANGMAN_CONTINUE
            return HANGMAN_CONTINUE
        
        
        


mygame = Hangman()
#mygame.choose_random_word()
mygame.construct_billboard()
print mygame.secret_word
mygame.guess = 't'
print mygame.validate_guess(mygame.guess)
print mygame.guesses
mygame.guess_status()
print mygame.correct_guesses
print mygame.incorrect_guesses
mygame.game_status()

mygame.guess = 'o'
print mygame.validate_guess(mygame.guess)
print mygame.guesses
mygame.guess_status()
print mygame.correct_guesses
print mygame.incorrect_guesses
mygame.game_status()

mygame.guess = 'r'
print mygame.validate_guess(mygame.guess)
print mygame.guesses
mygame.guess_status()
print mygame.correct_guesses
print mygame.incorrect_guesses
mygame.game_status()

mygame.guess = 'h'
print mygame.validate_guess(mygame.guess)
print mygame.guesses
mygame.guess_status()
print mygame.correct_guesses
print mygame.incorrect_guesses
mygame.game_status()

mygame.guess = 'q'
print mygame.validate_guess(mygame.guess)
print mygame.guesses
mygame.guess_status()
print mygame.correct_guesses
print mygame.incorrect_guesses
mygame.game_status()

mygame.guess = 'w'
print mygame.validate_guess(mygame.guess)
print mygame.guesses
mygame.guess_status()
print mygame.correct_guesses
print mygame.incorrect_guesses
mygame.game_status()

mygame.guess = 'y'
print mygame.validate_guess(mygame.guess)
print mygame.guesses
mygame.guess_status()
print mygame.correct_guesses
print mygame.trimmed_incorrect_guesses
mygame.game_status()

