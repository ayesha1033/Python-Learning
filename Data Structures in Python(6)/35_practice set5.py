# 1. Introduction to Lists
# Create a list fruits = ["apple", "banana", "cherry"].
  # Print the first fruit.
  # Replace "banana" with "orange".
  # Print the length of the list.
  
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits[1] = "orange"
print(len(fruits))
print(fruits)
  
# Create a list of numbers from 1 to 10.
   # Print the first three numbers using slicing.
   # Print the last three numbers using slicing.
   
list1 = [ i for i in range(1,11)]

print(list1)
print(list1[0:3])
print(list1[-3::])

# 2. List Methods
# Start with numbers = [5, 2, 9, 1, 7] and do the following:
  # Sort the list in ascending order.
  # Append the number 10 to the list.
  # Remove the number 2 from the list.

numbers = [5, 2, 9, 1, 7]

numbers.sort()
print(numbers)
numbers.append(10)
numbers.remove(2)

# Create a list names = ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1.

names = ["Alice", "Bob", "Charlie"]

names.insert(1,"David")
print(names)

# 3. Tuples and Operations on Tuples
# Create a tuple coordinates = (10, 20) and print both elements.
# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.

coordinates = (10, 20)
print(coordinates[0])
print(coordinates[1])

# coordinates[0] = 50  # 'tuple' object does not support item assignment

corlist = list(coordinates)
corlist[0] = 50
coordinates = tuple(corlist)
print(coordinates)


# 4. Sets and Set Methods
# Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)

my_set = {1, 2, 3, 3, 4} 
print(my_set)
"""3 is only printed once,because a set can't have duplicate elements."""

# Add 5 to the set, remove 2, and check if 4 is in the set.

my_set.add(5)
my_set.remove(2)
print(my_set)

# Create two sets:
  # a = {1, 2, 3}
  # b = {3, 4, 5}
  # Find their:
     # Union
     # Intersection
     # Difference (a - b)
     
a = {1, 2, 3}
b = {3, 4, 5}   

union = a.union(b)
intersection = a.intersection(b)
difference = a.difference(b)

print(union, intersection, difference)
     
# 5. Dictionaries and Dictionary Methods

# Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:
  # Print the value of "name".
  # Change "grade" to "A+".
  # Add a new key "city" with value "Delhi".
  
student = {"name": "John", "age": 20, "grade": "A"}  
  
  
# Create a dictionary of three friends and their phone numbers. Use:
   # keys() to get all names
   # values() to get all numbers
   # items() to loop over key-value pairs and print them.
   
   
# 6. Bonus Challenges

# Write a program that takes a list of numbers and removes all duplicates using a set.


# Given a dictionary of products and their prices, find the product with the highest price.


# Write a program that merges two dictionaries into one.