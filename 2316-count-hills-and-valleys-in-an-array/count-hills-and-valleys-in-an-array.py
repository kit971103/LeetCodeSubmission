class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        total = 0
        left = nums[0]
        for mid, right in itertools.pairwise(nums[1:]):
            if (mid > left and mid > right) or (mid < left and mid < right):
                total += 1
            if mid != right:
                left = mid
        return total


