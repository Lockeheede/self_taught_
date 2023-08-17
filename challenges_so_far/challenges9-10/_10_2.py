class ThatThing():
    def __init__(self):
        self.name = "Thing"

def the_same(fst, snd):
    print(fst is snd)
   

bob = ThatThing()
same_bob = bob
another_bob = ThatThing

the_same(bob, same_bob)
the_same(bob, another_bob)
