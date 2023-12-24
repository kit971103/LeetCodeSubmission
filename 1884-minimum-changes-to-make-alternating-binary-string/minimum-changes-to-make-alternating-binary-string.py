class Solution:
    def minOperations(self, s: str) -> int:
        
        p0 = p1 = 0

        for i, c in enumerate(s):
            if (i%2)^(c=="1"):
                p1+=1
            else:
                p0+=1
        
        return min(p0,p1)
        