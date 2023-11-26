class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            
            if  not( 0 <= row < rows and 0 <= col < cols) or grid[row][col] == 0: 
                return
            
            nonlocal area
            area += 1
            grid[row][col] = 0
            bfs(row+1, col)
            bfs(row-1, col)
            bfs(row, col+1)
            bfs(row, col-1)
        
        max_area = 0
        for row, col in itertools.product(range(rows), range(cols)):
            area = 0
            bfs(row, col)
            if area > max_area: max_area = area
        
        return max_area



            
        