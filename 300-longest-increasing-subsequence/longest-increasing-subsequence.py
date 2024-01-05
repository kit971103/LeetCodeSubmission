class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0]*len(nums)

        for i in range(len(nums)):
            dp[i] = max(itertools.chain([0], (dp[j] for j in range(i) if nums[i] > nums[j])) )+1
        return max(dp)

        