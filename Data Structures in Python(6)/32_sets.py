s = {3,22,"apple",2}

print(s, type(s))

#print(s[3])
#In Python, an expression like s[3] or indexing a set is not applicable because sets are unordered collections that do not support position-based indexing or slicing

s.add(32)
print(s)

s.remove(22) # throws an error
print(s)

s.discard(0) # No error if element not found
# No error if element not found

s.discard(22)
print(s)

s.pop() # Removes random element
print(s)

