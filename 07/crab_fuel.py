import math
import sys
from collections import defaultdict


def main():
    file_in = [line.rstrip("\n") for line in open(sys.argv[1])]

    crab_positions = defaultdict(int)

    for s in file_in[0].split(","):
        crab_positions[int(s)] += 1

    min_position1 = 0
    min_fuel1 = math.inf

    for goal_position in range(max(crab_positions.keys()) + 1):
        fuel_costs = sum(
            [c * abs((p - goal_position)) for p, c in crab_positions.items()]
        )
        if fuel_costs < min_fuel1:
            min_fuel1 = fuel_costs
            min_position1 = goal_position

    print(f"Solution 1: {min_fuel1} (moving all crabs to position {min_position1})")

    min_position2 = 0
    min_fuel2 = math.inf

    for goal_position in range(max(crab_positions.keys()) + 1):
        fuel_costs = sum(
            [
                c * sum(range(1, abs((p - goal_position)) + 1))
                for p, c in crab_positions.items()
            ]
        )
        if fuel_costs < min_fuel2:
            min_fuel2 = fuel_costs
            min_position2 = goal_position

    print(f"Solution 2: {min_fuel2} (moving all crabs to position {min_position2})")


if __name__ == "__main__":
    main()
