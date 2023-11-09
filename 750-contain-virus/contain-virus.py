class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        # for row in isInfected: print(row)

        def allInfected() -> bool:
            for row, col in itertools.product(range(rows), range(cols)):
                if isInfected[row][col] == 0: return False
            return True
        def activeVirus() -> bool:
            for row, col in itertools.product(range(rows), range(cols)):
                if isInfected[row][col] > 0 : return True
            return False

        def dfsFindWall(row, col, group_id) -> None:
            
            if not( 0 <= row < rows ) or not(0 <= col < cols) or visited[row][col] or isInfected[row][col] != group_id: return
            visited[row][col] = True
            isInfected[row][col] = -1


            if row > 0 and isInfected[row-1][col] == 0: isHWall[row-1][col] = True
            if row < rows - 1 and isInfected[row+1][col] == 0: isHWall[row][col] = True
            if col > 0 and isInfected[row][col-1] == 0: isVWall[row][col-1] = True
            if col < cols -1 and isInfected[row][col+1] == 0: isVWall[row][col] = True

            dfsFindWall(row+1, col, group_id)
            dfsFindWall(row, col+1, group_id)
            dfsFindWall(row-1, col, group_id)
            dfsFindWall(row, col-1, group_id)

        # def dfs_affectArea(row, col):

        #     if not( 0 <= row < rows) or not(0 <= col < cols) or visited[row][col]: return
        #     # if not( 0 <= row < rows) or not(0 <= col < cols):
        #     #     print(f"dfs visited {row}, {col}, out-range") 
        #     #     return
        #     # elif visited[row][col]:
        #     #     print(f"dfs visited {row}, {col}, visited") 
        #     #     return
        
        #     nonlocal area_count
        #     # print(f"dfs visited {row}, {col}, status: {isInfected[row][col]}")
        #     if isInfected[row][col]:
        #         visited[row][col] = True
        #         dfs_affectArea(row-1, col)
        #         dfs_affectArea(row, col+1)
        #         dfs_affectArea(row+1, col)
        #         dfs_affectArea(row, col-1)
        #     else: 
        #         area_count+=1
        #         print(f"\t{area_count=}")
        
        def dfsFindReion(row, col):
            if not(0 <= row < rows) or not(0 <= col < cols) or visited[row][col] or isInfected[row][col] <= 0: return

            isInfected[row][col] = n_group
            visited[row][col] = True
            dfsFindReion(row+1, col)
            dfsFindReion(row, col-1)
            dfsFindReion(row-1, col)
            dfsFindReion(row, col+1)

        def pprint():
            for row in range(rows-1):
                arow = []
                for col in range(cols-1):
                    arow.append(f"{isInfected[row][col]: >3}") 
                    arow.append("|" if isVWall[row][col] else " ")
                arow.append(f"{isInfected[row][-1]: >3}") 
                print("".join(arow))
                arow = [ " ---" if x else "    " for x in isHWall[row]]
                print("".join(arow))
            arow = []
            for col in range(cols-1):
                arow.append(f"{isInfected[-1][col]: >3}") 
                arow.append("|" if isVWall[-1][col] else " ")
            arow.append(f"{isInfected[-1][-1]: >3}") 
            print("".join(arow))

        rows = len(isInfected)
        cols = len(isInfected[0])
        isHWall = [[False] * cols for _ in range(rows-1)]
        isVWall = [[False] * (cols - 1) for _ in range(rows)]
        # visited_init = [ [False] * cols for _ in range(rows) ]

        while not allInfected() and activeVirus():

            #label all region
            visited = [ [False] * cols for _ in range(rows) ]
            n_group = 0
            virus_map =[]
            for row, col in itertools.product(range(rows), range(cols)):
                if not visited[row][col] and isInfected[row][col] > 0:
                    # print("in the IF")
                    n_group += 1
                    virus_map.append((n_group, (row, col)))
                    dfsFindReion(row, col)
            
            # # debugger
            # print(f"{n_group=}, {virus_map=}")
            # print("isInfected:")
            # pprint()
            # print()
            if n_group == 0: break #safety break


            # find which region will affect most area
            max_area = quarantine_id = 0
            for group_id in range(1, n_group+1):
                area = 0
                for row, col in itertools.product(range(rows), range(cols)):
                    #check if the cell is isInfectedable and have isInfected cell nearby
                    if isInfected[row][col] == 0:
                        if row > 0 and isInfected[row-1][col] == group_id: area+=1
                        elif row < rows-1 and isInfected[row+1][col] == group_id: area+=1
                        elif col > 0 and isInfected[row][col-1] == group_id: area+=1
                        elif col < cols - 1 and isInfected[row][col+1] == group_id: area+=1
                if area > max_area:
                    max_area = area
                    quarantine_id = group_id
            
            
            # #debugger
            # print(f"{quarantine_id=}, {max_area=}\n")
            if max_area == 0: break #safety break

            # quarantine
            visited = [ [False] * cols for _ in range(rows) ]
            row, col = virus_map[quarantine_id-1][1]
            dfsFindWall(row, col, quarantine_id)
             
            # # debugger
            # print("after quarantine, isInfected:")
            # pprint()
            # print()

            # infect near by cell
            willBeInfected =[]
            for row, col in itertools.product(range(rows), range(cols)):
                if isInfected[row][col] == 0: 
                    if row < rows-1 and isInfected[row+1][col] > 0: willBeInfected.append((row, col))
                    elif 0 < row and isInfected[row-1][col] > 0: willBeInfected.append((row, col))
                    elif col < cols-1 and isInfected[row][col+1] > 0: willBeInfected.append((row, col))
                    elif 0 < col and isInfected[row][col-1] > 0: willBeInfected.append((row, col))
            for row, col in willBeInfected: isInfected[row][col] = 1

            # # debugger
            # print("after diffuse, isInfected:")
            # pprint()
            # print()
        
        # # debugger
        # print("final")
        # pprint()

        count = 0
        for row in isHWall:
            for haveWall in row:
                if haveWall: count+=1
        for row in isVWall:
            for haveWall in row:
                if haveWall: count+=1
        return count




        