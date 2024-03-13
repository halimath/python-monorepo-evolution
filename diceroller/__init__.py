
__version__ = '0.1.0'
__author__ = 'Alexander Metzner'
__all__ = ['Roll']

"""
This module provides a class Roll which handles rolling dice based on a diceroller
expression. The formal definition of the expression is as follows:
"""


from random import randrange

class Roll:
    """
    A class to handle rolling one or more dice and modify the result with a
    constant modifier. Construct a new instance of this class passing in the
    diceroller expression. Each instance holds the result of making that roll.

    Attributes
    ----------
    count : int
        the number of dice to roll
    num_sides : int
        Number of sides the die/dice should have
    mod : int
        the modifier
    natural : int
        the natural result (i.e. just rolling the die/dice)
    value : int
        the overall result
    """
    def __init__(self, expr: str):
        expr = expr.lower()
        self.count = 1
        if expr[0] != 'd':
            (c, expr) = expr.split('d')
            self.count = int(c)
        else:
            expr = expr[1:]
    
        self.num_sides = 0
        self.mod = 0
        
        for idx, c in enumerate(expr):
            if c in ('+', '-'):
                self.mod = int(expr[idx:])
                self.num_sides = int(expr[:idx])
    
        if self.num_sides == 0:
            self.num_sides = int(expr)
        
        self.natural = sum(randrange(1, self.num_sides) for _ in range(self.count))

    @property
    def value(self):
        return self.natural + self.mod

    def __int__ (self):
        return self.value

    def __format__(self, format):
        match format:
            case 'd': return str(int(self))
            case 'f': return f"{str(self)}: {self.value} ({self.natural}{self.mod:+})"
            case _: raise TypeError('unsupported format string')
    
    def __str__(self):
        return f"{'' if self.count == 1 else self.count}d{self.num_sides}{'' if self.mod == 0 else format(self.mod, '+')}"
    
    def __repr__(self):
        return f"Roll({str(self)})"
