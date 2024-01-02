class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter()
        res = []
        for n in nums:
            k = count[n]
            if len(res) <= k:
                res.append([])
            res[k].append(n)
            count[n]+=1
        return res

