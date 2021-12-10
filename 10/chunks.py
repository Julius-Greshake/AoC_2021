import sys
from collections import defaultdict

OPENINGS = {"(", "[", "{", "<"}
CLOSINGS = {")", "]", "}", ">"}
PAIRS = {"()", "[]", "{}", "<>"}


def main():
    file_in = [line.rstrip("\n") for line in open(sys.argv[1])]

    illegal_tracker = defaultdict(int)

    incomplete_lines = []

    for line in file_in:
        # remove bracket pairs from line as long as this changes the line content
        changed = True
        while changed:
            changed = False
            for i, c in enumerate(line[:-1]):
                if PAIRS.__contains__(c + line[i + 1]):
                    changed = True
                    if i > 0:
                        before_pair = line[:i]
                    else:
                        before_pair = ""

                    if i + 2 < len(line):
                        after_pair = line[i + 2 :]
                    else:
                        after_pair = ""

                    line = before_pair + after_pair
                    break

        corrupted = False
        for c in line:
            if CLOSINGS.__contains__(c):
                illegal_tracker[c] += 1
                corrupted = True
                break

        if not corrupted:
            incomplete_lines.append(line)

    sol_1 = (
        3 * illegal_tracker[")"]
        + 57 * illegal_tracker["]"]
        + 1197 * illegal_tracker["}"]
        + 25137 * illegal_tracker[">"]
    )

    print(f"Solution 1: {sol_1}")

    completions = []

    for l in incomplete_lines:
        completions.append(reversed([get_closing_character(c) for c in l]))

    scores = []
    values = {")": 1, "]": 2, "}": 3, ">": 4}

    for l in completions:
        score = 0
        for c in l:
            score *= 5
            score += values[c]
        scores.append(score)

    scores.sort()

    print(f"Solution 2: {scores[int(len(scores)/2)]}")


def find_closing_character(opening, remainder):
    closing = get_closing_character(opening)
    for i, character in remainder:
        if character in OPENINGS:
            remainder = find_closing_character(character, remainder[i + 1 :])
        elif character in CLOSINGS:
            if character == closing:
                return remainder[i + 1 :]
        else:
            print(f"Unexpected character: {character}")


def get_closing_character(opening_character):
    # print(opening_character)
    match opening_character:
        case "(":
            return ")"
        case "[":
            return "]"
        case "{":
            return "}"
        case "<":
            return ">"


if __name__ == "__main__":
    main()
