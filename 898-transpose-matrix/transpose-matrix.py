class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        newmatrix=[ [0] * len(matrix) for _ in range(len(matrix[0]))]

        for i, j  in itertools.product(range(len(matrix)), range(len(matrix[0]))):
            newmatrix[j][i] = matrix[i][j]
        return newmatrix