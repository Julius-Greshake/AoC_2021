import sys
from collections import defaultdict


def main():
    file_in = [line.rstrip("\n") for line in open(sys.argv[1])]

    population = defaultdict(int)
    for s in file_in[0].split(","):
        population[int(s)] += 1

    end_population_80 = populate(population, 80)

    print(f"Solution 1: {sum(end_population_80.values())}")

    end_population_256 = populate(population, 256)
    print(f"Solution 2: {sum(end_population_256.values())}")


def populate(old_pop, days):
    for _ in range(days):
        new_pop = defaultdict(int)
        for state, amount in old_pop.items():
            if state == 0:
                new_pop[8] += amount
                new_pop[6] += amount
            else:
                new_pop[state - 1] += amount

        old_pop = new_pop

    return old_pop


if __name__ == "__main__":
    main()
