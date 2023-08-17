def f1(x):
    """
    Returns variable divided by 2
    """
    return x/2

def f2(x):
    """
    Returns variable multiplied by 4
    """
    return x*4

a = input("Give me a number: ")
a = int(a)
f1(a)
b = f2(a)
print(b)
