"""module docstring
"""

import random
from parasite import Parasite


class Plant():
    """class docstring
    """

    name: str = ""
    alive: bool = True
    infected: bool = False
    healed: bool = False
    parasite: Parasite = None

    def __init__(self, name: str):
        self.name = name
        self.alive = True
        self.infected = False
        self.healed = False

    def die(self):
        pass

    def infect(self, parasite: Parasite):
        pass

    def heal(self):
        pass

    def pass_day(self):
        pass

    def __str__(self):
        """Return a glyph representation of the plant."""
        glyph = ""
        if self.alive is False:
            glyph = " ☠️ "
        elif self.infected is True:
            glyph = " 🦠"
        elif self.healed is True:
            glyph = " 🌱"
        else:
            glyph = " 🪴 "
        return glyph
