class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        timeSum = 0

        for x in range(len(colors) - 1):
            if colors[x] == colors[x + 1]:
                if neededTime[x] < neededTime[x+1]:
                    timeSum += neededTime[x]
                else:
                    timeSum += neededTime[x+1]
                    neededTime[x+1] = neededTime[x]
        #  print(timeSum)
        
        return timeSum