class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        #
        # this is just a 2D 2-sum problem, slightly different condition
        #
        count = Counter()
        res = 0
        for x1, y1 in coordinates:
            for x in range(k + 1):
                # so we have x1^x2 = x and y1^y2=(k-x)
                # then x1^x2+y1^y2 = k
                res += count[x1 ^ x, y1 ^ (k - x)]
            count[x1, y1] += 1
        return res