class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        loggest_run = 0
        current_run = 0
        for i, n in enumerate(nums):
            if n != max_val:
                current_run = 0
                continue
            current_run += 1
            loggest_run = max(loggest_run, current_run)
        return loggest_run
        