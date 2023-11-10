class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def dfs(row, col, gold):
            if not(0 <= row < rows) or not(0 <= col < cols) or not grid[row][col] or visited[row][col]: return gold
            
            visited[row][col] = True
            gold += grid[row][col]
            up = dfs(row-1, col, gold)
            down = dfs(row+1, col, gold)
            left = dfs(row, col-1, gold)
            right = dfs(row, col+1, gold)
            visited[row][col] = False
            return max(up, down, left, right)

        rows = len(grid)
        cols = len(grid[0])
        max_gold = 0
        visited = [[False]*cols for _ in range(rows)]

        for row, col in itertools.product(range(rows), range(cols)):
            gold = dfs(row, col, 0)
            if gold > max_gold: max_gold = gold
        return max_gold



        