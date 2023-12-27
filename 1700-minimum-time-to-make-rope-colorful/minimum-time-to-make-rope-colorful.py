class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        last = start = None
        recording = False
        res = 0
        for i, c in enumerate(colors):
            if c == last and not recording:
                start = i-1
                recording = True
            elif c != last and recording:
                res += sum(neededTime[start: i])-max(neededTime[start: i])
                recording = False
            last = c
        
        if recording:
            res += sum(neededTime[start:])-max(neededTime[start:])

        return res


        