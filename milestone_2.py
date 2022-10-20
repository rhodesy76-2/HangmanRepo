#%%
# Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.
import random



# Step 1. Create a list containing the names of your 5 favorite fruits.
# Step 2. Assign this list to a variable called word_list
# Step 3. Print out the newly created list to the standard output (screen).

#%%
word_list = ["banana", "apple", "kiwi", "orange", "pear"]
print(word_list)


# %%
# Step 3: Create the random.choice method and pass the word_list variable into the choice method.
# Step 4: Assign the randomly generated word to a variable called word.
# Step 5: Print out word to the standard output. Run the code several times and observe the words printed out after each run.

word = random.choice(word_list)
print(word)


# %%
# Step 1. Using the input function, ask the user to enter a single letter.
# Step 2. Assign the input to a variable called guess.
guess=input("Please input a single letter")
print(guess)
# %%
# Step 1. Create an if statement that checks if the length (lens) of the input is equal to 1 and the input is an alphabet (isalpha).
# Step 2: In the body of the if statement, print a message that says "Good guess!".
# Step 3: Create an else block that prints "Oops! That is not a valid input." if the preceeding conditions are not met.

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else :
    print("Oops! That is not a valid input.")
# %%

# Combined above into a check letter while loop until only a single alphabetic letter is input
while True:
    guess = input("Please input a single letter")
    print(guess)
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
        break
    else :
        print("Oops! That is not a valid input.")
# %%


