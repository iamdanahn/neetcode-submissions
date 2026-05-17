class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # create list to track score
        # check what the current operation is and perform it to the list
        # sum the whole list at the end
        scores = []
        for op in operations:
            if op == '+':
                scores.append(int(scores[-2]) + int(scores[-1]))
            elif op == 'D':
                scores.append(int(scores[-1]) * 2)
            elif op == 'C':
                scores.pop()
            else:
                scores.append(int(op))
        sum = 0
        for num in scores:
            sum += num
        return sum
