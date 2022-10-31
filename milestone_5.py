# %%
# Import random module
import random
# Imported exit from sys so I could terminate my game when No selected in play_again method
from sys import exit
# escape in input as isalpha is called, how to recognize still?

# Creates the Hangman class
class Hangman():
    # Initialises the class with the world list (needs to be externally set when you call the class), num of lives set to default 5
    def __init__(self, word_list, num_lives):
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
        # Just checking how the variables change by printing dictionary for testing, edited out
        # print(self.__dict__)

    # Method to check guess, takes the guess as variable      
    def check_guess(self, guess): 
        # Changes the input to lower case if upper
        guess = guess.lower()
        # If guess is in the word then:
        if guess in self.word: 
            # Prints the letter is word
            print(f"Good guess {guess} is in the word.") 
            # For loop that loops through each letter in the word. Used enumerate to split the random word into ia list of individual letter strings so the list can be itterated through
            for ind, char in enumerate(self.word): 
                # IF charcater in the word is the same as the guessed letter
                if char == guess: 
                   # Update the guessed word so that letter replaces the _
                   self.word_guessed[ind] =  char 
                   print(self.word_guessed)
            # Reduces the number of letters left to guess by 1
            self.num_letters -= 1 
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            # Reduces the number of lives by 1
            self.num_lives -= 1
            # Added in pictorial of hangman for numner of lives 0-4
            if self.num_lives == 4:
                print("   _____ \n"
                      "  |     | \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")   
            elif self.num_lives == 3:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif self.num_lives == 2:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")         

            elif self.num_lives  == 1:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            elif self.num_lives  == 0:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__\n")
            print(f"You have {self.num_lives} lives left.")
            print(self.word_guessed)
                
                
        # self.list_of_guesses.append(guess) was told to add but this already happens as part of the ask_input function as this would duplicate
            
    # Defines the ask of input method, ask_for_input, uses as while true loop that takes the input and checks if the input is a single letter and alphabetical, otherwise loops back until these conditions are met
    def ask_for_input(self):
        # Added in pictorial of hangman for numner of lives 5
        if self.num_lives == 5:
                print(
                     "   _____ \n"
                     "  |      \n"
                     "  |      \n"
                     "  |      \n"
                     "  |      \n"
                     "  |      \n"
                     "  |      \n"
                     "__|__\n")
                print(self.word_guessed)
        # Created a while True loop  to check user input o
        while True:
            # Takes user input and assigns to guess variable
            guess = input("Please input a single alphabetic letter: ")  
            # Checks if the guess is not (False) a single (!=) aplhabet (isaplha)
            # TODO Could add a condition to check if escape pressed 
            if len(guess) != 1 or guess.isalpha() == False: 
                print(f"{guess} is an invalid letter. Please, enter a single alphabetical character.")
            # Checks if the guess has aldready been guesssed
            elif guess in self.list_of_guesses: 
                # Prints that it has already been tried 
                print(f"You guessed {guess}, but you already tried that letter!")      
            # Else then run the following
            else:  
                # Prints the guess
                print(f"You guesssed {guess}")            
                # Calls the check guess function with the single alphabetical guess
                self.check_guess(guess)
                # Adds the guess to the end list of guesses (append)
                self.list_of_guesses.append(guess)
                # Just checking how the variables change by printing dictionary for testing, edited out
                # print(self.__dict__)
                break
    
    # Defined a simple play again method. Could improve by checking if other letters input, if just one letter etc. Does accept upper and lower case
    def play_again(self):
        while True:
            yes_no_input = input("Do you want to play again y/n?: ")
            # If Y used is set to y using .lower()
            yes_no_input = yes_no_input.lower()
            # TODO Not using next bit as had issues recognosing y or n. Can expand later
            # if len(yes_no_input) != 1 or yes_no_input != ("n" or "y"): 
             #   print(f"{yes_no_input} is an invalid input. Please enter y or n only.")
            
            # If input = y run the playgame with a new word. Checked the new word is random
            if yes_no_input == "y":
                print("You chose to play again")
                play_game(self.word_list)
            else:
                print("Game closed")
                # Called Exit from sys at top of page, implemented here to terminate the loop, as break still continued the play_game method and created an unwanted loop
                exit()
                
         
    
# Method to run the game                
def play_game(word_list):
        # Creates an instance of Hanman, taking variables of the word list and num_lives default value set to 5; important stays 5 as otheriwse graphics dont work as only 5 drawings
        game = Hangman(word_list, num_lives=5) 
        # while true loop 
        while True:
            # If number of lives equals 0 
            if game.num_lives == 0:
                print('You lost!')
                print(f"The word was '{game.word}'")
                # Calls the play again function
                game.play_again()
                # Break removed as added play again feature
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print('Congratulations. You won the game!')
                # Calls the play again method
                game.play_again()
                # Break removed as added play again feature
        
# Calls the play_game function to play your game.
play_game(["banana", "apple", "kiwi", "orange", "pear"])
# %%


# %%
