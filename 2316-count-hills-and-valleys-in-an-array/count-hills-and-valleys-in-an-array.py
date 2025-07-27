class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # if only two number, there is no hill nor valley by definition
        if len(nums) <= 2:
            return 0

        total = 0
        left = nums[0]
        for i, n in enumerate(nums[1:-1], start = 1):
            right = nums[i + 1]
            # print(f"{i=}, {left=}, {n=}, {right=}")

            if (n > left and n > right) or (n < left and n < right):
                # print(f"added at {i}")
                total += 1

            left = n if n != right else left
        return total


