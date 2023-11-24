class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        i = 1
        piles.sort(reverse = True)
        for _ in range(len(piles)//3):
            res += piles[i]
            i+=2
        return res

        