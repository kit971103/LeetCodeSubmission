class Solution:
    def knightDialer(self, n: int) -> int:

        posible_numbers_end_with = [1] * 10
        mod = 10**9+7
        for _ in range(n-1):

            temp_store = posible_numbers_end_with.copy()

            posible_numbers_end_with[0] = (temp_store[4] + temp_store[6]                )%mod
            posible_numbers_end_with[1] = (temp_store[6] + temp_store[8]                )%mod
            posible_numbers_end_with[2] = (temp_store[7] + temp_store[9]                )%mod
            posible_numbers_end_with[3] = (temp_store[4] + temp_store[8]                )%mod
            posible_numbers_end_with[4] = (temp_store[0] + temp_store[3] + temp_store[9])%mod
            posible_numbers_end_with[5] = 0
            posible_numbers_end_with[6] = (temp_store[0] + temp_store[1] + temp_store[7])%mod
            posible_numbers_end_with[7] = (temp_store[2] + temp_store[6]                )%mod
            posible_numbers_end_with[8] = (temp_store[1] + temp_store[3]                )%mod
            posible_numbers_end_with[9] = (temp_store[2] + temp_store[4]                )%mod

        return sum(posible_numbers_end_with)%mod