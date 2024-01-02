class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter()
        res = []
        for n in nums:
            if len(res) <= count[n]:
                res.append([])
            res[count[n]].append(n)
            count[n]+=1
        return res

