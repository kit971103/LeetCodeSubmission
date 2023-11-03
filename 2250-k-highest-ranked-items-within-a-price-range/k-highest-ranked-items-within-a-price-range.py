class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        
        self.grid = grid
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.visited = [ [False]*self.width for _ in range(self.height)]
        
        def diffuse(point, aset):
            row, col = point
            if row > 0 and self.grid[row-1][col]: aset.add( (row-1, col) )
            if row < self.height-1 and self.grid[row+1][col]: aset.add( (row+1, col) )
            if col > 0 and self.grid[row][col-1]: aset.add( (row, col-1) )
            if col < self.width-1 and self.grid[row][col+1]: aset.add( (row, col+1) )
        
        def unwrap(f):
            return lambda args: f(*args)
        
        ans=[]
        queqe = [tuple(start)]
        count=0
        
        while queqe:
            
            nextlayer = set()
            for point in queqe:

                diffuse(point, nextlayer)

                row, col = point
                self.visited[row][col] = True
                if pricing[0] <= grid[row][col] <= pricing[1]:
                    count += 1
                    ans.append(point)
            if count >= k: return ans[:k]

            queqe = [ (row, col) for row, col in nextlayer if not self.visited[row][col] ]
            queqe.sort( key  = unwrap(lambda row, col: (self.grid[row][col], row, col) ))
        return ans



