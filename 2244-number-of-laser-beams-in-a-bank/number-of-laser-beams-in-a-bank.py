class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = decives_pre = 0
        for row in bank:
            decives_this = row.count("1")
            if decives_this!=0:
                res+=decives_pre*decives_this
                decives_pre = decives_this
        return res