class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        timeSum = 0

        for x in range(len(colors) - 1):
            if colors[x] == colors[x + 1]:
                timeSum+= min(neededTime[x],neededTime[x+1])
                neededTime[x+1] = max(neededTime[x],neededTime[x+1])
        return timeSum