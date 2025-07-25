class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = {n for n in filter(lambda x: x>0,nums)}
        return sum(seen) if seen else max(nums)

