class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = dict()

        for i, c in enumerate(s):
            if c in seen:
                seen[c][1] = i
            else:
                seen[c] = [i, None]
        res = -1
        for _, indexs in seen.items():
            if indexs[1]:
                res = max(res, indexs[1]-indexs[0]-1)
        return res
