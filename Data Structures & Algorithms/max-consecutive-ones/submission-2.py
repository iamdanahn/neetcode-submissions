class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # set max_counter to track the max #1
        # iterate thru the nums
        # have a "switch" to indicate when we're in a group of 1s
        # switch ON/True when in 1s
        # switch OFF/False when not in 1s
        # when switching from ON->OFF, this will increment the counter
        # return counter in the end
        max_count = 0
        group_count = 0
        for num in nums:
            if num == 1:
                group_count += 1
            else:
                max_count = max(max_count, group_count)
                group_count = 0
        max_count = max(max_count, group_count)
        return max_count