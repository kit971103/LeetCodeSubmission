class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        return sum (abs(n) for n in (count_s-count_t).values())
        