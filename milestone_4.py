# %%
# Import random module
import random

# escape in input as isalpha is called, how to recognize still?

# Creates the Hangman class
class Hangman():
    # initialises the class with the world list (needs to be externally set when you call the class), num of lives set to default 5
    def __init__(self, word_list, num_lives=5):
        # The word to be guessed, picked randomly from the word_list, using the random function (imported at start)
        self.word =  random.choice(word_list) 
        # Takes random word, from self.word, create new variable list, guessed_word, replacing each letter in the word with a _ for each letter not guesssed
        self.word_guessed = ["_" for i in self.word] 
        # Creates new variable stores the number of UNIQUE letters in the word that have not been guessed yet, by using getting the length (via len) on unique letters (use set to get unique letters only) of the randown word
        self.num_letters = len(set(self.word)) 
        # The number of lives the player has at the start of the game, a default parameter and the value is set to 5 in the initial variables.
        self.num_lives = num_lives 
        # A list of words, set in init variable word_list
        self.word_list = word_list 
        # New variable, a list of guesssed letters, set to empty initially
        self.list_of_guesses = [] 
        # Just checking how the variables change by printing dictionary
        print(self.__dict__)

    # check guess method, takes the guess as variable      
    def check_guess(self, guess): 
        # changes the input to lower case if upper
        guess = guess.lower()
        # if guess is in the word then:
        if guess in self.word: 
            # prints the letter is word
            print(f"Good guess {guess} is in the word.") 
            # for-loop that loops through each letter in the word. Used enumerate to split the random word into ia list of individual letter strings so the list can be itterated through
            for ind, char in enumerate(self.word): 
                # if charcater in the word is the same as the guessed letter
                if char == guess: 
                   # update the guessed word so that letter replaces the _
                   self.word_guessed[ind] =  char 
            # reduce the number of letters left to guess by 1
            self.num_letters -= 1 
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            # reduce the number of lives by 1
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
        # self.list_of_guesses.append(guess) was told to add but this already happens as part of the ask_input function as this would duplicate
            
    # ask_for_input uses as while true loop that takes the input and checks if the input is a single letter and alphabetical, otherwise loops back until these conditions are met
    def ask_for_input(self):
        #creates a while True loop 
        while True:
            # takes user input and assigns to guess variable
            guess = input("Please input a single letter")  
            # checks if the guess is not (False) a single (!=) aplhabet (isaplha)
            if len(guess) != 1 or guess.isalpha() == False: 
                print(f"{guess} is an invalid letter. Please, enter a single alphabetical character.")
            # checks if the guess has aldready been guesssed
            elif guess in self.list_of_guesses: 
                # prints that it has already been tried 
                print(f"You guessed {guess}, but you already tried that letter!")      
            # else/otherwise then run the following
            else:  
                # prints the guess
                print(f"You guesssed {guess}") 
                # Calls the check guess function with the single alphabetical guess
                self.check_guess(guess)
                # adds the guess to the end list of guesses (append)
                self.list_of_guesses.append(guess)
                # Just checking how the variables change by printing dictionary
                print(self.__dict__)
              

        
# sets up game 1 by calling the Hangman class and setting the word list variable for the class
game_1 = Hangman(["banana", "apple", "kiwi", "orange", "pear"])    

# Calls the ask_for_input method for game_1 to test the code       
game_1.ask_for_input()

# %%
