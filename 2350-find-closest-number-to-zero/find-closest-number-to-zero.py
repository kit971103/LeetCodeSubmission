class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return min(nums, key = lambda n: abs(n) - (0.5 if n > 0 else 0))
        