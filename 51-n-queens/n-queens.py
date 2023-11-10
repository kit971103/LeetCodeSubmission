class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(k):
            if k >= n:
                rep = [ "".join("Q" if j == Q_position else "." for j in range(n)) for Q_position in sol]
                # rep= []
                # for each_Q_position in sol:
                #     row = ["Q" if j == each_Q_position else "." for j in range(n)]
                #     row = "".join(row)
                #     rep.append(row)
                # print(f"Found one solution:{sol}, {rep=}")
                res.append(rep)
                return
            

            possible_position = [True] * n
            for row, Q_position in enumerate(sol):
                possible_position[Q_position] = False
                d = k - row
                left_down = Q_position - d
                right_down = Q_position + d
                if left_down >= 0:  possible_position[left_down] = False
                if right_down < n: possible_position[right_down] = False
            possible_position = [index for index, val in enumerate(possible_position) if val]
            
            # print(f"At row {k}, {sol=}, {possible_position=}")
            for Q_position in possible_position:
                # print(f"\tTry {Q_position= }")
                sol.append(Q_position)
                dfs(k+1)
                sol.pop()
                # print(f"\tDone {Q_position= }")

        res = []
        sol = []
        dfs(0)
        return res
        

            


        