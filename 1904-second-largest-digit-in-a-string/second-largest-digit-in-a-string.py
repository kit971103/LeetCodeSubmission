class Solution:
    def secondHighest(self, s: str) -> int:
        res = [None, None]
        for n in map(int, filter(lambda c: c.isnumeric(), s)):
            if n in res:
                continue

            if res[0] is None:
                res[0] = n
            elif n > res[0]:
                res[1] = res[0]
                res[0] = n
            elif res[1] is None or n > res[1]:
                res[1] = n
        return res[1] if res[1] is not None else -1
                
        