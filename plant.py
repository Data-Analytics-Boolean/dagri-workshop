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
        """Change the status of the plant to "dead"."""
        self.alive = False
        self.infected = False
        self.healed = False

    def infect(self, parasite: Parasite):
        if self.alive is False:
            raise Exception("Cannot infect a dead plant.")
        if self.healed is True:
            raise Exception("Cannot infect a healed plant.")
        self.parasite = parasite
        self.infected = True

    def heal(self):
        if self.alive is False:
            raise Exception("Cannot heal a dead plant.")
        self.healed = True
        self.infected = False

    def pass_day(self):
        if self.infected is True:
            if random.random() < self.parasite.chance_to_kill:
                self.die()
            elif random.random() < self.parasite.chance_to_heal:
                self.heal()

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
