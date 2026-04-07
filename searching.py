import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    try:
        with open(file_name, "r") as file:
            data = json.load(file)

        if field not in data:
            return None

        # file_path = os.path.join(cwd_path, file_name)
        return data[field]
    except FileNotFoundError:
        print(f"Složka {file_name} nenalezena")


def linear_search(searched_seq, wanted_num):
    positions = []
    num_count = 0

    for i in range(len(searched_seq)):
        if searched_seq[i] == wanted_num:
            positions.append(i)
            num_count += 1
    return {
        "positions": positions,
        "count": num_count
    }


def binary_search(list_of_num, wanted_num):
    left_edge = 0
    right_edge = len(list_of_num) - 1

    while left_edge <= right_edge:
        mid = (left_edge + right_edge) // 2

        if list_of_num[mid] == wanted_num:
            return mid
        elif list_of_num[mid] > wanted_num:
            right_edge = mid - 1
        else:
            left_edge = mid + 1
    return None


def main():
    file_to_open = "sequential.json"
    key_to_find = "ordered_numbers"

    sequential_data = read_data(file_to_open, key_to_find)
    print(sequential_data)

    wanted_num = 64
    result = linear_search(sequential_data, wanted_num)
    print(result)

    target_num = 64
    result2 = binary_search(sequential_data, target_num)

    print(result2)


if __name__ == '__main__':
    main()
