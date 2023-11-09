class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        status = 0
        differnt = ("","")
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if status == 0:
                    differnt = (c1, c2)
                    status = 1
                elif status == 1:
                    if not (c2, c1) == differnt: return False
                    status = 2
                else: return False
        return status != 1


        