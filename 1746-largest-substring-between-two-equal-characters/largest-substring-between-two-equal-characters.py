class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = dict()
        res = -1
        for i, c in enumerate(s):
            if c in seen:
                res = max(res, i-seen[c]-1)
            else:
                seen[c] = i
        return res
