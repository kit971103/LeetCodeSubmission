class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def f(x):
            return x-int(str(x)[::-1])
        count = Counter(f(n) for n in nums)
        res = 0
        for _, freq in count.items():
            res += freq*(freq-1)
        return res//2%(10**9 +7)