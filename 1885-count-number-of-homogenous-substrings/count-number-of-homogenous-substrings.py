class Solution:
    def countHomogenous(self, s: str) -> int:
        length = 1
        res = 0
        for a, b in itertools.pairwise(s):
            if a != b:
                res += (length+1)*length//2
                length = 1
            else: 
                length += 1
        res += (length+1)*length//2
        return res%(10**9+7)
        
        