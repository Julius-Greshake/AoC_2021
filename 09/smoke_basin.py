import sys


def main():
    file_in = [line.rstrip("\n") for line in open(sys.argv[1])]
    heightmap = []

    for line in file_in:
        heightmap.append([int(n) for n in line])

    low_points = {}

    for i, row in enumerate(heightmap):
        for j, column in enumerate(row):
            h = heightmap[i][j]

            # check above if not on row 0
            if i > 0:
                if heightmap[i - 1][j] <= h:
                    continue

            # check bottom if not on last row
            if i + 1 < len(heightmap):
                if heightmap[i + 1][j] <= h:
                    continue

                    # check left if not on column 0
            if j > 0:
                if heightmap[i][j - 1] <= h:
                    continue

            # check right if not on last column
            if j + 1 < len(heightmap[i]):
                if heightmap[i][j + 1] <= h:
                    continue

            low_points[(i, j)] = h

    print(f"Solution 1: {sum(low_points.values())+len(low_points)}")

    # Start of part 2

    basin_sizes = []

    for location, basin_height in low_points.items():
        members = set()
        # members[location] = basin_height
        members.add(location)
        border = set()
        border.add(location)
        while len(border) > 0:
            new_border = set()
            for i, j in border:
                h = heightmap[i][j]

                # check above if not on row 0
                if i > 0:
                    if 9 > heightmap[i - 1][j] > h:
                        if (i - 1, j) not in members:
                            members.add((i - 1, j))
                            new_border.add((i - 1, j))

                # check bottom if not on last row
                if i + 1 < len(heightmap):
                    if 9 > heightmap[i + 1][j] > h:
                        if (i + 1, j) not in members:
                            members.add((i + 1, j))
                            new_border.add((i + 1, j))

                # check left if not on column 0
                if j > 0:
                    if 9 > heightmap[i][j - 1] > h:
                        if (i, j - 1) not in members:
                            members.add((i, j - 1))
                            new_border.add((i, j - 1))

                # check right if not on last column
                if j + 1 < len(heightmap[i]):
                    if 9 > heightmap[i][j + 1] > h:
                        if (i, j + 1) not in members:
                            members.add((i, j + 1))
                            new_border.add((i, j + 1))

                border = new_border

        basin_sizes.append(len(members))

    basin_sizes.sort()
    solution_2 = 1
    for s in basin_sizes[-3:]:
        solution_2 *= s
    print(f"Solution 2: {solution_2}")


if __name__ == "__main__":
    main()
