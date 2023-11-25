class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        length = len(nums)
        lsum = 0
        res=[]
        for i, n in enumerate(nums,1):
            lsum+=n
            res.append(total - 2*( lsum - n*i ) - n*length)
        return res