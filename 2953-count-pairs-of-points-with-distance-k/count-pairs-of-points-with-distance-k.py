class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        
        c=0
        hasmap = collections.Counter()
        
       
        for point in coordinates:
            
            point = tuple(point)
            x1, y1 = point
            
            for x in range(k+1):
                target = (x1^x, y1^(k-x))
                if target in hasmap: 
                    c += hasmap[target]
            
            if point in hasmap: hasmap[point]+=1
            else: hasmap[point] = 1    
        
        return c
        