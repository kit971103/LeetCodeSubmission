class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        
        c=0
        hasmap = collections.Counter()
        
       
        for x1, y1 in coordinates:
            
            for x in range(k+1):
                c += hasmap[ x1^x, y1^(k-x) ]
            
            hasmap[x1, y1]+=1   
        
        return c
        