class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for (x0, y0), (x1, y1) in itertools.pairwise(points):
            res += max(abs(x1-x0), abs(y1-y0))
        return res

        