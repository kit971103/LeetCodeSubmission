class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row, col in itertools.product(range(len(matrix)-1), range(len(matrix[0])-1)):
            if matrix[row][col] != matrix[row+1][col+1]: return False
        return True