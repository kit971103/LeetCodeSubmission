class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        for col in range(len(matrix[0])):
            count = 0
            for row in range(len(matrix)):
                count = count + 1 if matrix[row][col] else 0
                matrix[row][col] = count

        max_area = 0
        for row in matrix:
            row.sort(reverse = True)
            max_area = max(max_area, *(length * height for length, height in enumerate(row,1)))
        return max_area




        