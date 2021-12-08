import sys
from collections import defaultdict


def main():
    file_in = [line.rstrip("\n") for line in open(sys.argv[1])]
    # ints = list(map(int, file_in))

    signal_patterns = []
    output_values = []

    for line in file_in:
        signal_pattern, output_value = line.split(" | ")
        signal_patterns.append(signal_pattern)
        output_values.append(output_value)

    unique_counter = 0

    for line in output_values:
        for pattern in line.split():
            if {2, 3, 4, 7}.__contains__(len(pattern)):
                unique_counter += 1

    print(f"Solution 1: {unique_counter}")


    # Start Part 2
    output_sum = 0

    all_segments = {"a", "b", "c", "d", "e", "f", "g"}

    for sig, out in zip(signal_patterns, output_values):
        numbers = sig.split()
        segment_dict = defaultdict(list)
        for n in numbers:
            segment_set = set()
            for segment in n:
                segment_set.add(segment)

            segment_dict[len(n)].append(segment_set)

        # Decode the wiring from our segments-dictionary

        # "a" is the set-difference between 3 and 2
        mapping = {}
        mapping[segment_dict[3][0].difference(segment_dict[2][0]).pop()] = "a"

        # find missing segments from numbers with 6 segments -> {c,d,e}
        cde_segments = set()
        for segment_set in segment_dict[6]:
            cde_segments.add(segment_dict[7][0].difference(segment_set).pop())

        for cde_segment in cde_segments:
            if cde_segment in segment_dict[2][0]:
                mapping[cde_segment] = "c"
                mapping[segment_dict[2][0].difference(cde_segment).pop()] = "f"
            elif cde_segment in segment_dict[4][0]:
                mapping[cde_segment] = "d"
                mapping[segment_dict[4][0].difference({cde_segment}.union(segment_dict[2][0])).pop()] = "b"
            else:
                mapping[cde_segment] = "e"

        # g segment is the unused segment
        non_g_segments = {c for c in mapping.keys()}
        mapping[all_segments.difference(non_g_segments).pop()] = "g"

        # Convert output digits into number:
        out_number_string = ""
        out_digits = out.split()

        for d in out_digits:
            digit_segments = set()
            for c in d:
                digit_segments.add(c)

            match len(digit_segments):
                case 2:
                    out_number_string += "1"
                case 3:
                    out_number_string += "7"
                case 4:
                    out_number_string += "4"
                case 5:
                    # number can be 2, 3 or 5
                    missing_segs = all_segments.difference(digit_segments)
                    mapped_missing_segs = {mapping[s] for s in missing_segs}
                    if mapped_missing_segs == {"b", "f"}:
                        out_number_string += "2"
                    elif mapped_missing_segs == {"b", "e"}:
                        out_number_string += "3"
                    elif mapped_missing_segs == {"c", "e"}:
                        out_number_string += "5"
                    else:
                        print("5 segments but not matching number!")

                case 6:
                    # number can be 0, 6 or 9
                    missing_seg = all_segments.difference(digit_segments).pop()
                    mapped_missing_seg = mapping[missing_seg]
                    match mapped_missing_seg:
                        case "c":
                            out_number_string += "6"
                        case "d":
                            out_number_string += "0"
                        case "e":
                            out_number_string += "9"
                case 7:
                    out_number_string += "8"
                case _:
                    print("Unexpected amount of segments!")

        output_sum += int(out_number_string)

    print(f"Solution 2: {output_sum}")


if __name__ == "__main__":
    main()
