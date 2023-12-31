class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = dict()
        res = -1
        for i, c in enumerate(s):
            if c in seen:
                t = i-seen[c]-1
                if t > res: 
                    res = t
            else:
                seen[c] = i
        return res
