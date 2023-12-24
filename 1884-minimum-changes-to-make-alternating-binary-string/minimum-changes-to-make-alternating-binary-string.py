class Solution:
    def minOperations(self, s: str) -> int:
        p=0
        for i, c in enumerate(s):
            p+=(i%2)^(c=="1")
        
        return min(p,len(s)-p)
        