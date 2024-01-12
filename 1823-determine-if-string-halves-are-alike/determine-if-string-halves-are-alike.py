class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return (sum( 1 for c in islice(s,0,len(s)//2) if c in "aeiouAEIOU") - sum( 1 for c in islice(s,len(s)//2, None) if c in "aeiouAEIOU") ) == 0

