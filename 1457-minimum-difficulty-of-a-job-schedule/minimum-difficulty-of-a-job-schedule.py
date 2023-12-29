class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        @cache
        def dp(end, d):
            # print(f"{end= }, {d= }")
            if d > end : 
                # print(None)
                return None
            elif d == end:
                # print(sum(jobDifficulty[:end]))
                return sum(jobDifficulty[:end])
            
            if d == 1:
                # print(max(jobDifficulty[:end]))
                return max(jobDifficulty[:end])

            res = None
            for start in range(d-1,end):
                left = dp(start, d-1)
                if left is None:
                    continue
                right = max(jobDifficulty[start:end])
                t = left + right
                if (res is None) or(t < res):
                    res = t
            # print(res)
            return res
        
        ans = dp(len(jobDifficulty), d)

        return ans if ans is not None else -1

        