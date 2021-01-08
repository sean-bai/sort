from typing import List, NoReturn
import heapq


def heap_sort(in_list: List[int]) -> List[int]:
    heapq.heapify(in_list)
    return heapq.nsmallest(len(in_list), in_list) 


if __name__ == "__main__":
    in_list = [15,12,73,23,89,2,87,94,54,3,162,12,33]
    res = heap_sort(in_list)
    assert res == [2, 3, 12, 12, 15, 23, 33, 54, 73, 87, 89, 94, 162]
    print("Test succeeded.")
