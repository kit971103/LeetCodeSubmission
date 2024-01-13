class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum (abs(n) for n in (Counter(s)-Counter(t)).values())
        