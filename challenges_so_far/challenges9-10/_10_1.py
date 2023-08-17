class Square():
    sqr = []

    def __init__(self,w,l):
        self.width = w
        self.length = l
        self.sqr.append((self.width, self.length))

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.width, self.width, self.length, self.length)

a_square = Square(15, 15)
print(a_square)
    
