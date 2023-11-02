class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(5.5*minutes - 30*hour)
        return angle if angle < 180 else 360-angle 