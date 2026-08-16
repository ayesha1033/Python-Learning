#1.Creating Strings
"""
 # Single-quoted string
a = 'Hello, Python!'

# Double-quoted string
b = "Hello, World!"

# Triple-quoted string (useful for multi-line strings)
c = '''This is
a multi-line
string.'''

"""

#2. String Indexing

name = "Aish"
# name = "A  i  s  h"
#         0  1  2  3 
#        -4 -3 -2 -1
print("Now forwards indexing")

print(name[0]) #output: A
print(name[1]) #output: i
print(name[2]) #output: s
print(name[3]) #output: h

print("Now backwards indexing")

print(name[-1]) #output: h  name[-1+4] = name[3]
print(name[-2]) #output: s  name[-2+4] = name[2]
print(name[-3]) #output: i  name[-3+4] = name[1]
print(name[-4]) #output: A  name[-4+4] = name[0]
