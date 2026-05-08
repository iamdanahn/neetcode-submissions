class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // 1. compare each word's len. end if possible (only )
        // 2. iterate each word's chars. create a count of each word's chars.
        // 3. iterate thru word 1's chars and compare it with word 2s
        // 4. return results

        if (s.length !== t.length) return false;
        const word1 = {};
        const word2 = {};

        for (let char of s) {
            if (char in word1) {
                word1[char]++;
            } else {
                word1[char] = 1;
            }
        }
        for (let char of t) {
            if (char in word2) {
                word2[char]++;
            } else {
                word2[char] = 1;
            }
        }

        for (let char of s) {
            if (word1[char] !== word2[char]) return false;
        }

        return true;
    }
}
