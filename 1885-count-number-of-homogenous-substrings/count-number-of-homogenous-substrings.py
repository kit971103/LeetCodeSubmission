class Solution:
    def countHomogenous(self, s: str) -> int:
        memorization = dict()
        length = 1
        res = 0
        mod = 10**9 +7
        for a, b in itertools.pairwise(s):
            if a != b:
                if length not in memorization: 
                    memorization[length] = ((length+1)*length//2)%mod
                    if memorization[length] >= mod: memorization[length] %= mod
                res += memorization[length]
                if res >= mod: res %= mod
                length = 1
            else: 
                length += 1
        
        if length not in memorization: 
            memorization[length] = ((length+1)*length//2)%mod
            if memorization[length] >= mod: memorization[length] %= mod
        res += memorization[length]
        if res >= mod: res %= mod

        return res
        