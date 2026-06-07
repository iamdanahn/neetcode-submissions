class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # iterate thru the array
        # keep track of each element's count with map
        # keys are each num in the list
        # values are the count of each num/key
        # create a new map with keys equal to the count
        # it will be a list from 1~len of nums
        # create a results array where we add the num from the frequency map until we hit k
        # iterate the map k times to find each num result
        initMap = {}
        for num in nums:
          if num not in initMap:
            initMap[num] = 0
          initMap[num] += 1
        
        frequency = [[] for i in range(len(nums) + 1)]
        for num, count in initMap.items():
          frequency[count].append(num)
        
        res = []
        for i in range(len(frequency) - 1, 0, -1):
          for num in frequency[i]:
            res.append(num)
            if len(res) == k:
              return res