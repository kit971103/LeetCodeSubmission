class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0]
        for row in islice(matrix, 1, None):
            t = []
            for i, val in enumerate(row):
                if 0 < i < n-1:
                    k = min(dp[i-1:i+2])
                elif i == 0:
                    k = min(dp[i:i+2])
                else:
                    k = min(dp[i-1:i+1])
                t.append(val+k)
            dp = t.copy()
        return min(dp)

        