class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        row, col = 0, 0
        direction = "RU"
        res = []
        for _ in range(rows*cols):
            
            res.append(mat[row][col])
            
            if direction == "RU":
                hit_wall = (row == 0 or col == cols-1)
                if not hit_wall:
                    row -= 1
                    col += 1 
                else:
                    direction = "LD"
                    if col+1 < cols:
                        col +=1
                    else:
                        row += 1
            
            else:
                hit_wall = (row == rows-1 or col == 0)
                if not hit_wall:
                    row += 1
                    col -= 1
                else:
                    direction = "RU"
                    if row+1 < rows:
                        row +=1
                    else:
                        col += 1
        return res










        