class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # for row in matrix: print(row)
        # width = len(matrix[0])
        # height = len(matrix)
        
        ans = []
        row = col = 0
        left_boundary = 0
        right_boundary = len(matrix[0]) - 1
        up_boundary = 0
        down_boundary = len(matrix) - 1
        # walk_dirertion = itertools.cycle("RDLU")
        # cur_dirertion = next(walk_dirertion)
        cur_dirertion = "R"

        for i in range( (right_boundary+1) * (down_boundary+1) ):
            
            ans.append(matrix[row][col])
            # print(f"\npoistion {i}: {row},{col}; dirertion={cur_dirertion}")
            # print(f"\t{ans=}")
            # print(f"\t{left_boundary=}, {right_boundary=}, {up_boundary=}, {down_boundary=}")
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
            
            elif cur_dirertion == "U":
                if up_boundary < row: row -= 1
                else:
                    left_boundary+=1
                    cur_dirertion="R"
                    col += 1

            # if not(left_boundary < col < right_boundary and up_boundary < row < down_boundary) :
            #     if cur_dirertion == "R": up_boundary += 1
            #     elif cur_dirertion == "D": right_boundary -= 1
            #     elif cur_dirertion == "L": down_boundary -= 1
            #     elif cur_dirertion == "U": left_boundary += 1
            #     cur_dirertion = next(walk_dirertion)

            # if cur_dirertion == "R": col += 1
            # elif cur_dirertion == "D": row += 1
            # elif cur_dirertion == "L": col -= 1
            # elif cur_dirertion == "U": row -= 1
        
        return ans



        