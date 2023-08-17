"""

"""

aboot_me = {
    "Height": 75,
    "Weight": 245,
    "FavColor": "Orange",
    "FavDesigner": "Miyamoto/Kojima",
    "FavGame": "Metal Gear Solid 1"
    }

def question():
    qestion = input("What question would you like to know? ")
    if qestion in aboot_me:
        q = aboot_me[qestion]
        print(q)
    else:
        print("Invalid Question")

question()
