# Hangman milestone_1
Milestone 1 dealt  with importing the random function, creating a list of fruits and then calling one of the fruits using the random function. I then created a statement that checks that only one letter is input and that it is an alphabet. Finally I pulled the lasts steps together using a while loop with a break so that an input would only be accepted if a sinle letter was input.

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


# Step 9. Creates an if statement that checks if the length (lens) of the input is equal to 1 and the input is an alphabet (isalpha).
# Step 10: In the body of the if statement, prints a message that says "Good guess!".
# Step 11: Creates an else block that prints "Oops! That is not a valid input." if the preceeding conditions are not met.

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

