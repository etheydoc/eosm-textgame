# The base classes for entities, players, allies, and enemies.
# (c) Ethan Block, 2018

class Character:
    def __init__(self,name,hp,ac,inventory,exp):
        self.name=name
        self.hp=hp
        self.ac=ac
        self.inventory=inventory
        self.exp=exp

class Player(Character):

    def __init__(self,name,hp,ac,inventory,exp):
        super().__init__(name,hp,ac,inventory,exp)
