class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen_start = set()
        seen_end = set()
        for start, end in paths:
            if start in seen_end:
                seen_end.remove(start)
            else:
                seen_start.add(start)
            
            if end in seen_start:
                seen_start.remove(end)
            else:
                seen_end.add(end)    
        return seen_end.pop()


            