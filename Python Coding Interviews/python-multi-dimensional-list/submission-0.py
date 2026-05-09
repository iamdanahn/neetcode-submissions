from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_nums = []
    for sublist in nested_arr:
        curr_max = -1
        for ele in sublist:
            curr_max = max(curr_max, ele)
        max_nums.append(curr_max)
    return max_nums


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
