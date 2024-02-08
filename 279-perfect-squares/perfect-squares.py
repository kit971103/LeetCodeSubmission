class Solution:
    def numSquares(self, n: int) -> int:
        i = 2
        perfect_squares = [1]
        while i*i <= n:
            perfect_squares.append(i*i)
            i+=1
        bfs = set([0])
        depth = 1
        while True:
            bfs = set(a+b for a,b in itertools.product(bfs, perfect_squares))
            if n in bfs:
                return depth
            depth+=1
        return None




