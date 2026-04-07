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


def main():
    file_to_open = "sequential.json"
    key_to_find = "unordered_numbers"

    sequential_data = read_data(file_to_open, key_to_find)
    print(sequential_data)

    wanted_num = 0
    result = linear_search(sequential_data, wanted_num)
    print(result)


if __name__ == '__main__':
    main()
