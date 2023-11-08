class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if (sx == fx) and (sy == fy): return t != 1
        return t >= max(abs(fx-sx), abs(fy-sy))