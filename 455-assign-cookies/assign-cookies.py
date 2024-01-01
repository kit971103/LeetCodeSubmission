class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse  = True)
        s.sort(reverse  = True)
        n = len(g)
        while g and s:
            if s[-1] >= g[-1]:
                g.pop()
            s.pop()
        return n-len(g)

        