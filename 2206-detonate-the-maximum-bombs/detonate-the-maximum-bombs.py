class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def will_detonate(bomb1, bomb2) -> bool:
            return bomb1[2] >= math.sqrt( (bomb1[0]-bomb2[0])**2 + (bomb1[1]-bomb2[1])**2 )
        
        nearby = { i:[ j for j, bomb2 in enumerate(bombs) if will_detonate(bomb, bomb2[:2])] for i, bomb in enumerate(bombs) }
        
        max_detonate = 1
        n = len(bombs)
        
        for i in range(n):
            detonated = [False] * n
            queqe = [i]
            while queqe:
                j = queqe.pop()
                if detonated[j]: continue
                detonated[j] = True
                queqe.extend(nearby[j])
            count = sum(detonated)
            if count > max_detonate: max_detonate= count

        return max_detonate



