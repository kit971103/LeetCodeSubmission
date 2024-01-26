class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        dp = [[0]*n for _ in range(m)]
        dp[startRow][startColumn] = 1
        res = sum(dp[0])+sum(dp[-1])+sum(dp[i][0] for i in range(m))+sum(dp[i][-1] for i in range(m))
        MOD=10**9+7
        for _ in range(maxMove-1):
            dp = [ [ (dp[row-1][col] if row > 0 else 0)+(dp[row+1][col] if row < m-1 else 0)+(dp[row][col-1] if col > 0 else 0)+(dp[row][col+1] if col < n-1 else 0) for col in range(n)] for row in range(m)]
            res += sum(dp[0])+sum(dp[-1])+sum(dp[i][0] for i in range(m))+sum(dp[i][-1] for i in range(m))
            if res > MOD:
                res%=MOD
        return res
