class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        for solution in itertools.permutations(range(n)):
            for row, col in enumerate(solution):
                for i in range(row + 1, n):
                    j = solution[i]
                    d = i - row
                    if (j == col + d) or (j == col - d): break
                else: continue
                break
            else: res.append(["".join( "Q" if j == i else "." for j in range(n) ) for i in solution])
        return res


            


        