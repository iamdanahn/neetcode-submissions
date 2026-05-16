class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        amap = {}
        for num in nums:
            if num not in amap:
                amap[num] = True
            else:
                return True
        return False
        