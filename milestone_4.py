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
        
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            
    # ask_for_input uses as while true loop that takes the input and checks if the input is a single letter and alphabetical, otherwise loops back until these conditions are met
    def ask_for_input(self):
        while True:
            guess = input("Please input a single letter")
            if len(guess) != 1 or guess.isalpha() == False:
                print(f"{guess} is an invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"You guessed {guess}, but you already tried that letter!")      
            else: 
                print(f"You guesssed {guess}")
                # Calls the check guess function with the single alphabetical guess
                self.check_guess(guess)
                self.list_of_guesses = (self.list_of_guesses).append(guess)
                print(self.__dict__)
              
# argument of type 'NoneType' is not iterable error and also, keeps trying to take guesses?
        
       
game_1 = Hangman(["banana", "apple", "kiwi", "orange", "pear"])    
        
game_1.ask_for_input()

# %%
