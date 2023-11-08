class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        d = max(abs(fx-sx), abs(fy-sy))
        return t >= d if d else t != 1
