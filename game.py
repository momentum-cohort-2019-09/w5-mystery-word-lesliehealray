from collections import defaultdict
from random import choice



def word_list():
    with open("words.txt") as file_handler:
        words = file_handler.read().split()
    return words
    

def game_levels(words):
    levels = defaultdict(list)
    for word in words:
        if len(word) <= 6:
            levels['EASY'].append(word)
        elif 8 > len(word) > 6:
            levels['MODERATE'].append(word)
        else:
            levels['HARD'].append(word) 
        
    return levels
    
def set_difficulty(levels):
    keys = levels.keys()
    level_set = False
    while not level_set:
        difficulty = input("Welcome to Mystery Word Challenge! Do you want an EASY, MODERATE or HARD word to guess? ").upper()
        level_set = difficulty in keys
    return difficulty

def find(word, letter):
    # loops through every letter in the word and compares it to the submitted letter. 
    # returns indexes for each occurance of the letter in the word.
    return [i for i, x in enumerate(word) if x == letter]



def prepare_game():
    words = word_list()
    levels = game_levels(words)
    difficulty = set_difficulty(levels)
    mystery_word = choice(levels[difficulty]) 
    return mystery_word


def run_game():
    mystery_word = prepare_game()
    guesses = 0
    wrong_guesses = []
    board = "_" * len(mystery_word)
    while guesses <= 10:
        letter = input('Guess a letter: ')
        if not letter.isalpha() and len(letter) != 1:
            print("Please submit a single letter.")
        elif board == mystery_word:
            print("you won!")
        else:
            guesses +=1
            if letter in mystery_word:
                index = mystery_word.index(letter) 
                board = list(board)
                matches = find()
                board[index] = letter 
                board = "".join(board) 
            else:
                wrong_guesses.append(letter)
                print(f"Wrong Guesses {wrong_guesses}")
            print(board)          
    else:
        print(f"You lose the word was {mystery_word}")
    

    
 
if __name__ == "__main__":
    
    run_game()
