class Solution:
    def minOperations(self, s: str) -> int:
        odd = even = 0
        for i, c in enumerate(s):
            if c == "1":
                if i%2:
                    odd+=1
                else:
                    even+=1
        return min((len(s))//2-odd+even, odd+(len(s)+1)//2-even)
        