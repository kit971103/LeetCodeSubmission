class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            n = columnNumber%26
            if n:
                res.append(chr(64 + n))
            else:
                res.append(chr(90))
                columnNumber -= 26
            columnNumber //= 26
        return ''.join(res[::-1])

        
        

