class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        try:
            length = math.floor(math.log(n, 2))+1
        except:
            return 0
        res = count = 0
        for i in range(length, -1, -1):
            if n & (1 << i):
                count += 1
                if count%2:
                    res += 2**(i+1)-1
                else:
                    res -= 2**(i+1)-1
        return res
            
        