#1. Basic String Operations

#Create a string variable name with your full name. Print:
# The first character
# The last character
# The length of the string

from importlib import abc


name = "Ayesha Jamil"
print(name[0])
print(name[-1])
print(len(name))

#Concatenate two strings: "Hello" and "World" with a space in between.

str1 = "Hello"
str2 = "World"

print(str1 + " " + str2)
print(str1,str2)

# 2. String Slicing and Indexing
# Given text = "Python Programming", do the following:
    # Print the first 6 characters
    # Print the last 6 characters
    # Print every second character from the string
    
text = "Python Programming"
print(text[0:6])
print(text[-6:])
print(text[::2])

# Reverse the string text using slicing.

print(text[::-1])

# 3. String Methods and Functions
  # Take the string "  i love python programming  " and:
  
  # Remove extra spaces from both ends
  # Convert it to title case
  # Count how many times "o" appears

text = "  i love python programming  "
print(text.strip())
print(text.title())
print(text.count("o"))

# Check if the string "123abc" is alphanumeric.

text = "123abc"
print(text.isalnum())

if text.isalnum():
    print("yes,the string is alphanumeric")
else:
    print("no,the string is not alphanumeric")
    
# 4. String Formatting and f-Strings

# Using format(), create a sentence:
# "My name is John and I am 25 years old."
# by passing "John" and 25 as variables.

print("My name is {} and I am {} years old.".format("John", 25))

# Do the same using f-strings.
print(f"My name is John and I am 25 years old.")


# 5. String Manipulation Challenges

# Given sentence = "Coding in Python is fun", replace "fun" with "awesome" and print it.
sentence = "Coding in Python is fun"
print(sentence.replace("fun", "awesome"))

# Find the index of the word "Python" in sentence.

print(sentence.index("Python"))

# Convert the entire sentence to uppercase and print it.

print(sentence.upper())

# 6. Bonus Questions
# Write a program that counts how many vowels are in a given string.

string = "Coding in Python is fun and funny"
sum = 0
vowels = ['a','e','i','o','u']
for char in string.lower():
    if(char in vowels):
        sum +=1 
print(f"There are {sum} vowels in this sentence")

# Take a user input string and check if it is a palindrome (same forwards and backwards). 
#solved separately.


 
