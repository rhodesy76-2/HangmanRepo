
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
