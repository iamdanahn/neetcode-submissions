class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const checker = {};

        for (let num of nums) {
            if (num in checker) return true;
            checker[num] = true;
        }

        return false;
    }
}
