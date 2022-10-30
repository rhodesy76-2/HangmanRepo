# %%
# Import random module
import random

# Word List to play with
# word_list = ["banana", "apple", "kiwi", "orange", "pear"]
# print(word_list)

# Takes word list and randomly chooses word


class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word =  random.choice(word_list)
        self.word_guessed = list
        self.num_letters = int
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        print(self.__dict__)
        
       
game_1 = Hangman(["banana", "apple", "kiwi", "orange", "pear"])    
        


# %%
