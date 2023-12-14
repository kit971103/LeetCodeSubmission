class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, count = -1, 1
        rows, cols =len(grid), len(grid[0])
        checked = set()

        while count:
            count = 0
            time += 1
            visited = set()
            for row, col in product(range(rows), range(cols)):
                if not( (row,col) in checked or (row, col) in visited) and grid[row][col] == 2:
                    checked.add( (row,col) )
                    if 0 < row and grid[row-1][col] == 1:
                        count += 1
                        grid[row-1][col] = 2
                        visited.add( (row-1,col) )
                    if row+1 < rows and grid[row+1][col] == 1:
                        count += 1
                        grid[row+1][col] = 2
                        visited.add( (row+1,col) )
                    if 0 < col and grid[row][col-1] == 1:
                        count += 1
                        grid[row][col-1] = 2
                        visited.add( (row,col-1) )
                    if col+1 < cols and grid[row][col+1] == 1:
                        count += 1
                        grid[row][col+1] = 2
                        visited.add( (row,col+1) )

        for row, col in product(range(rows), range(cols)):
            if grid[row][col] == 1:
                return -1
        return time
        

        
        