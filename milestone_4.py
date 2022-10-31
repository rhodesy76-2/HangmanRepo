# %%
# Import random module
import random

# escape in input as isalpha is called, how to recognize still?


class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word =  random.choice(word_list) # The word to be guessed, picked randomly from the word_list, using the random funcrtiun (imported at start of program)
        self.word_guessed = ["_" for i in self.word] # Takesr andom word, from self.word, create new list, guessed_word, replacing each letter in the word with a _ for each letter not guesssed
        self.num_letters = len(set(self.word)) # The number of UNIQUE letters in the word that have not been guessed yet, by using len on the set (unique letters) of the randown word
        self.num_lives = num_lives # The number of lives the player has at the start of the game, a default parameter and the value is set to 5.
        self.word_list = word_list # A list of words, set in init variable word_list
        self.list_of_guesses = [] # List of guesssed letters, set to empty initially
        print(self.__dict__)

            
               
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess {guess} is in the word.")
            for ind, char in enumerate(self.word):
                if char == guess:
                   self.word_guessed[ind] =  char
            self.num_letters -= 1
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
                self.list_of_guesses.append(guess)
                print(self.__dict__)
              
# argument of type 'NoneType' is not iterable error and also, keeps trying to take guesses?
        
       
game_1 = Hangman(["banana", "apple", "kiwi", "orange", "pear"])    
        
game_1.ask_for_input()

# %%
