class Solution:
    vowels = "aeiouAEIOU"
    # vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    def halvesAreAlike(self, s: str) -> bool:
        res = 0
        for c in islice(s, 0, len(s)//2):
            if c in Solution.vowels:
                res+=1
        for c in islice(s, len(s)//2, None):
            if c in Solution.vowels:
                res-=1
        return res == 0

