class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(itertools.islice(sorted(piles, reverse = True), 1 , len(piles)//3*2+1, 2))

        