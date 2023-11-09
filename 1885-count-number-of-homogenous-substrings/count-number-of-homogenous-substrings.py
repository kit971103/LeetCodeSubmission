class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        for k, g in itertools.groupby(s):
            l = len(list(g))
            res += (l+1)*l//2
        return res%(10**9+7)

        
        