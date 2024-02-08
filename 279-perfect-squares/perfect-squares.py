class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = [i*i for i in range(1,int(math.sqrt(n))+1)]
        bfs = set([0])
        depth = 1
        while True:
            bfs = set(a+b for a,b in itertools.product(bfs, perfect_squares))
            if n in bfs:
                return depth
            depth+=1
        return None




