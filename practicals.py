
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
from math import pi 
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
