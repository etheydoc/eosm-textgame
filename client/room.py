# This class defines rooms and worlds for the text game.
# (c) Ethan Block, 2018

class Room:
    """The class that defines a single room."""
    def __init__(self, name, desc, exits, items, entities):
        self.name = name
        self.desc = desc
        self.exits = exits
        self.items = items
        self.entities = entities

class World:
    """The class that defines a collection of rooms."""
    def __init__(self, rooms):
        self.rooms = rooms
