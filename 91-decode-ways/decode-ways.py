class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == "0":
            return 0
        
        last = s[0]
        bound = 1
        unbound = 1 if int(last) < 3 else 0

        for cur in islice(s,1,None):
            if cur == "0":
                if int(last)>2:
                    return 0
                bound = unbound
                unbound = 0
            elif last == "1" or (last =="2" and int(cur) <7):
                bound += unbound
                unbound = bound - unbound
            else:
                unbound = bound
            last = cur
        return bound
