
# %%

print("This print statement was created in Python")

# %%
# Void Functions
# A function that doesn't return anything is called a void function. In Python, you can define a void function by simply not including a return statement.

def void_fuction():
    print("This is a void function")
void_result = void_fuction() 
print(void_result)
# %%
# Range checker 
def in_range(lower_bound, upper_bound, number):
    if number >= lower_bound and number <= upper_bound:
        print(f"{number} is between {lower_bound} and {upper_bound}.")
    else:
        print(f"{number} is NOT between {lower_bound} and {upper_bound}.")

in_range(3,5,4)
in_range(3,5,6)
# %%
# Volume of as sphere
pi = 3.14
def volume_of_sphere(radius):
    V = 4/3 * pi * radius ** 3
    print(V)
volume_of_sphere(4)


# %%
# beefier version of above
# import pi from math
from cgitb import reset
from math import factorial, pi
from typing_extensions import Self
from unicodedata import name
from xml.dom import ValidationErr 
# function to calculate volume
def volume(r): 
    return (4 * pi * r ** 3) / 3 
# take a user entered input and output pi
r = float(input("Input the radius: ")) 
print(f"Volume: {volume(r)}") 

# %%
# %%
# Come up with your own functiosn practical
# Write a program to print fibonacci series upto n terms in python
def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fib(20)



# %%
def fun_dummy(*args, **kwargs):  # args = arguments, kwargs = key word arguments
    print(args)  # args is now a tuple
    print(kwargs)  # kwargs is now a dictionary


fun_dummy(1, 2, e=4, d=4, c=6, e=5)
# %%

# Create a function which takes in a dictionary of attributes about a piece of clothing and prints each of the key-value pairs on a line
# def clothing_function(item, size, colour):
def clothing_function(*args, **kwargs):
    print(args)
    print(kwargs)
        

clothing_function(1, 2, 34, item="tshirt", size="large", colour="red")

# %%
def clothing_function(attributes_to_print='all'):
    print(args)
    print(kwargs)
        

