class Solution:
    vowels = "aeiouAEIOU"
    # vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    def halvesAreAlike(self, s: str) -> bool:
        return (sum( 1 for c in islice(s,0,len(s)//2) if c in Solution.vowels) - sum( 1 for c in islice(s,len(s)//2, None) if c in Solution.vowels) ) == 0

