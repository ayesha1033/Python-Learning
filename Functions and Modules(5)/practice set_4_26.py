# 1. Defining Functions
# Write a function greet() that prints "Hello, Python Learner!" when called.

def greet():
    print("Hello, Python Learner!")
    
    # string = "Hello, Python Learner!"
    # return string  # when this way called by usim=ng print 
    
    # { print(greet()) }
   

greet()

# Write a function square(num) that returns the square of a given number. Test it with different numbers.

def square(a,b):
    c = a+b
    return c

print(square(3,3))
print(square(0,3))
print(square(31,3))

# 2. Function Arguments & Return Values

# Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".

def full_name(first, last):
    return f"{first} {last}"

print(full_name("John","Doe"))

# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
# Both length and width
# Only length (use default width)

def calculate_area(length, width=10):
    return length * width

print(calculate_area(13,2))
print(calculate_area(13))

# 3. Lambda Functions
# Write a lambda function that adds two numbers and test it.

add = lambda a, b:a + b

print(add(3,5))

# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.
square = lambda x: x*x
list1 = [1, 2, 3, 4, 5]

print(list(map(square, list1)))

# 4. Recursion in Python
# Write a recursive function factorial(n) that returns the factorial of a number.

def factorial(n):
    if n==0 or n==1:
        return 1
    return factorial(n-1)*n

print(factorial(0))
print(factorial(3))
print(factorial(10))

# Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.

def sum_of_digits(n):
    if n == 0:
        return 0
    return n%10 + sum_of_digits(n//10)

print(sum_of_digits(7532))
# sum of digits of 7532 is same as:
# 2(last digit) + sum of digit of 753
# 2+(7+5+3)=17


# 5. Modules and Pip – Using External Libraries
# Import the math module and use it to:
  # Find the square root of 144
  # Calculate sin(90°) (hint: use math.radians())
  
import math

a = math.sqrt(144)
b = math.sin(math.radians(90))
print(a," \n",b)


# Install and import the requests module (if available) and use it to fetch data from "https://api.github.com".

import requests #pip install requests

a = requests.get("https://api.github.com")
print(a.json())

# 6. Variable Scope and Docstrings
# Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.

def increment():
    counter = 0
    counter +=1
    print(counter)
    
increment()
increment()
increment()
    

# Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.

def multiply(a, b):
    '''multiplying
    parameter: a
    parameter: b
    return : a*b
    '''
    return a * b

print(multiply(2,4))
print(multiply(4,4))
help(multiply)

# 7. Bonus Challenges
# Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.

def fib(n):
     #Base case of recursion
    if(n ==0 or n==1):
        return n
    
    return fib(n-2)+fib(n-1)
print(fib(9))
print(fib(6))

# Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.

def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    c = a / b
    return c
    
print(safe_divide(6,3))
print(safe_divide(9,0))

#Q3 of bonus Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.
#27 index separetly


    
    
