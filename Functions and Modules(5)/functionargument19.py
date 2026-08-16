# Types of Arguments:
#1. Positional Arguments
def add(a,b):
    x = a + b
    return x

c = add(3,2)
print(c)

#2. Default Arguments
#ex1
def add1(a, b, plus=0):
    x = a + b + plus
    return x

c = add1(3, 5, 2)
print(c)
#ex2
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!

#3. Keyword Arguments
#ex1
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=20, name="Bob")

#ex2
def add1(a, b, plus=0):
    x = a + b + plus
    return x

c = add1(b=4, plus=5, a=2)
print(c)