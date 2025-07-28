class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        def or_(x, y):
            return x | y

        max_or = functools.reduce(or_, nums)
        total = 0
        for r in range(1, len(nums) + 1):
            for combination in itertools.combinations(nums, r):
                if functools.reduce(or_, combination) == max_or:
                    total += 1
        return total