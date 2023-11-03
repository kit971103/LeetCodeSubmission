class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        
        width = len(grid[0])
        height = len(grid)
        visited = [ [False]*width for _ in range(height)]
        ans=[]
        queqe = [tuple(start)]
        count=0
        
        while queqe:
            
            # print(f"before queqe, {queqe=}, {ans=}")
            
            nextlayer = set()
            for point in queqe:

                row, col = point
                visited[row][col] = True
                
                if row > 0 and grid[row-1][col]: nextlayer.add( (row-1, col) )
                if row < height-1 and grid[row+1][col]: nextlayer.add( (row+1, col) )
                if col > 0 and grid[row][col-1]: nextlayer.add( (row, col-1) )
                if col < width-1 and grid[row][col+1]: nextlayer.add( (row, col+1) )
                
                if pricing[0] <= grid[row][col] <= pricing[1]:
                    count += 1
                    ans.append( point )
            
            # print(f"finished queqe, {ans=}, {count=}")
            # print(f"visited=\n{visited}")
            if count >= k: return ans[:k]

            queqe = [ point for point in nextlayer if not visited[ point[0] ][ point[1] ]]

            # print(f"before filtering, {nextlayer=}")
            # print(f"before sorting queqe, {queqe=}")

            queqe.sort( key  = lambda point: (grid[point[0]][point[1]], point[0], point[1]))
            # print(f"after sorting queqe, {queqe=}\n\n")
        return ans



