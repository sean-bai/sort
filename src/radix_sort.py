from typing import List, NoReturn


def radix_sort(
        in_list: List[int], 
        radix: int,
        max_depth: int
    ) -> List[int]:

        tmp = [[] for i in range(radix)]
        base = radix ** 0
        for num in in_list:
            quotient = num // base
            residual = num % radix
            tmp[residual].append(num) 

        for d in range(1, max_depth):
            tmp_2 = [[] for i in range(radix)]
            base = radix ** d
            for l in tmp:
                for num in l:
                    quotient = num // base
                    residual = quotient % radix
                    tmp_2[residual].append(num) 
            tmp = tmp_2

        res = [num for l in tmp for num in l]
        return res


if __name__ == "__main__":
    in_list = [15,12,73,23,89,2,87,94,54,3,162,12,33]
    res = radix_sort(in_list, radix=10, max_depth=3)
    assert res == [2, 3, 12, 12, 15, 23, 33, 54, 73, 87, 89, 94, 162]
    print("Test succeeded.")
