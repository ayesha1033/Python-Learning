print("Example 1")
def sum(a,b):
# a and b are local variables 
    c = a+b
    z = 1 #it creates a local variable called z which is destroyed after this function returns
    return c

z = 8
print(z)
print(sum(4,6))

print("\nExample 2")
x = 10  # Global variable

def my_func():
    x = 5  # Local variable
    print(x)  # Output: 5

my_func()
print(x)  # Output: 10 (global x remains unchanged)