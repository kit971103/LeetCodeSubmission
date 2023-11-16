class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        layer = collections.Counter()
        layer[(row, column)] += 1
        steps = ((+1, +2), (+2, +1), (+1, -2), (+2, -1), (-1, +2), (-2, +1), (-1, -2), (-2, -1))

        for _ in range(k):
            
            nextlayer = collections.Counter()
            for y, x in layer.keys():
                for dy, dx in steps:
                    ny = y+dy
                    nx = x+dx
                    if 0 <= ny < n and 0 <= nx < n: 
                        nextlayer[(ny, nx)]+=layer[(y,x)]
            
            layer = nextlayer.copy()

        return layer.total()/8**k
            


        