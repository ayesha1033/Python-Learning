def sum(a,b):
    print("addition occuring")
    c = a+b
    global z # please modify global z
    z = 30  #this will refer to global z and not create a local variable
    return c

z = 3
print(sum(3,12))
print(z)