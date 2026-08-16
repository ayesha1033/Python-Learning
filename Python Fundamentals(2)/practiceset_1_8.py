#Q1Write a program that prints: Hello, World! Welcome to Python.

print("Hello, World! Welcome to Python.")

#Q2Write a program that prints the following poem using a single print() statement:
# (Hint: Use \n for a new line.)
# Twinkle, twinkle, little star,
# How I wonder what you are!

print("Twinkle, twinkle, little star,", '\nHow I wonder what you are!') 

print("Twinkle, twinkle, little star, \nHow I wonder what you are!")

print("""Twinkle, twinkle, little star,
How I wonder what you are!""")

#Q3 Create variables to store:

# Your name (string)
# Your age (integer)
# Your height in meters (float)
# A boolean value representing whether you are a student
# Print all of them in one line.

A = "Ayesha"
B = 20
C = 5.5
D = True

print(A,B,C,D, sep ="," ,end =".") 

print("\nThe name of the student is "+ A + ".she is " + str(B) + " years old." + "She is " + str(C) + " inches tall." + "student:" + str(D))

# Q4 You are given a string:

# num = "45"
# Convert it into an integer
# Add 10 to it
# Print the result

num ="45"

# str_num = int(num)
# print(str_num+10)

print(int(num)+10)


# Q5: Taking User Input
# Write a program that:

# Asks the user for their favorite food.
# Prints:
# Wow! I also like <food>. 

FOOD = input("What is your favorite food? ")

print("Wow! I also like " + FOOD+".")

#Q6 done separately in simplecalculator8.py

# Q7: Escape Sequences
# Print the following output using escape sequences:

# Hello "Python" World!
# This is on a new line.
# This is a tab →	    after tab.

print('Hello "Python" World!\nThis is on a new line.\nThis is a tab -> \t <- here.')

#Q8: Operator Challenge (already done in sq&cube8.py)
# Write a program that:
# Takes an integer as input from the user.
# Prints the square and cube of that number. 

# Q9: Quick Quiz (True/False)
# Mark True or False:
# Python code must always end with a semicolon ; . false
# The # symbol is used for comments in Python. true
# "123" and 123 are the same in Python.  false
# The * operator is used for multiplication. true
# \n creates a new line.  true
# Variables in Python can start with numbers.  false
# int("10") + 5 gives 15  true