#String Formatting 
#String formatting is a powerful feature in Python that allows you to insert variables and expressions into strings in a structured way. Python provides multiple ways to format strings, including the older .format() method and the modern f-strings.
'''
# method 1: Using the .format() method

template = "Hello, {}. Take this {} $ bag."
a = "john"
a1 = 1000
b = "ana"
b1 = 300
c = "dimy"
c1= 0

s1 = template.format(a, a1)
print(s1)
'''
# method 1.2 
print("{1} is learning {0}".format("Python", "Alice"))  # Output: Alice is learning Python
print("{name} is {age} years old".format(name="Bob", age=25))



#  f-Strings
# print(f"hello, {b}. take this {b1} $ bag.")

name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

#Using Expressions in f-Strings
x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}")

#Formatting Numbers
pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")

#Padding and Alignment
text = "Python"
print(f"{text:>10}")  # Right align
print(f"{text:<10}")  # Left align
print(f"{text:^10}")  # Center align.0