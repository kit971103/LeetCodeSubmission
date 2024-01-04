class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for f in Counter(nums).values():
            if f == 1:
                return -1
            res += math.ceil(f/3)
        return res

        