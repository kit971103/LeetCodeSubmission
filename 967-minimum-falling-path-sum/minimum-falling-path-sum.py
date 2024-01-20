class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = matrix[0]
        for row in islice(matrix, 1, None):
            dp = [val + (min(dp[i-1:i+2]) if i else min(dp[0:2])) for i,val in enumerate(row)]
        return min(dp)

        