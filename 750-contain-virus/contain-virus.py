class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        # # debug
        # print("INIT isInfected:")
        # for row in isInfected: print("|".join([f"{n: >2}" for n  in row]))
        # print()

        def allInfected() -> bool:
            for row, col in itertools.product(range(rows), range(cols)):
                if isInfected[row][col] == 0: return False
            return True
        def activeVirus() -> bool:
            for row, col in itertools.product(range(rows), range(cols)):
                if isInfected[row][col] > 0 : return True
            return False
        
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
        # visited_void = [ [False] * cols for _ in range(rows) ]

        while not allInfected() and activeVirus():

            #idenify all region and find area
            visited = [ [False] * cols for _ in range(rows) ]
            virus_location = [] #( area, (row,col))
            for location in itertools.product(range(rows), range(cols)):
                row, col = location
                if not visited[row][col] and isInfected[row][col] > 0:
                    
                    visited_iter = [ [False] * cols for _ in range(rows) ]
                    area = 0
                    dfsFindReion(*location)

                    virus_location.append((area, location))

            # # debugger
            # print(f"\n\n{virus_location=}")

            # quarantine
            virus_location.sort()
            max_area, quarantine_reion = virus_location.pop()
            visited = [ [False] * cols for _ in range(rows) ]
            dfsQuarantine(*quarantine_reion)
            turn-=1
            
            # # debugger
            # print(f"{quarantine_reion=}, {max_area=}")
            # print("after quarantine, isInfected:")
            # for row in isInfected: print("|".join([f"{n: >2}" for n  in row]))
            # print()
            
            # infect near by cell
            visited = [ [False] * cols for _ in range(rows) ]
            for area, location in virus_location:
                dfsInfect(*location)
            
            # print("after infect, isInfected:")
            # for row in isInfected: print("|".join([f"{n: >2}" for n  in row]))
            # print()
        
        #count walls
        count = 0
        for row in isInfected:
            for a,b in itertools.pairwise(row):
                if a != b: count += 1
        for col in zip(*isInfected):
            for a,b in itertools.pairwise(col):
                if a != b: count += 1 
        return count




        