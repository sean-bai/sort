from typing import List, NoReturn


def quick_sort(in_list: List[int], s_idx: int, e_idx: int) -> NoReturn:
    if e_idx > s_idx:
        first_idx = s_idx
        last_idx = e_idx
        
        base_idx = int((s_idx + e_idx)/2)
        base_val = in_list[base_idx]
        
        in_list[first_idx], in_list[base_idx] = in_list[base_idx], in_list[first_idx]
        s_idx += 1
        
        while e_idx > s_idx:
            if in_list[s_idx] <= base_val:
                s_idx += 1
                continue
            if in_list[e_idx] > base_val:
                e_idx -= 1
                continue
            in_list[s_idx], in_list[e_idx] = in_list[e_idx], in_list[s_idx]
            s_idx += 1
            e_idx -= 1
            
        if in_list[s_idx] <= base_val:
            final_idx = s_idx
        else:
            final_idx = s_idx - 1
            
        in_list[first_idx], in_list[final_idx] = in_list[final_idx], in_list[first_idx]
        quick_sort(in_list, first_idx, final_idx-1)
        quick_sort(in_list, final_idx+1, last_idx)


if __name__ == "__main__":       
    in_list = [15,12,73,23,89,2,87,94,54,3,162,12,33]
    quick_sort(in_list, 0, len(in_list)-1)
    assert in_list == [2, 3, 12, 12, 15, 23, 33, 54, 73, 87, 89, 94, 162]
    print("Test succeeded.")
