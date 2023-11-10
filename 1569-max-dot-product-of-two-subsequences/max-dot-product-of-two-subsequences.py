class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        rows = len(nums2)
        cols = len(nums1)
        dp = [ [0]*cols for _ in range(rows)]

        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                x = nums2[row] * nums1[col]
                if row < rows - 1 and col < cols - 1: dp[row][col] = max(x, x + dp[row+1][col+1], dp[row+1][col], dp[row][col+1])
                elif row < rows - 1: dp[row][col] = max(x, dp[row+1][col])
                elif col < cols - 1: dp[row][col] = max(x, dp[row][col+1])
                else: dp[row][col] = x
        return dp[0][0]
                
        