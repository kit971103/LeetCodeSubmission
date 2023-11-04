class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        maxtime=0
        for t in itertools.chain(left, [n-x for x in right]):
            if t > maxtime: maxtime = t
        return maxtime

        