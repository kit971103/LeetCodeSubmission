class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for f in count.values():
            if f == 1:
                return -1
            res += (f+2)//3
        return res

        