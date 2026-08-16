def sum(a,b):
    '''("Summation occuring")'''
    c = a+b
    return c

print(sum.__doc__)


def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b

print(add.__doc__)
print(add(2,3))
