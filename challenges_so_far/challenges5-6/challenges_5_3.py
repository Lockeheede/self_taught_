n = " "
cor = 5
play = True
while play:
    n = input("Guess a number: ")
    if n == "q":
        break
    n = int(n)
    if n == cor:
        print("Correct!")
        break
    else:
        print("Incorrect!")
