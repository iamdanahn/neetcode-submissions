import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    # return sorted(nums, reverse=True)
    temp = []
    for num in nums:
        heapq.heappush(temp, -num)

    max_heap = []
    while temp:
        max_heap.append(-heapq.heappop(temp))
    return max_heap




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
