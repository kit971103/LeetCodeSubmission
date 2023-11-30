class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0: return 0
        length = math.floor(math.log(n, 2))+1
        res = count = 0
        for i in range(length, -1, -1):
            if n & (1 << i):
                count += 1
                if count%2:
                    res += 2**(i+1)-1
                else:
                    res -= 2**(i+1)-1
        return res
            
        