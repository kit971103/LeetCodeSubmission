class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        for solution in itertools.permutations(range(n)):
            OK = True
            for row, col in enumerate(solution):
                for i in range(row + 1, n):
                    j = solution[i]
                    d = i - row
                    if (j == col + d) or (j == col - d): 
                        OK = False
                        break
                if not OK: break
            else:
                res.append(["".join( "Q" if j == i else "." for j in range(n) ) for i in solution])
        return res


            


        