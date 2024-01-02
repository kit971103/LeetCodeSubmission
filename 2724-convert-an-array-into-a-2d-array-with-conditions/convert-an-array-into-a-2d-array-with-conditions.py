class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt= collections.Counter(nums)
        res= [[] for _ in range(max(list(cnt.values()))) ]
        for n in nums:
            j=0
            while cnt[n]>0:
                res[j].append(n)
                j+=1
                cnt[n]-=1
        return res