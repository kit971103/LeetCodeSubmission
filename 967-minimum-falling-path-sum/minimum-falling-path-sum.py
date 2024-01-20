class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [0]*len(matrix)
        for row in matrix:
            dp = [val + (min(dp[i-1:i+2]) if i else min(dp[0:2])) for i,val in enumerate(row)]
        return min(dp)

        