class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        time = [ math.ceil(d/v) for d, v in zip(dist, speed) ]
        time.sort()
        # print(time)
        
        for i, monster in enumerate(time): 
            if i >= monster: return i
        
        return i + 1