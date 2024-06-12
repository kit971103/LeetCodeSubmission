class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = collections.Counter(nums)
        i0 = c[0]
        i1 = i0 + c[1]
        nums[0:i0] = [ 0 for _ in range(i0) ]
        nums[i0:i1] = [ 1 for _ in range(i1-i0) ]
        nums[i1:] = [ 2 for _ in range(len(nums)-i1) ]




