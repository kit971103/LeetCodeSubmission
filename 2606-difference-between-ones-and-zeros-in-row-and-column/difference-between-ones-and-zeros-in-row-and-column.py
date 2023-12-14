class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        total = len(grid) + len(grid[0])
        row_sum = sum(grid[0])
        res = [ [2*(sum(col) + row_sum)-total for col in zip(*grid)] ]
        for row in islice(grid, 1, None):
            delta = sum(row)-row_sum
            row_sum += delta
            res.append( [ n + 2*delta for n in res[-1]] )
        return res
        