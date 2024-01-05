class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0]*len(nums)

        for i in range(len(nums)):
            try:
                dp[i] = max(dp[j] for j in range(i) if nums[i] > nums[j])+1
            except ValueError:
                dp[i] = 1
        return max(dp)

        