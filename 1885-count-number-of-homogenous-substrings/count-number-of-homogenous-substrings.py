class Solution:
    def countHomogenous(self, s: str) -> int:
        memorization = [0]
        length = 1
        res = 0
        mod = 10**9 +7
        for a, b in itertools.pairwise(s):
            if a != b:
                while length >= len(memorization):
                    memorization.append( (len(memorization)+1)*len(memorization)//2%mod )
                res += memorization[length]
                if res >= mod: res %= mod
                length = 1
            else: 
                length += 1
        
        while length >= len(memorization):
            memorization.append( (len(memorization)+1)*len(memorization)//2%mod )
        res += memorization[length]
        if res >= mod: res %= mod

        return res
        