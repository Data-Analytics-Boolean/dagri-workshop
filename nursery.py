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
        for _ in range(infected_plants_amount):
            sick_x = random.randint(0, self.rows - 1)
            sick_y = random.randint(0, self.columns - 1)

            self.plants[sick_x * self.columns + sick_y].infect(parasite)


    def pass_day(self):
        self.get_stats()
        if self.stats["alive"] == 0:
            raise Exception("No more alive plants.")
        if self.stats["infected"] == 0:
            raise Exception("No more infected plants.")
        for i in range(self.rows):
            for j in range(self.columns):
                plant: Plant = self.plants[i * self.columns + j]
                plant.pass_day()
                self.propagate(i, j)

    def propagate(self, i, j):
        plant: Plant = self.plants[i * self.columns + j]
        if plant.infected is True:
            adjacent_plants = self.get_adjacent_plants(i, j)
            for adjacent_plant in adjacent_plants:
                if adjacent_plant.alive is False:
                    continue
                elif adjacent_plant.infected is True:
                    continue
                elif adjacent_plant.healed is True:
                    continue
                if random.random() < plant.parasite.chance_to_spread:
                    self.stats["propagations"] += 1
                    adjacent_plant.infect(plant.parasite)

    def get_adjacent_plants(self, row, column):
        adjacent_plants = []
        if row > 0:
            adjacent_plants.append(self.plants[(row - 1) * self.columns + column])
        if row < self.rows - 1:
            adjacent_plants.append(self.plants[(row + 1) * self.columns + column])
        if column > 0:
            adjacent_plants.append(self.plants[row * self.columns + column - 1])
        if column < self.columns - 1:
            adjacent_plants.append(self.plants[row * self.columns + column + 1])
        if row > 0 and column > 0:
            adjacent_plants.append(self.plants[(row - 1) * self.columns + column - 1])
        if row > 0 and column < self.columns - 1:
            adjacent_plants.append(self.plants[(row - 1) * self.columns + column + 1])
        if row < self.rows - 1 and column > 0:
            adjacent_plants.append(self.plants[(row + 1) * self.columns + column - 1])
        if row < self.rows - 1 and column < self.columns - 1:
            adjacent_plants.append(self.plants[(row + 1) * self.columns + column + 1])
        return adjacent_plants

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
