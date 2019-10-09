from collections import defaultdict
import random


def mystery_word(filename):
    with open("words.txt") as file_handler:
        words = file_handler.read().split()
        #remove regex?
    return words
    

def game_level(words):
    mode = defaultdict(list)
    for word in words:
        if len(word) <= 6:
            mode['EASY'].append(word)
        elif 8 > len(word) > 6:
            mode['MODERATE'].append(word)
        else:
            mode['HARD'].append(word) 
    return mode 

   
def begin_game():
    get_level = raw_input("Welcome to Mystery Word Challenge! Do you want an EASY, MODERATE or HARD word to guess?")
    requested _level = get_level.upper()
    if requested_level == "EASY" or "MODERATE" or "HARD":
        pick_word()
    elif not requested_level:
        return get_level
    else print("Please choose EASY, MODERATE or HARD")




def pick_word(mode):

    secret_word = random.choice.get(level)












 
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Guess the mystery word.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        words = mystery_word(file)
        words_by_difficulty = game_level(words)
    else:
        print(f"{file} does not exist!")
        exit(1)
