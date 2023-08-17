#Exception handling
def f():
    """
    Exception handling test
    Converts string to float
    Gives error if input is invalid
    Prints a float
    """
    try:
        x = input("Give me a decimal number: ")
        x = float(x)
        print(x)
    except(ValueError):
        print("Invalid input!")

f()
