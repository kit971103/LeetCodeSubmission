class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        smallest  = nums[-1]
        res = level = 0
        for i in range(len(nums)-1):
            if nums[i] == smallest: return res
            level += 1
            if nums[i] != nums[i+1]:
                res+=level
        return res




