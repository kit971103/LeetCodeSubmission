class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minium = nums[0]
        for n in nums:
            if (abs(n) < abs(minium)) or (abs(n) == abs(minium) and n > minium): minium = n
        return minium
        