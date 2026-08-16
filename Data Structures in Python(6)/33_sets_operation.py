a = {3,11,23}
b = {2,33,4,11}
 
c = a.union(b)  # contain all the elements in [a] along with all the elements in [b]
print(c)
 
d = a.intersection(b) # contains only the elements that are present in [a] as well as [b]
print(d)

e = a.difference(b) #  typically represents a set difference operation in programming, meaning it finds elements in set a that are not present in set 
print(e)

f = b.difference(a)
print(f)