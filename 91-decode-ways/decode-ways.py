class Solution:
    one_two = ("1", "2")
    one_six = ("1","2","3","4","5","6")
    def numDecodings(self, s: str) -> int:

        if s[0] == "0":
            return 0
        
        last = s[0]
        bound = 1
        unbound = 1 if last in Solution.one_two else 0

        for cur in islice(s,1,None):
            if cur == "0":
                if last not in Solution.one_two:
                    return 0
                bound = unbound
                unbound = 0
            elif last == "1" or (last =="2" and cur in Solution.one_six):
                bound += unbound
                unbound = bound - unbound
            else:
                unbound = bound
            last = cur
        return bound
