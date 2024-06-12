class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = collections.Counter(nums)
        i0 = c[0] - 1
        i1 = i0 + c[1]
        i2 = i1 + c[2]
        for i in range(len(nums)):
            if i <= i0:
                n = 0
            elif i <= i1:
                n = 1
            else:
                n = 2
            nums[i] = n



