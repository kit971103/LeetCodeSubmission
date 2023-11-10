class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        def dfs(k):
            if k >= n:
                nonlocal count
                count += 1
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
        sol =[]
        count = 0
        dfs(0)
        return count