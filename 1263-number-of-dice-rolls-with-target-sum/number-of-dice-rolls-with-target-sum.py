class Solution:
    @functools.cache
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n or target > k*n:
            return 0
        if n == 1 and (1<= target <= k):
            return 1

        res = 0
        for i in range(1, k+1):
            res += self.numRollsToTarget(n-1, k, target-i)
        return res%(10**9+7)
        