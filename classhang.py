# This is the hangman game.
import random
import sys
from hangmanascii import *
import time
import string
import textwrap

SCREEN_SIZE = 100

#list_of_words = "words.txt"

def load_wordlist():
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    self.lines = open(self.list_of_words).read().decode('utf-8').split('\n')
    self.lines = [line for line in self.lines if line.isalpha()]
    self.lines = [line for line in self.lines if line.islower()]
    self.lines = [line for line in self.lines if len(line) > 6]
    self.lines = [line for line in self.lines if set(line) <= alphabet]
   
    #print self.lines
    return self.lines
        

        
def cool_print(str):
    textwrap.dedent(str)
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)   # Or whatever delay you'd like
    print   # One last print to make sure that you move to a new line
        
def clear_screen():
#clear screen variable (how many blank lines to print)
    print "\n"*SCREEN_SIZE
        

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
        return ' '.join(self.billboard)
        
    def validate_guess(self, letter):
        if len(letter) != 1:
            return HANGMAN_ONELETTER
        elif letter in self.guesses:
            return HANGMAN_ALREADYGUESSED
        elif letter not in self.allowed_letters:
            return HANGMAN_ALPHABET
        self.guesses.append(letter)
        
        
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
            return HANGMAN_LOSE
        if hit >= set(self.secret_word):
            return HANGMAN_WIN
        else:
            return HANGMAN_CONTINUE
        
        
def run_game():
    pass
    

mygame = Hangman()

intro_text = textwrap.dedent("""
The year is 1750. You are a resident of England and have been charged with a crime! 
You attempted to steal an apple at the market. You have been scheduled to be hanged 
in the village of Tyburn UNLESS you can guess the secret word that is chosen by the
king. 
""")

cool_print(intro_text)

raw_input("Press ENTER to Continue.\n> ")

print intro_text
clear_screen()
print king
time.sleep(1)
clear_screen()
print king_speaks
time.sleep(1)
clear_screen()
print king
time.sleep(1)
clear_screen()

while True:

    mygame.guess = raw_input("Guess a letter!\n> ")


    result = mygame.validate_guess(mygame.guess)


    if result == 'HANGMAN_ONELETTER':
        print "Please type one letter."
    
    elif result == 'HANGMAN_ALREADYGUESSED':
        print "You already guessed that letter."
    
    elif result == 'HANGMAN_ALPHABET':
        print "Please type a letter from the English alphabet."

    
    mygame.construct_billboard()
    mygame.guess_status()
    state = mygame.game_status()
    
    if state == 'HANGMAN_LOSE':
        print "Quit?"
        break
    
    elif state == 'HANGMAN_WIN':
        print "Congratulations"
        break
        
    elif state == HANGMAN_CONTINUE:
        pass

