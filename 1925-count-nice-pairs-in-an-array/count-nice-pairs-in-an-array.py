class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def f(x):
            z = x
            y = 0
            while z:
                y = y * 10 + z%10
                z//=10
            return x-y
        count = Counter(f(n) for n in nums)
        res = 0
        for _, freq in count.items():
            res += freq*(freq-1)
        return res//2%(10**9 +7)