from typing import List, NoReturn


def merge_sort(in_list: List[int], s_idx: int, e_idx: int) -> NoReturn:
    if s_idx < e_idx:
        m_idx = int((s_idx + e_idx)/2)
        merge_sort(in_list, s_idx, m_idx)
        merge_sort(in_list, m_idx+1, e_idx)
        merge_array(in_list, s_idx, m_idx, e_idx)


def merge_array(in_list: List[int], s_idx: int, m_idx: int, e_idx: int) -> NoReturn:
    left_idx = s_idx
    left_end = m_idx
    right_idx = m_idx + 1
    right_end = e_idx
    tmp = []

    while left_idx <= left_end and right_idx <= right_end:
        if in_list[left_idx] <= in_list[right_idx]:
            tmp.append(in_list[left_idx])
            left_idx += 1
        else:
            tmp.append(in_list[right_idx])
            right_idx += 1

    while left_idx <= left_end:
        tmp.append(in_list[left_idx])
        left_idx += 1
    
    while right_idx <= right_end:
        tmp.append(in_list[right_idx])
        right_idx += 1

    for i in range(len(tmp)):
        in_list[s_idx+i] = tmp[i]


if __name__ == "__main__":
    in_list = [15,12,73,23,89,2,87,94,54,3,162,12,33]
    merge_sort(in_list, 0, len(in_list)-1)
    assert in_list == [2, 3, 12, 12, 15, 23, 33, 54, 73, 87, 89, 94, 162]
    print("Test succeeded.")
