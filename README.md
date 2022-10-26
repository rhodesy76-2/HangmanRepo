# Hangman milestone_2
Milestone 2 dealt  with importing the random function, creating a list of fruits and then calling one of the fruits using the random function. I then created a statement that checks that only one letter is input and that it is an alphabet. Finally I pulled the lasts steps together using a while loop with a break so that an input would only be accepted if a sinle letter was input.

## Usage
```python
# import random function. Note: To import a module, you have to use the import keyword at the top of the file.

import random


# Step 1. Created a list containing the names of 5 of my favorite fruits.
# Step 2. Assigned this list to a variable called word_list
# Step 3. Print out the newly created list to the standard output (screen).

word_list = ["banana", "apple", "kiwi", "orange", "pear"]
print(word_list)


# Step 4: Creates the random.choice method and passes the word_list variable into the choice method.
# Step 5: Assign the randomly generated word to a variable called word.
# Step 6: Print out word to the standard output. Run the code several times and observe the words printed out after each run.

word = random.choice(word_list)
print(word)


# Step 7. Using the input function, ask the user to enter a single letter.
# Step 8. Assign the input to a variable called guess.

guess=input("Please input a single letter")
print(guess)


# Step 9. Created an if statement that checks if the length (lens) of the input is equal to 1 and the input is an alphabet (isalpha).
# Step 10: In the body of the if statement, prints a message that says "Good guess!".
# Step 11: Created an else block that prints "Oops! That is not a valid input." if the preceeding conditions are not met.

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else :
    print("Oops! That is not a valid input.")


# Step 12 (extra): Combined above into a check letter while loop until only a single alphabetic letter is input

while True:
    guess = input("Please input a single letter")
    print(guess)
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
        break
    else :
        print("Oops! That is not a valid input.")
```
# Hangman milestone_3
Milestone_3 dealt with checking if the guessed letter is in the radonly chosen word

## Usage
```python

# %%
# Import random module
import random



# Word List to play with
word_list = ["banana", "apple", "kiwi", "orange", "pear"]
print(word_list)

# Takes word list and randomly chooses word
word = random.choice(word_list)
print(word)
# Takes word list and randomly chooses word

# Step 1. Created a while loop and set the condition to True. 
# Setting the condition to True ensures that the code run continuously. In the body of the loop, 
while True:
# Step 2: Asked the user to guess a letter and assign this to a variable called guess.
    guess = input("Please input a single letter")
    # print(guess)
# Step 3. Checked that the guess is a single, alphabetical character.
    if len(guess) == 1 and guess.isalpha():
# Added line to shgow user guess
        print(f"You guesssed {guess}")
# Step 4. If the guess passes the checks, broke out of the loop.
        break
# Step 5: If the guess does not pass the checks, print a message saying "Invalid letter. Please, enter a single alphabetical character."
    else :
        print("Invalid letter. Please, enter a single alphabetical character.")





# %%
# Step 6. Created an if statement that checks if the guess is in the word.
if guess in word:
# Step 7 Prints a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.
    print(f"Good guess {guess} is in the word.")

 # Step 3. Created an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.
else:
    print(f"Sorry, {guess} is not in the word. Try again.")

# %%
# Pulling the above into two functions, check_guess and ask_for_input, so it is easier to see what is what
# guess and 

# Import random module
import random

# Word List to play with
word_list = ["banana", "apple", "kiwi", "orange", "pear"]
print(word_list)

# Takes word list and randomly chooses word
word = random.choice(word_list)
print(word)


# check_guess takes the guessed letter as an argument and check if the letter is in the word
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# ask_for_input uses as while true loop that takes the input and checks if the input is a single letter and alphabetical, otherwise loops back until these conditions are met
def ask_for_input():
    while True:
        guess = input("Please input a single letter")
        if len(guess) == 1 and guess.isalpha():
            print(f"You guesssed {guess}")
            break 
        else:
            print(f"{guess} is an invalid letter. Please, enter a single alphabetical character.")
    # Calls the check guess function with the single alphabetical guess
    check_guess(guess)


ask_for_input()

    
# %%
