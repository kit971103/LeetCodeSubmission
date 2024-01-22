class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = [False] * len(nums)
        res = []

        for n in nums:
            if seen[n-1]:
                res.append(n)
            else:
                seen[n-1] = True
        
        for n, found in enumerate(seen):
            if not found:
                res.append(n+1)
        
        return res

