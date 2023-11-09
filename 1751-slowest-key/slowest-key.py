class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        newlist = [(releaseTimes[i] - releaseTimes[i-1], keysPressed[i]) for i in range(1, len(releaseTimes))]
        newlist.append((releaseTimes[0], keysPressed[0]))
        newlist.sort()
        return newlist[-1][1]

        