class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = []
        while count:
            res.append([])
            remove = []
            for n in count:
                count[n]-=1
                res[-1].append(n)
                if count[n] == 0:
                    remove.append(n)
            for n in remove:
                count.pop(n)
        return res
        