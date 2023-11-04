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
            
            if cur_dirertion == "R" and col >= right_boundary:
                up_boundary+=1
                cur_dirertion="D"
            elif cur_dirertion == "D" and row >= down_boundary:
                right_boundary-=1
                cur_dirertion="L"
            elif cur_dirertion == "L" and col <= left_boundary:
                down_boundary-=1
                cur_dirertion="U"
            elif cur_dirertion == "U" and row <= up_boundary:
                left_boundary+=1
                cur_dirertion="R"
            
            if cur_dirertion == "R": col += 1
            elif cur_dirertion == "D": row += 1
            elif cur_dirertion == "L": col -= 1
            else: row -= 1

        return ans



        