class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt= collections.Counter(nums)
        res= [[0] for _ in range(max(list(cnt.values()))) ]
        for i in range(len(nums)):
            j=0
            while cnt[nums[i]]>0:
                res[j].append(nums[i])
                j=j+1
                cnt[nums[i]]-=1
        return [r[1:] for r in res]