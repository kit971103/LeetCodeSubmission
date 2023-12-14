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
                    for dy, dx in ((+1, 0), (-1,0), (0, +1), (0, -1)):
                        if 0 <= row+dy <rows and 0 <= col+dx < cols and grid[row+dy][col+dx] == 1:
                            count += 1
                            grid[row+dy][col+dx] = 2
                            visited[row+dy][col+dx] = True

        for row, col in product(range(rows), range(cols)):
            if grid[row][col] == 1:
                return -1
        return time-1
        

        
        