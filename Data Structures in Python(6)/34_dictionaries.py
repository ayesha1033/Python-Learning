marks = {"harry": 32, "Jax": 22, "mannu": 21}

print(marks, type(marks))
print("The marks of Jax is",marks["Jax"])
marks["mannu"] = 100

print(marks.keys())
print(marks.values())

# marks.clear()

marks.pop("mannu")
print(marks)

student = {"name": "Alice", "age": 21, "grade": "A"}
# Accessing & Modifying Values:
print(student["name"])  # Output: Alice
student["age"] = 22     # Updating value
student["city"] = "New York"  # Adding new key-value pair

# Common Dictionary Methods:
print(student.keys())    # dict_keys(['name', 'age', 'grade', 'city'])
print(student.values())  # dict_values(['Alice', 22, 'A', 'New York'])
print(student.items())   # dict_items([('name', 'Alice'), ('age', 22), ...])

student.pop("age")  # Removes "age" key
student.clear()  # Empties dictionary

# Dictionary Comprehensions:
table_of_5 = {i: 5*i for i in range(1,11)}

print(table_of_5)

squares = {x: x**2 for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
