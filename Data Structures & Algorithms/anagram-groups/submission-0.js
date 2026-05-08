class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        // 1. interate thru all words in strs
        // 2. interate each word to find the char + count creating a key
        // 3. create a "map" to store the kv, where val = word itself
        // 4. iterate thru the map and add the values as an array into a final array for submission
        const wordMap = {};
        for (let word of strs) {
            //"a" ascii is 97
            const count = new Array(26).fill(0);
            for (let i = 0; i < word.length; i++) {
                const pos = word.charCodeAt(i) - 97;
                count[pos]++;
            }
            
            const key = count.toString();
            if (!(key in wordMap)) {
                wordMap[key] = [];
            } 
            wordMap[key].push(word);
        }
        // console.log(wordMap);
        const result = [];
        for (let word in wordMap) {
            // console.log(wordMap[word]);
            result.push(wordMap[word]);
        }    
        
        return result;
    }
}
