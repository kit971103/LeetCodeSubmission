class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        for row in mat:
            if sum(row) == 1 and sum( mat[i][row.index(1)] for i in range(len(mat))) == 1:
                count += 1
        return count

        