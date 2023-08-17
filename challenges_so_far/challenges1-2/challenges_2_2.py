#Required and optional parameters
def f(a, b, c, x = 10, y = 5):
    """
    Returns sum of 5 ints
    3 are required parameters
    2 are optional parameters
    """
    a = int(a)
    b = int(b)
    c = int(c)
    return a+b+c+x+y

z = f(5, 10, 15)
print(z)
