class Solution:
    def totalMoney(self, n: int) -> int:
        a=n//7
        b=n%7
        return int(a*(a-1)/2*7 + 28*a + a*b +b*(b+1)/2 )