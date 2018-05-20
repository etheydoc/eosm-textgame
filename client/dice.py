# The class that defines a set of dice for rolling for stats, D&D style.
# (c) Ethan Block, 2018

import random

class Die:
    """Represents a single die."""

    def __init__(self, sides=6):
        """Set the number of sides (defaults to six)."""
        self.sides = sides

    def roll(self):
        """Roll the die."""
        return random.randint(1, self.sides)

class Dice:
    """Represents multiple dice."""

    def __init__(self, num=2, sides=6):
        """Set the number of dice (defaults to two)."""
        self.num = num
        """Set the number of sides (defaults to six)."""
        self.sides = sides

    def roll_sum(self):
        """Roll the dice and sum the results."""
        return sum(random.randint(1,self.sides) for i in range(self.num))

    def roll_avg(self):
        """Roll the dice, average the results, and round to the nearest integer."""
        return int(sum(random.randint(1,self.sides) for i in range(self.num))/self.num)

    def roll_max(self):
        """Roll the dice and pick the highest one."""
        return max([random.randint(1,self.sides) for i in range(self.num)])

    def roll_min(self):
        """Roll the dice and pick the lowest one."""
        return min([random.randint(1,self.sides) for i in range(self.num)])
