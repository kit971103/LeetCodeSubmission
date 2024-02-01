class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if i%3 == 0:
                t = []
            t.append(n)
            if i%3 == 2:
                if t[-1] - t[0] > k:
                    return []
                res.append(t)
        return res
        