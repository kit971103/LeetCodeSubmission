class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2: return nums
        
        nums.sort()
        res = []
        if nums[1] - nums[0] > 1: res.append(nums[0])
        i = 1
        while i < n-1:
            if nums[i+1] - nums[i] <= 1: 
                i+=2
                continue
            if nums[i] - nums[i-1] <= 1:
                i+=1
                continue
            res.append(nums[i])
            i+=1
        if nums[-1] - nums[-2] > 1: res.append(nums[-1])
        return res

