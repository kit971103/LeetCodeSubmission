class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = collections.Counter(nums)
        i0 = c[0] - 1
        i1 = i0 + c[1]
        for i in range(len(nums)):
            nums[i] = (i > i0) + (i > i1)



