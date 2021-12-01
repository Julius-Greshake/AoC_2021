import sys


def main():
    sol_1 = 0
    sol_2 = 0

    file_in = list([line.rstrip("\n") for line in open(sys.argv[1])])

    depths = list(map(int, file_in))

    for i, d in enumerate(depths):
        if i > 0:
            if d - depths[i - 1] > 0:
                sol_1 += 1

        if i > 2:
            cur_3 = sum(depths[i - 2 : i + 1])
            pre_3 = sum(depths[i - 3 : i])
            if cur_3 > pre_3:
                sol_2 += 1

    print(f"Solution 1: {sol_1}")
    print(f"Solution 2: {sol_2}")


if __name__ == "__main__":
    main()
