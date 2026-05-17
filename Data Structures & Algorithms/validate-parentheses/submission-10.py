class Solution:
    def isValid(self, s: str) -> bool:
        # iterate thru the string
        # stack
        # 1. Add the char if open char
        # 2. If close char, pop from teh stack and compare
        # 2a. if it matches the current char's closing bracket, then continue
        # 2b. if it doesn't, reutrn false
        # 3. after iterating all the chars in the string, if the stack is empty. we're good, else false
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0: return False
                opener = stack.pop()
                if (c == ")" and opener != "(") or (c == "}" and opener != "{") or (c == "]" and opener != "["):
                    return False
        return len(stack) == 0