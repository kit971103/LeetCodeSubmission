class Solution:
    def minOperations(self, s: str) -> int:
        p=sum(1 for i, c in enumerate(s) if (i%2)^(c=="1"))
        return min(p,len(s)-p)
        