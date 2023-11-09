class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        d = 0
        length = len(nums)
        while (start - d >= 0) or (start + d < length):
            if start - d >= 0 and nums[start -d] == target: return d
            elif start + d < length and nums[start +d] == target: return d
            d+=1
        return None

        