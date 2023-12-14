class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, count = 0, 1
        rows, cols =len(grid), len(grid[0])
        checked = [ [False]*cols for _ in range(rows)]

        while count:
            count = 0
            time += 1
            visited = [ [False]*cols for _ in range(rows)]
            for row, col in product(range(rows), range(cols)):
                if not checked[row][col] and not visited[row][col] and grid[row][col] == 2:
                    checked[row][col] = True
                    if 0 < row and grid[row-1][col] == 1:
                        count += 1
                        grid[row-1][col] = 2
                        visited[row-1][col] = True
                    if row+1 < rows and grid[row+1][col] == 1:
                        count += 1
                        grid[row+1][col] = 2
                        visited[row+1][col] = True
                    if 0 < col and grid[row][col-1] == 1:
                        count += 1
                        grid[row][col-1] = 2
                        visited[row][col-1] = True
                    if col+1 < cols and grid[row][col+1] == 1:
                        count += 1
                        grid[row][col+1] = 2
                        visited[row][col+1] = True

        for row, col in product(range(rows), range(cols)):
            if grid[row][col] == 1:
                return -1
        return time-1
        

        
        