a = "Ayesha" # strings are immutable, so we cannot change the value of a string by using indexing. We can only access the characters of a string using indexing.

# name[0] = "y" # You cannot do this

l = len(a)

# Common String Methods
# Changing Case

# print(l) # output: 6
# print(a.upper(), a)
# print(a.lower(), a)
# print(a.capitalize(), a)
# print(a.title(), a)

#Removing Whitespace

# text = " hello world "
# print(text)
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

#Finding and Replacing

# text = "I love L.J Shein"
# print(text.find("Shein")) # output: 11
# print(text.replace("L.J Shein", "L.J author")) # output: I love L.J author

# Splitting and Joining
"""
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']

new_text = " - ".join(fruits)
print(new_text)  # Output: "apple - banana - orange"

"""

# Checking String Properties

"""
text = "Python123"
print(text.isalpha())  # Output: False,alpha means alphabet
print(text.isdigit())  # Output: False,digit means number
print(text.isalnum())  # Output: True,almum means alphabet and number
print(text.isspace())  # Output: False,space means whitespace

"""



