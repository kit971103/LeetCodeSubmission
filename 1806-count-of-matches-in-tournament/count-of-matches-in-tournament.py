class Solution:
    def numberOfMatches(self, n: int) -> int:
        match = 0
        while n > 1:
            match += n//2
            n = math.ceil(n/2)
        return match
        
        