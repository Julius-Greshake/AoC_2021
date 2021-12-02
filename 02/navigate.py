import sys


def main():
    sol_1 = 0
    sol_2 = 0

    depth1 = 0
    position1 = 0
    
    depth2 = 0
    position2 = 0
    aim = 0

    file_in = list([line.rstrip("\n") for line in open(sys.argv[1])])

    for line in file_in:
        match line.split():
            case ("forward", n):
                position1 += int(n)

                position2 += int(n)
                depth2 += aim*int(n)
            
            case ("down", n):
                depth1 += int(n)

                aim += int(n)

            case ("up", n):
                depth1 -= int(n)

                aim -= int(n)

    sol_1 = depth1*position1
    sol_2 = depth2*position2

    print(f"Solution 1: {sol_1}")
    print(f"Solution 2: {sol_2}")


if __name__ == "__main__":
    main()
