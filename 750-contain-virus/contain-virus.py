class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        
        def dfsQuarantine(row, col):
            if not(0 <= row < rows) or not(0 <= col < cols) or visited[row][col] or isInfected[row][col] <= 0: return
            visited[row][col] = True
            isInfected[row][col] = turn
            dfsQuarantine(row+1, col)
            dfsQuarantine(row, col-1)
            dfsQuarantine(row-1, col)
            dfsQuarantine(row, col+1)

        def dfsFindReion(row, col):
            if not(0 <= row < rows) or not(0 <= col < cols) or visited_iter[row][col] or isInfected[row][col] < 0: return
            visited_iter[row][col] = True

            if isInfected[row][col] > 0:
                visited[row][col] = True
                dfsFindReion(row+1, col)
                dfsFindReion(row, col-1)
                dfsFindReion(row-1, col)
                dfsFindReion(row, col+1)
            else: 
                nonlocal area
                area += 1

        def dfsInfect(row, col):
            if not(0 <= row < rows) or not(0 <= col < cols) or visited[row][col] or isInfected[row][col] < 0: return
            visited[row][col] = True
            if isInfected[row][col] > 0:
                dfsInfect(row+1, col)
                dfsInfect(row, col-1)
                dfsInfect(row-1, col)
                dfsInfect(row, col+1)
            else: 
                isInfected[row][col] = 1
                
        rows = len(isInfected)
        cols = len(isInfected[0])
        turn = -1

        while True:

            visited = [ [False] * cols for _ in range(rows) ]
            virus_location = [] #( area, (row,col))
            max_area = 0
            for location in itertools.product(range(rows), range(cols)):
                row, col = location
                if isInfected[row][col] > 0 and not visited[row][col]:
                    visited_iter = [ [False] * cols for _ in range(rows) ]
                    area = 0
                    dfsFindReion(*location)
                    if area >= max_area:
                        max_area = area
                        quarantine_reion = location
                    virus_location.append( location )
            if len(virus_location) == 0: break

            visited = [ [False] * cols for _ in range(rows) ]
            dfsQuarantine(*quarantine_reion)
            turn-=1
            if len(virus_location) == 1: break

            visited = [ [False] * cols for _ in range(rows) ]
            for location in virus_location:
                if location == quarantine_reion: continue
                dfsInfect(*location)

        count = 0
        for row in isInfected:
            for a,b in itertools.pairwise(row):
                if a != b: count += 1
        for col in zip(*isInfected):
            for a,b in itertools.pairwise(col):
                if a != b: count += 1 
        return count




        