class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == "0":
            return 0
        
        last = s[0]
        bound = 1
        unbond = 1 if last == "1" or last == "2" else 0
        
        for cur in islice(s,1,None):
            old_b = bound
            old_ub = unbond

            if cur == "0":
                
                if last in ("1", "2"):
                    bound = old_ub
                    unbond = 0
                else:
                    return 0
            elif last == "1":
                bound = old_b + old_ub
                unbond = old_b
            elif last =="2":
                bound = old_b + (old_ub if cur in ("1","2","3","4","5","6") else 0)
                unbond = old_b
            else:
                bound = old_b
                unbond = old_b
            
            last = cur
        
        return bound
