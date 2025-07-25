class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n > 0:
                seen.add(n)
        return sum(seen) if seen else max(nums)

