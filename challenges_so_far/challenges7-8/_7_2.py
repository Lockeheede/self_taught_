x = input("What is your name? ")
y = input("What is your age? ")
z = input("What is your weight? ")
a = input("What is your height? ")

with open("new-file.txt", "w") as f:
    f.write("Your name is {}\n".format(x))
    f.write("Your age is {}\n".format(y))
    f.write("Your weight is {}\n".format(z))
    f.write("Your height is {}\n".format(a))

print("Data saved into new-file.txt")
