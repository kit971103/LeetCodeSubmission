class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []
        row = col = 0
        left_boundary = 0
        right_boundary = len(matrix[0]) - 1
        up_boundary = 0
        down_boundary = len(matrix) - 1
        cur_dirertion = "R"

        for i in range( (right_boundary+1) * (down_boundary+1) ):
            
            ans.append(matrix[row][col])
            
            if cur_dirertion == "R":
                if col < right_boundary: col += 1
                else:
                    up_boundary+=1
                    cur_dirertion="D"
                    row += 1
            
            elif cur_dirertion == "D":
                if row < down_boundary: row += 1
                else:
                    right_boundary-=1
                    cur_dirertion="L"
                    col -= 1
            
            elif cur_dirertion == "L":
                if left_boundary < col: col -= 1
                else:
                    down_boundary-=1
                    cur_dirertion="U"
                    row -= 1
            
            else:
                if up_boundary < row: row -= 1
                else:
                    left_boundary+=1
                    cur_dirertion="R"
                    col += 1
        
        return ans



        