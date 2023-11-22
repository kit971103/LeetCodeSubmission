class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result = [(row + col, col, nums[row][col]) for row in range(len(nums)) for col in range(len(nums[row]))]
        result.sort()
        return [val for _,__, val in result]


