class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty): 
            return -1
        
        @cache
        def dp(end, d):
            if d == end:
                return sum(jobDifficulty[:end])
            elif d == 1:
                return max(jobDifficulty[:end])

            res = defalut
            for start in range(d-1,end):
                t = dp(start, d-1) + max(jobDifficulty[start:end])
                if t < res:
                    res = t
            return res
        
        defalut = sum(jobDifficulty)
        ans = dp(len(jobDifficulty), d)

        return ans

        