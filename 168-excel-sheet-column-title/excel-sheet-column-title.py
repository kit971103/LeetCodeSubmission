class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            n = columnNumber%26
            if n:
                res.append(n)
            else:
                res.append(26)
                columnNumber -= 26
            columnNumber //= 26
        
        print(res)
        return ''.join(chr(64 + n) for n in res[::-1])

        
        

