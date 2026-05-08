class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const numIdx = {};

        for (let i = 0; i < nums.length; i++) {
            const num = nums[i];
            const rem = target - num;
            if (rem in numIdx) {
                return [numIdx[rem], i];
            }
            numIdx[num] = i;
        }
    }
}
