class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        res = 0
        dp = [[0]*n for _ in range(m)]
        dp[startRow][startColumn] = 1
        MOD=10**9+7
        for _ in range(maxMove):
            res += sum(dp[0])+sum(dp[-1])+sum(dp[i][0] for i in range(m))+sum(dp[i][-1] for i in range(m))
            if res > MOD:
                res%=MOD
            temp = [[0]*n for _ in range(m)]
            for row, col in product(range(m), range(n)):
                if row > 0:
                    temp[row][col] += dp[row-1][col]
                if row < m-1:
                    temp[row][col] += dp[row+1][col]
                if col > 0:
                    temp[row][col] += dp[row][col-1]
                if col < n-1:
                    temp[row][col] += dp[row][col+1]
            dp = temp
        return res
