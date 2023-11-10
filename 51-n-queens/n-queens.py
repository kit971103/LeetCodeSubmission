class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(k):
            if k >= n:
                res.append([ "".join("Q" if j == Q_position else "." for j in range(n)) for Q_position in sol])
                return

            possible_position = set(range(n))
            for row, Q_position in enumerate(sol):
                d = k - row
                possible_position.discard(Q_position)
                possible_position.discard(Q_position+d)
                possible_position.discard(Q_position-d)

            for Q_position in possible_position:
                sol.append(Q_position)
                dfs(k+1)
                sol.pop()

        res = []
        sol = []
        dfs(0)
        return res
        

            


        