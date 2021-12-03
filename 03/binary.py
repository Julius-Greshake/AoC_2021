import sys


def main():
    file_in = list([line.rstrip("\n") for line in open(sys.argv[1])])

    array_in = []

    for i, line in enumerate(file_in):
        array_in.append([])
        for j, bit in enumerate(line):
            array_in[i].append(int(bit))

    gamma = find_most_common_bits(array_in)
    epsilon = [(1 - g) for g in gamma]

    gamma_int = bin_list_to_int(gamma)
    epsilon_int = bin_list_to_int(epsilon)

    print(f"Solution 1: {gamma_int*epsilon_int}")

    # Part 2 #

    oxygen_array = array_in.copy()
    co2_array = array_in.copy()

    oxygen_counter = 0
    while len(oxygen_array) > 1:
        print(f"Length of oxygen array: {len(oxygen_array)}")
        most_commons = find_most_common_bits(oxygen_array)

        new_oxygen_array = [
            o for o in oxygen_array if o[oxygen_counter] == most_commons[oxygen_counter]
        ]
        oxygen_array = new_oxygen_array
        oxygen_counter += 1

    co2_counter = 0
    while len(co2_array) > 1:
        print(f"Length of co2 array: {len(co2_array)}")
        most_commons = find_most_common_bits(co2_array)
        new_co2_array = [
            c for c in co2_array if c[co2_counter] != most_commons[co2_counter]
        ]
        co2_array = new_co2_array
        co2_counter += 1

    oxygen_rating = bin_list_to_int(oxygen_array[0])
    co2_rating = bin_list_to_int(co2_array[0])

    print(f"Solution 2: {oxygen_rating*co2_rating}")


def bin_list_to_int(bin_list):
    return int("".join(str(i) for i in bin_list), 2)


def find_most_common_bits(nested_bin_list):

    sums = [0] * len(nested_bin_list[0])
    for row in nested_bin_list:
        for i, col_bit in enumerate(row):
            sums[i] += col_bit

    most_common = [1] * len(nested_bin_list[0])
    for i, s in enumerate(sums):
        if s < (len(nested_bin_list) / 2):
            most_common[i] = 0

    return most_common


if __name__ == "__main__":
    main()
