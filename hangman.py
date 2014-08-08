# This is the hangman game.
import random
import sys
from hangmanascii import *
import time

SCREEN_SIZE = 100

list_of_words = "words.txt"

def load_wordlist():
    lines = open(list_of_words).read().decode('utf-8').split('\n')
    return lines
    

def cool_print(str):
  for char in str:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)   # Or whatever delay you'd like
  print   # One last print to make sure that you move to a new line


def intro(): 
    cool_print("""
The year is 1750. You are a resident of England and have been charged with a crime! 
You attempted to steal an apple at the market. You have been scheduled to be hanged 
in the village of Tyburn UNLESS you can guess the secret word that is chosen by the
king. """)
            
    raw_input("\n\nPRESS ENTER TO CONTINUE.\n> ") 

def start():
    randomwordchoice()

def clear_screen():
#clear screen variable (how many blank lines to print)
    print "\n"* SCREEN_SIZE

def randomwordchoice():
    # using a small word list for now
    wordlist = 'Apple Watermelon Pineapple Papaya Strawberry Blueberry Fig Durian'.split()
    lowerwordlist = [letter.lower() for letter in wordlist] # make everything lower case
    
    
    secretword = random.choice(lowerwordlist)
    #printing out the secretword just to see if spaces match update
    
    
    
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

    print "_ "*len(secretword)
    print noman

    guesses = ''

    while True: #ask about formatting
        
        guess = str(raw_input("\nGuess a letter!\n> "))
        guess = guess.lower()
        allowed_letters = 'abcdefghijklmnopqrstuvwxyz'
        
             
       
        if len(guess) != 1:
            clear_screen()
            print "Type in a single letter."
            secretword_spaces(secretword, guesses)
            print "\n These are the guesses you have made so far:\n", guesses
            hangmanascii(incorrectguesses)
            continue
        if guess in guesses:
            clear_screen()
            print "You already guessed that."
            secretword_spaces(secretword, guesses)
            print "\n These are the guesses you have made so far:\n", guesses
            hangmanascii(incorrectguesses)
            continue
        if guess not in allowed_letters:
            clear_screen()
            print "Please type in a single letter from the English alphabet."
            secretword_spaces(secretword, guesses)
            print "\n These are the guesses you have made so far:\n", guesses
            hangmanascii(incorrectguesses)
            continue
    
 
        clear_screen()
        guesses += guess
         # trying out a list for the incorrectguesses to use later when programming the hangman appearance
        incorrectguesses = []
        for letter in guesses:
            if letter not in secretword:
                incorrectguesses.append(letter)
                
        # keeping track of correct guesses
        correctguesses = []
        for letter in guesses:
            if letter in secretword:
                correctguesses.append(letter)
 
        secretword_spaces(secretword, guesses) 
        print "\n These are the guesses you have made so far:\n", guesses  
        hangmanascii(incorrectguesses)
            
       	
       
          
        
        youwin = guessed_all_letters(secretword, correctguesses)

        if youwin == True:
            print "You win!"
            play_more()
            
            
def secretword_spaces(secretword, guesses):
	for letter in secretword:
            if letter in guesses:
                print letter,
            else:
                print '_',
	
            
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
        print laughing_king
        print "\n\nGAME OVER YOU'RE DEAD"
        play_more()
        
                
def play_more():
    print "Play again? Y or N?"
    while True:
        play_again = str(raw_input("> "))
        play_again = play_again.upper()
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


    
intro()
randomwordchoice()
