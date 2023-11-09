class Solution:
    def countHomogenous(self, s: str) -> int:
        memorization = [0]
        length = 1
        res = 0
        for a, b in itertools.pairwise(s):
            if a != b:
                while length >= len(memorization):
                    memorization.append( (len(memorization)+1)*len(memorization)//2 )
                res += memorization[length]
                length = 1
            else: 
                length += 1
        
        while length >= len(memorization):
            memorization.append( (len(memorization)+1)*len(memorization)//2 )
        res += memorization[length]

        return res%(10**9 + 7 )
        