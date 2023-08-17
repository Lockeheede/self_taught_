class Horse():
    def __init__(self, n, w, s, o):
        self.name = n
        self.weight = w
        self.speed = s
        self.owner = o

class Rider():
    def __init__(self, n):
        self.name = n

jame = Rider("Jaime Lynne")
epo = Horse("Epona", 1000, 10, jame)

print(epo.owner.name)
    
