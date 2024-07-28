class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        res = 0
        for i, c in enumerate(s):
            if i%2:
                res -= int(c)
            else:
                res += int(c)
        
        return res
