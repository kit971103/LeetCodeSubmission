class Solution:
    def countHomogenous(self, s: str) -> int:
        length = 1
        res = 0
        mod = 10**9 +7
        for a, b in itertools.pairwise(s):
            if a != b:
                res += (length+1)*length//2
                if res >= mod: res%=mod
                length = 1
            else: 
                length += 1
        res += (length+1)*length//2
        
        return res%mod if res >= mod else res

        
        