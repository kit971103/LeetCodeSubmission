class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        steps = ((+1, +2), (+2, +1), (+1, -2), (+2, -1), (-1, +2), (-2, +1), (-1, -2), (-2, -1))
        def addPossibleMove(y, x):
            for dy, dx in steps:
                new_y = y + dy
                new_x = x + dx
                if 0 <= new_y < n and 0 <= new_x < n:
                    nextlayer[new_y, new_x] += layer[y,x]


        layer = collections.Counter()
        layer[row, column] = 1

        for _ in range(k):
            nextlayer = collections.Counter() 
            for point in layer:
                addPossibleMove(*point)
            layer = nextlayer.copy()

        return layer.total()/8**k
            


        