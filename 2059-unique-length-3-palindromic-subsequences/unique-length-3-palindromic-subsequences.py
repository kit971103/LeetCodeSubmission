class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        seen = dict()
        for i, c in enumerate(s):
            if c not in seen: seen[c] = [i,i]
            else: seen[c][1] = i
        
        not_active_range = [ (end, start, c) for c, (start, end) in seen.items() if start != end]
        not_active_range.sort(reverse = True, key = lambda x: x[1])
        active_range = []
        res = set()

        for i, c in enumerate(s):
            if not_active_range and i > not_active_range[-1][1]:
                heapq.heappush(active_range, not_active_range.pop())
            if active_range and i >= active_range[0][0]:
                heapq.heappop(active_range)
            res.update( x+c+x for _, __, x in active_range )
        return len(res)


        