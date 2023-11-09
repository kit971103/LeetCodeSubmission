class Solution:
    def countHomogenous(self, s: str) -> int:
        memorization = dict()
        length = 1
        res = 0
        for a, b in itertools.pairwise(s):
            if a != b:
                if length not in memorization: 
                    memorization[length] = (length+1)*length//2
                res += memorization[length]
                length = 1
            else: 
                length += 1
        
        if length not in memorization: 
            memorization[length] = (length+1)*length//2
        res += memorization[length]

        return res%(10**9+7)
        
        