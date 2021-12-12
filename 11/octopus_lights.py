import sys


def main():
    file_in = [line.rstrip("\n") for line in open(sys.argv[1])]
    # ints = list(map(int, file_in))

    energies_in = []

    for line in file_in:
        energies_in.append([int(n) for n in line])

    count_flashes(energies_in, 1000)


def count_flashes(e, steps):
    flashes = 0
    solved1 = False
    solved2 = False

    for s in range(steps):
        flashing = set()
        flashed = set()

        # increase all energy levels by 1
        for x, row in enumerate(e):
            for y, col in enumerate(row):
                e[x][y] += 1
                if e[x][y] > 9:
                    flashing.add((x, y))

        # work through all flashing octopus positions
        while len(flashing) > 0:
            (row, col) = flashing.pop()
            flashes += 1
            flashed.add((row, col))
            for i in [-1, 0, 1]:
                if row + i < 0 or row + i > len(e) - 1:
                    continue
                for j in [-1, 0, 1]:
                    if col + j < 0 or col + j > len(e[row + i]) - 1:
                        continue
                    e[row + i][col + j] += 1
                    if e[row + i][col + j] > 9 and (row + i, col + j) not in flashed:
                        flashing.add((row + i, col + j))

        # reset all energy levels > 9 to 0
        for (row, col) in flashed:
            e[row][col] = 0

        # print number of flashes after 100 steps
        if s == 99:
            print(f"Solution 1: {flashes}")
            solved1 = True

        if len(flashed) == 100:
            print(f"Solution 2: {s+1}")
            solved2 = True

        if solved1 and solved2:
            break


if __name__ == "__main__":
    main()
