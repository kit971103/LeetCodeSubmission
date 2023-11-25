class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        length = len(nums)
        return [ total +n*(2*i-length)-2*lsum  for i,(n, lsum) in enumerate(zip(nums, itertools.accumulate(nums)),1)]