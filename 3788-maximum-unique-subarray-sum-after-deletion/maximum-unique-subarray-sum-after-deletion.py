class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = {n for n in nums if n > 0}
        return sum(seen) if seen else max(nums)

