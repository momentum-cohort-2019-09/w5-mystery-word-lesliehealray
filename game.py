from collections import defaultdict
from random import choice



def word_list():
    with open("words.txt") as file_handler:
        words = file_handler.read().split()
    return words
    

def game_levels(words):
    levels = defaultdict(list)
    for word in words:
        word = word.lower()
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
    # returns a list of indexes for each occurance of the letter in the word.
    return [i for i, letter_in_word in enumerate(word) if letter_in_word == letter]
    



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
        letter = input('Guess a letter: ').lower()
        if not letter.isalpha() and len(letter) != 1:
            print("Please submit a single letter.")
        else:
            guesses +=1
            # find returns either an emptylist or a list of index(es) 
            matches = find(mystery_word, letter)
            # python empty lists evaluates to false. For index in matches will only run if there is an index and won't execute if an empty list.
            for index in  matches:
                # convert board to a list
                board = list(board)
                board[index] = letter 
                board = "".join(board) 
            if board == mystery_word:
                print("you won!")
                exit()
            if not matches:            
                wrong_guesses.append(letter)
                print(f"Wrong Guesses {wrong_guesses}")
            
            print(board)          
    else:
        print(f"You lose the word was {mystery_word}")
    

    
 
if __name__ == "__main__":
    
    run_game()
