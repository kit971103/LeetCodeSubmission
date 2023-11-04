class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        maxtime=0
        for a,b  in itertools.zip_longest(left, right, fillvalue = -1):
            if a!= -1 and a > maxtime: maxtime = a
            if b!=-1 and  n-b > maxtime: maxtime = n-b
        return maxtime

        