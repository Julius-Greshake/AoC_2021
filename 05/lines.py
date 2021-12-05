import sys


def main():
    file_in = list([line.rstrip("\n") for line in open(sys.argv[1])])

    segments = []
    max_x = 1
    max_y = 1
    for l in file_in:
        start, stop = l.split(" -> ")
        x1, y1 = [int(i) for i in start.split(",")]
        x2, y2 = [int(i) for i in stop.split(",")]

        # potentially update max-values (and thus diagram size)
        if x1 > max_x:
            max_x = x1
        if x2 > max_x:
            max_x = x2

        if y1 > max_y:
            max_y = y1
        if y2 > max_y:
            max_y = y2

        segments.append([x1, y1, x2, y2])

    diagram1 = [[0 for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    diagram2 = [
        [0 for _ in range(max_y + 1)] for _ in range(max_x + 1)
    ]  # could also use copy.deepcopy(diagram1)

    for s in segments:

        if s[0] == s[2]:  # x1 == x2 -> horizontal line
            x = s[0]
            if s[1] < s[3]:
                y_start = s[1]
                y_end = s[3]
            else:
                y_start = s[3]
                y_end = s[1]

            for y in range(y_start, y_end + 1):
                diagram1[x][y] += 1
                diagram2[x][y] += 1

        elif s[1] == s[3]:  # y1 == y2 -> vertical line
            y = s[1]
            if s[0] < s[2]:
                x_start = s[0]
                x_end = s[2]
            else:
                x_start = s[2]
                x_end = s[0]

            for x in range(x_start, x_end + 1):
                diagram1[x][y] += 1
                diagram2[x][y] += 1

        elif abs(s[0] - s[2]) == abs(s[1] - s[3]):
            if s[0] < s[2]:
                x_step = 1
            else:
                x_step = -1

            if s[1] < s[3]:
                y_step = 1
            else:
                y_step = -1

            for step_size in range(abs(s[0] - s[2]) + 1):
                diagram2[s[0] + x_step * step_size][s[1] + y_step * step_size] += 1

    counter1 = 0
    counter2 = 0
    for ix, x in enumerate(diagram1):
        for iy, y in enumerate(x):
            if diagram1[ix][iy] >= 2:
                counter1 += 1
            if diagram2[ix][iy] >= 2:
                counter2 += 1

    print(f"Solution 1: {counter1}")
    print(f"Solution 2: {counter2}")


if __name__ == "__main__":
    main()
