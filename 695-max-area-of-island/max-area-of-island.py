class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            if  not( 0 <= row < rows and 0 <= col < cols) or visited[row][col]: 
                return
            visited[row][col] = True
            if grid[row][col]:
                nonlocal area
                area += 1
                bfs(row+1, col)
                bfs(row-1, col)
                bfs(row, col+1)
                bfs(row, col-1)
        
        max_area = 0
        visited = [ [False] * cols for _ in range(rows)]
        for row, col in itertools.product(range(rows), range(cols)):
            area = 0
            bfs(row, col)
            if area > max_area: max_area = area
        
        return max_area



            
        