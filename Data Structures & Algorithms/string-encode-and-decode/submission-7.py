class Solution:

    def encode(self, strs: List[str]) -> str:
        # iterate thru the list
        # for each string, get the length and a delimiter like #
        # then place the string into a results string
        res = []
        for word in strs:
            res.append(str(len(word))) 
            res.append("#")
            res.append(word)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # go index by index
        # when you find a number and a # next to each other
        # slice the word and add it to a results list
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded_strs.append(s[i:j])
            i = j

        return decoded_strs
