#Creating a Tuple:

a = (3,4,5,66,7)

print(a)
print(a[2])
# a[3] = 32 #'tuple' object does not support item assignment or Tuples are ordered but immutable collections (cannot be changed after creation).


single_element = (5,)  # Tuple with one element (comma required)

# Tuple Unpacking:

x, y, z, w, v = a

print(x, y, z, w, v, y)


# tuple method 

t = (30,44,50,669,457,44,44,44)

print(t.count(44))
print(t.index(44))
print(t.index(50))

print(t, type(t))


