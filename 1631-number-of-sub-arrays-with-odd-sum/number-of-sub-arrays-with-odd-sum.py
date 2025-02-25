MOD = 10**9 + 7
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = even = count = 0
        for n in arr:
            if n%2:
                odd, even = even, odd
                odd += 1
            else:
                even += 1
            count += odd

            count %= MOD
            odd %= MOD
            even %= MOD

        return count
            

