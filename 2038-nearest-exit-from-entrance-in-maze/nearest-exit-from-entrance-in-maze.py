class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        maze[entrance[0]][entrance[1]] = "+"
        rows, cols = len(maze), len(maze[0])
        for c in itertools.chain(maze[0], maze[-1]):
            if c==".":
                break
        else:
            for i in range(rows):
                if maze[i][cols-1] == "." or maze[i][cols-1] == ".":
                    break
            else:
                return -1

        queue = deque([entrance])
        step = 0
        
        while queue:
            k = len(queue)
            for _ in range(k):
                row, col = queue.popleft()
                if ((row == rows-1) or (row == 0) or (col == cols-1) or (col == 0)) and step:
                    return step 
                # if (row + 1 < rows) and maze[row+1][col] == ".": 
                #     queue.append((row+1, col))
                # if 0 <= row - 1 and maze[row-1][col] == ".": 
                #     queue.append((row-1, col))
                # if col + 1 < cols and maze[row][col+1] == ".": 
                #     queue.append((row, col+1))
                # if 0 <= col - 1 and maze[row][col-1] == ".": 
                #     queue.append((row, col-1))
                
                for new_row, new_col in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                    if (0 <= new_row < rows) and (0 <= new_col < cols) and maze[new_row][new_col] == ".":
                        maze[new_row][new_col] = "+"
                        queue.append((new_row, new_col))
            step += 1
        return -1


