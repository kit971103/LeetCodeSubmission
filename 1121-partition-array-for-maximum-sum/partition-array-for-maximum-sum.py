class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*n
        
        # handle the first k indexes differently
        for j in range(k): dp[j]=max(arr[:j+1])*(j+1)
        
        # we can get rid of index i by running i times
        for j in range(k,n):
            curr = []
            for m in range(k):
                curr.append(dp[j-m-1] + max(arr[(j-m):(j+1)]) * (m+1))
            dp[j] = max(curr)

        return dp[-1]
