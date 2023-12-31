class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = dict()
        res = -1
        for i, c in enumerate(s):
            if c in seen:
                if (t:=i-seen[c]-1) > res: 
                    res = t
            else:
                seen[c] = i
        return res
