class Solution:
    def knightDialer(self, n: int) -> int:
        posible_move = [(4,6), (6,8), (7,9), (4,8), (0,3,9),  tuple(), (0,1,7), (2,6), (1,3), (2,4), (4,6)]

        posible_numbers_end_with = [1] * 10
        mod = 10**9+7
        for _ in range(n-1):
            last_iter = posible_numbers_end_with.copy()
            for i in range(10):
                posible_numbers_end_with[i] = sum(last_iter[j] for j in posible_move[i])

        return sum(posible_numbers_end_with)%mod