class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        newlist = []
        old = 0
        for t, c in zip(releaseTimes, keysPressed): 
            newlist.append((t - old, c))
            old = t
        newlist.sort()
        return newlist[-1][1]

        