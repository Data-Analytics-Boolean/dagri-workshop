"""module docstring
"""

import random
from parasite import Parasite
from plant import Plant


class Nursery():
    """class docstring
    """

    plants = []
    rows = None
    columns = None
    stats = {
        "alive": 0,
        "infected": 0,
        "healed": 0,
        "deaths": 0,
        "propagations": 0
    }

    def __init__(self, rows, columns):
        self.plants = []
        self.rows = rows
        self.columns = columns

        for i in range(rows):
            for j in range(columns):
                self.plants.append(Plant(f"Plant {i}-{j}"))

    def spread_parasite(self, infected_plants_amount, parasite: Parasite):
        pass


    def pass_day(self):
        pass

    def propagate(self, i, j):
        pass

    def get_adjacent_plants(self, row, column):
        pass

    def get_stats(self):
        self.stats["alive"] = 0
        self.stats["infected"] = 0
        self.stats["healed"] = 0
        self.stats["deaths"] = 0
        for i in range(self.rows):
            for j in range(self.columns):
                plant: Plant = self.plants[i * self.columns + j]
                if plant.alive is True:
                    self.stats["alive"] += 1
                if plant.infected is True:
                    self.stats["infected"] += 1
                if plant.healed is True:
                    self.stats["healed"] += 1
                if plant.alive is False:
                    self.stats["deaths"] += 1
        return self.stats

    def __str__(self):
        string_rep = f''
        for i in range(self.rows):
            string_rep += "\n"
            for j in range(self.columns):
                plant: Plant = self.plants[i * self.columns + j]
                string_rep += str(plant)
        return f"{string_rep}\n"
