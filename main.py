""" module docstring
"""

from time import sleep

from console import delete_last_lines
from nursery import Nursery
from parasite import Parasite

SIMULATION_DAYS = 365
STARTING_SICK_PLANTS = 8
NURSERY_ROWS = 10
NURSERY_COLUMNS = 20

if __name__ == '__main__':
    n1 = Nursery(NURSERY_ROWS, NURSERY_COLUMNS)
    p1 = Parasite("Japonica", chance_to_kill=.01, chance_to_heal=.001, chance_to_spread=.01)

    n1.spread_parasite(STARTING_SICK_PLANTS, p1)

    for i in range(1, SIMULATION_DAYS+1):
        print(f"Day {i}", end="")
        print(n1, end="\r")
        try:
            n1.pass_day()
        except Exception as e:
            print(e)
            break
        sleep(0.05)
        delete_last_lines(NURSERY_ROWS + 1)

    print(f'Simulation ended on day {i}. \n Stats: {n1.get_stats()}')
