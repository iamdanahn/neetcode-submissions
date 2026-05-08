class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = [];
        const brackets = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }

        for (let c of s) {
            if (c in brackets && stack.length > 0) {
                if (stack[stack.length - 1] === brackets[c]) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c)
            }
        }
        
        return stack.length === 0;
    }
}
