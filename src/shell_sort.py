from typing import List, NoReturn


def shell_sort(in_list: List[int], ini_step) -> NoReturn:
    length = len(in_list)
    step = ini_step
    while step > 1:
        for i in range(1, length):
            for j in range(i, 0, -int(step)):
                if in_list[j] < in_list[j-1]:
                    in_list[j], in_list[j-1] = in_list[j-1], in_list[j]
                else:
                    break
        step /= 2


if __name__ == "__main__":      
    in_list = [15,12,73,23,89,2,87,94,54,3,162,12,33]
    shell_sort(in_list, len(in_list)-2)
    assert in_list == [2, 3, 12, 12, 15, 23, 33, 54, 73, 87, 89, 94, 162]
    print("Test succeeded.")
