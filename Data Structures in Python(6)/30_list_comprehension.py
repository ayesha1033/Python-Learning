# Create a list containing the table of 5
'''
a = 5
table = []

for i in range(1,11):
    table.append(a*i)
    
print(table)

'''

#  Create a list containing the table of 5 using List Comprehensions (Efficient List Creation)

table = [5*i for i in range (1,11)]

print(table)


squared = [x**2 for x in range(5)]
print(squared)  # Output: [0, 1, 4, 9, 16]