class Solution:
    @functools.cache
    def integerReplacement(self, n: int) -> int:
        if n == 1: return 0
        if n%2:
            return min(self.integerReplacement(n-1), self.integerReplacement(n+1)) + 1
        else:
            return self.integerReplacement(n//2)+1
        