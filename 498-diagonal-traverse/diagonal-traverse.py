class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(mat), len(mat[0])
        for total in range(rows + cols - 1):
            if total%2:
                res.extend(mat[row][total - row] for row in range(max(total - cols + 1, 0), min(total+1, rows)))
            else:
                res.extend(mat[total - col][col] for col in range(max(total - rows + 1, 0), min(total+1, cols)))
        return res












        