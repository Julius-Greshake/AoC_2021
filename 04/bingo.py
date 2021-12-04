import sys
from dataclasses import dataclass


def main():
    file_in = list([line.rstrip("\n") for line in open(sys.argv[1])])

    drawn = list(map(int, file_in[0].split(",")))

    board_lines = [l for l in file_in[2:] if l != ""]
    boards = []

    # iterate through board_lines in sets of five
    for i in range(0, len(board_lines), 5):
        nums = []

        for j in range(5):
            # split at arbitrary whitespace length, then map to ints and add to nums
            nums += list(map(int, board_lines[i + j].split()))

        boards.append(BingoBoard(numbers=nums, crosses=[0] * len(nums)))

    finished_boards = []
    final_scores = []

    for d in drawn:
        for i, board in enumerate(boards):
            if finished_boards.__contains__(i):
                continue
            board.cross_number(d)
            score = board.check_for_bingo()
            if score > 0:
                print(f"Bingo on board {i+1}!\tIts final score is {d*score}")
                final_scores.append(d * score)
                finished_boards.append(i)

        if len(finished_boards) == len(boards):
            print("\n")
            break

    print(f"Solution 1: {final_scores[0]}")
    print(f"Solution 2: {final_scores[-1]}")


@dataclass
class BingoBoard:
    numbers: list
    crosses: list

    def cross_number(self, n):
        if self.numbers.__contains__(n):
            self.crosses[self.numbers.index(n)] = 1

    def check_for_bingo(self):
        """Returns sum of unmarked numbers if there is a bingo, 0 otherwise"""
        for i in range(0, len(self.crosses), 5):
            if (sum(self.crosses[i : i + 5]) == 5) or ():
                return sum(self.get_unmarked_numbers())

        for i in range(0, 5):
            if sum(self.crosses[i::5]) == 5:
                return sum(self.get_unmarked_numbers())

        return 0

    def get_unmarked_numbers(self):
        return [num for i, num in enumerate(self.numbers) if self.crosses[i] == 0]


if __name__ == "__main__":
    main()
