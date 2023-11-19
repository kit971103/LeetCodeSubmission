class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        smallest_i = bisect.bisect_right(nums, nums[0])-1
        res = 0
        n = len(nums)
        i = n-1
        while i > smallest_i:
            i = bisect.bisect_left(nums, nums[i])-1
            res += n-i-1
        return res