clothing_function(1, 2, 34, item="tshirt", size="large", colour="red"
# %%

def clothing_function(attributes_to_print=all):

      for key in clothing_function:
        print("key:", key, "Value:", attributes_to_print[key])

attributes_to_print{"item": "tshirt", "size": "large", "colour": "red"}

# %%
def func(d):
      
    for key in d:
        print("key:", key, "Value:", d[key])
          
# Driver's code
D = {'a':1, 'b':2, 'c':3}
func(D)
# %%
class Employee(object):
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

e = Employee({"name": "abc", "age": 32})
# %%
cloth_dictionary= {"item": "tshirt", "size": "large", "colour": "red"}
attributes_to_print=["item", "colour"]
attributes_to_print_2=["size"]
def clothing_function(list_of_items: list):
    for key, value in cloth_dictionary.items():
        if key in list_of_items: 
            print(f'{key}: {value}')
        else:
            print("key doesn't exist")
    

clothing_function(attributes_to_print)
print(" ")
clothing_function(attributes_to_print_2)
print(" ")
clothing_function(["item"])
# %%
# Profile valiadation possible demo/ example code
o="hai$"
import re
if(bool(re.match('^[a-zA-Z0-9]*$',o))==True):
    print("valid")
else:
    print("invalid")

# %%
# See how tom check does not have !@£$%^&*()
# Profile valiadation possible demo/ example code
import re
def new_user():
    while True:
        name = input("Please input your name")
        if(bool(re.match('^[a-zA-Z0-9]*$', name))):
            print(f"You input {name}")
            return
        else:
            print("Please enter without !@£$%^&*() ")
# the  age and email parts

new_user()
# %%
# Profile valiadation possible demo/ example code
def user_name():
    while True:
        name = input("Please input your name")
        characters_not_wanted = ["!", "@", "£", "$", "%", "^", "&", "*", "(", ")"]
        for mystr in name:
            if all(x not in mystr or x in characters_not_wanted):
                print(f"You input {name}")
                return 
            else:
                print("Please enter without !@£$%^&*() ")


user_name()
# %%
# Profile valiadation possible demo/ example code
name = input("Please input your name")
characters_not_wanted = ["!", "@", "£", "$", "%", "^", "&", "*", "(", ")"]
for mystr in name:
    if all(x not in mystr for x in characters_not_wanted):
        print(f"You input {mystr}")
    else:
        print("Please enter without !@£$%^&*() ")

# %%
# Profile valiadation possible demo/ example code
mystring = ["reddit", "google"]
mylist = ["a", "b", "c", "d"]
for mystr in mystring:
  if all(x not in mystr for x in mylist):
    print(mystr)
# %%
# Profile valiadation possible demo/ example code
list = ['admin', 'add', 'swear']
st = 'siteadmin'
if any([x in st for x in list]):
    print("found")
else: 
    print("not found")
# %%
checked_name =''
def user_name():
    while True:     
        characters_not_wanted = ["!", "@", "£", "$", "%", "^", "&", "*", "(", ")"]
        name = input("Please input your name")
        if any([x in name for x in characters_not_wanted]):
            print("Please enter without !@£$%^&*() ")
        else: 
            print(f"You input {name}")
            global checked_name
            checked_name = name
            return 

user_name()

print(checked_name)
# %%

# %%

# Check the name does not contain any of the following characters "!@£$%^&*()"
# Check the email is valid by making sure it contains "@"
# Check the age > 12
# Turn each step above into a function, so that you have one function, whiich calls 3 other functions inside
# Print a friendly error to explain the issue to the user if any of these checks does not pass


class NewProfile:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

    def check_user_name(self):
        while True:   
            characters_not_wanted = ["!", "@", "£", "$", "%", "^", "&", "*", "(", ")"]
            name = input("Please input your name")
            if any([x in name for x in characters_not_wanted]):
                print("Please enter without !@£$%^&*() ")
            else: 
                print(f"Your name is {name}")
                return 

    def check_input_age(self):
        while True: 
            age = input("Please input your age in years")
            if age.isnumeric():
                print(f"Your age is {age}")
                if int(age) > 12:
                    print("You are older than 12")
                else:
                    print("You are not old enough to set up an account")
                    break
                return
            else:
                print("Please enter a number only")

    def check_email(self):
       while True:   
            check_email_condition = ["@"]
            email = input("Please input your email")
            if any([x in email for x in check_email_condition]):
                print(f"Your email is {email}")
                return
            else: 
                print("Please ensure you have input an email address including @")
                
                

            
new_user = NewProfile("","","")



new_user.check_user_name()
new_user.check_input_age()
new_user.check_email()


# %%
# rather than using a class just simplified as per the question, so that you have one function, which calls 3 other functions inside 
def new_profile():
    def check_user_name():
        while True:   
            characters_not_wanted = ["!", "@", "£", "$", "%", "^", "&", "*", "(", ")"]
            name = input("Please input your name")
            if any([x in name for x in characters_not_wanted]):
                print("Please enter without !@£$%^&*() ")
            else: 
                print(f"Your name is {name}")
                return 
    check_user_name()

    def check_input_age():
        while True: 
            age = input("Please input your age in years")
            if age.isnumeric():
                print(f"Your age is {age}")
                if int(age) > 12:
                    print("You are older than 12")
                else:
                    print("You are not old enough to set up an account")
                    # break
                return
            else:
                print("Please enter a number only")
    check_input_age()

    def check_email():
       while True:   
            check_email_condition = ["@"]
            email = input("Please input your email")
            if any([x in email for x in check_email_condition]):
                print(f"Your email is {email}")
                return
            else: 
                print("Please ensure you have input an email address including @")
    check_email()

new_profile()
# %%
# A recursive function is a function that calls itself. This is useful when you want to perform an operation on a number and all the numbers below it.
# Define a recursive function called factorial that returns the factorial of a given number.
# Define a function called factorial that takes in a number
# If the number is 0, return 1
# Otherwise, return the number multiplied by the factorial of the number minus 1. In this case, you have to call the function again inside itself.
# Call your function to test it. Use the number 5 as an input, you should get 120 as an output.

def factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*factorial(n-1)  
# take input from the user  
num = int(input("Enter a number: "))  
# check is the number is negative  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",factorial(num))  

# %%

# simple version but doesnt handle negative, added assert
def factorial(n):
    assert n>=0
    if n == 0:
        return [1]
    last = factorial(n-1)
    return [n * last[-1]]

factorial(5)

# %%

# Recursive using a main function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
        
def main():
    num = int(input("Enter number: "))
    if num < 0:  
        print("Sorry, factorial does not exist for negative numbers")  
    else:
        print("The factorial of",num,"is",factorial(num))  
main()

# %%
# Write a recursive function to print fibonacci series upto n terms in python

def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# Call
 
print(Fibonacci(10))

# %%
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
# take input from the user.
nterms = int(input("To what term? "))  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur_fibo(i))  
# %%
# Write a for loop that prints the first 100 Fibonnaci numbers
# Create a function which returns True if the number is a multiple of 7 and False otherwise
# Call this function on each number inside your loop
# Add an elif condition to the loop to call another new function which checks if the number is greater than or equal to 100 OR is less than 50. In the case that it is True, format a string that prints the number and either "is larger than 100" or "is less than 50".
# build on the bellow I used above?
def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
        multiple_seven(a)
    else:
        print(a)
        multiple_seven(a)
        print(b)
        multiple_seven(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
            multiple_seven(c)
            
            

# fib(100)

def multiple_seven(p):
    if p == 0:
        print("False. This number is not a multiple of 7")
    elif p % 7 == 0:
        print("True. This number is a multiple of 7")  
    else :
        print("False. This number is not a multiple of 7")
        
        
# multiple_seven(5)      
fib(100)
# %%
