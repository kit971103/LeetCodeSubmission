class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        dp = [[1] * n for _ in range(n)]
        steps = ((+1, +2), (+2, +1), (+1, -2), (+2, -1), (-1, +2), (-2, +1), (-1, -2), (-2, -1))

        for _ in range(k):
            # print(f"depth: {_}")
            # for _ in dp:
            #     print(f"\t{_}")

            temp = [[0] * n for _ in range(n)]
            for y, x in itertools.product(range(n), repeat = 2):
                temp[y][x] = sum( dp[y+dy][x+dx] for dy, dx in steps if (0 <= y+dy < n)and(0 <= x+dx < n))
            
            dp = copy.deepcopy(temp)
        
        return dp[row][column]/8**k
            


        