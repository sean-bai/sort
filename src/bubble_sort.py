from typing import List, NoReturn


def bubble_sort(in_list: List[int]) -> NoReturn:
    length = len(in_list)
    for i in range(length-1):
        for j in range(i, length):
            if in_list[i] > in_list[j]:
                in_list[i], in_list[j] = in_list[j], in_list[i]


if __name__ == "__main__":      
    in_list = [15,12,73,23,89,2,87,94,54,3,162,12,33]
    bubble_sort(in_list)
    assert in_list == [2, 3, 12, 12, 15, 23, 33, 54, 73, 87, 89, 94, 162]
    print("Test succeeded.")
