class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        if (s.length <= 1) return false;

        // keep track of whats in the s
        const stack = [];

        for (let i = 0; i < s.length; i++) {
            const bracket = s[i];
            if (bracket === "(" || bracket === "[" || bracket === "{") {
                stack.push(bracket);
            } else {
                // check if last bracket is reciprocal of closing bracket
                const last = stack.pop();

                if (last !== "(" && bracket === ")" ||
                    last !== "[" && bracket === "]" ||
                    last !== "{" && bracket === "}") {
                        return false;
                }
            }
        }

        if (stack.length > 0) return false;
        return true;
    }
}
