class Parasite():

    name: str = ""
    chance_to_kill: float = 0.0 # chance to kill its host plant in a day
    chance_to_heal: float = 0.0 # chance that its host plant self heals in a day
    chance_to_spread: float = 0.0 # chance that it spreads to another adjacent plant in a day

    def __init__(self, name: str, chance_to_kill: float, chance_to_heal: float, chance_to_spread: float):
        self.name = name
        self.chance_to_kill = chance_to_kill
        self.chance_to_heal = chance_to_heal
        self.chance_to_spread = chance_to_spread
